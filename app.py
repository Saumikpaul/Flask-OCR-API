import easyocr
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from PIL import Image
import io
import torch

app = FastAPI()

# Initialize EasyOCR reader. It automatically uses GPU if available (from torch/torchvision installed in requirements)
try:
    reader = easyocr.Reader(['en'], gpu=torch.cuda.is_available())
    print(f"EasyOCR initialized. GPU available: {torch.cuda.is_available()}")
except Exception as e:
    print(f"Failed to initialize EasyOCR: {e}")
    reader = easyocr.Reader(['en'], gpu=False) # Fallback

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    """
    GPU-accelerated OCR endpoint using EasyOCR.
    Accepts an image file and extracts text.
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/tiff"]:
        raise HTTPException(status_code=400, detail="Invalid image format. Supported: JPEG, PNG, TIFF.")

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')

        # Perform OCR
        result = reader.readtext(image)

        # Extract and format text
        ocr_text = " ".join([text for (bbox, text, prob) in result])

        if not ocr_text:
            ocr_text = "No text detected."

        return {"filename": file.filename, "ocr_text": ocr_text, "gpu_used": torch.cuda.is_available()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.get("/")
def read_root():
    gpu_status = "GPU available" if torch.cuda.is_available() else "GPU not available, running on CPU"
    return {"message": "GPU-accelerated EasyOCR API ready", "status": gpu_status}
