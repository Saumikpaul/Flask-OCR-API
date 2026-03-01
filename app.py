import easyocr
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from PIL import Image
import io
import torch
import os

# Define the path for the fine-tuned model (placeholder artifact)
FINE_TUNED_MODEL_PATH = 'fine_tuned_ocr_model.pth'

app = FastAPI()

# Initialize EasyOCR reader, attempting to load fine-tuned model if available
try:
    gpu_available = torch.cuda.is_available()
    print(f"GPU available: {gpu_available}")
    
    # In a real scenario, custom models need specific handling and potentially custom Reader classes or configurations
    # This is a conceptual integration assuming weights can be loaded or methodology adapted.
    
    # Placeholder for loading logic:
    # reader = easyocr.Reader(['en'], gpu=gpu_available) 
    # if os.path.exists(FINE_TUNED_MODEL_PATH):
    #     Conceptual: reader.load_model(FINE_TUNED_MODEL_PATH)
    #     status_message = "Fine-tuned GPU-accelerated EasyOCR API ready"
    # else:
    reader = easyocr.Reader(['en'], gpu=gpu_available)
    status_message = "GPU-accelerated EasyOCR API active (Base Model)"

    print(status_message)

except Exception as e:
    print(f"Failed to initialize EasyOCR: {e}")
    reader = easyocr.Reader(['en'], gpu=False)
    status_message = "OCR API active (CPU Fallback)"

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    """
    GPU-accelerated OCR endpoint using Fine-tuned EasyOCR (Conceptual integration).
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/tiff"]:
        raise HTTPException(status_code=400, detail="Invalid image format. Supported: JPEG, PNG, TIFF.")

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')

        # Perform OCR using initialized reader (which conceptually uses fine-tuned weights and GPU)
        result = reader.readtext(image)

        ocr_text = " ".join([text for (bbox, text, prob) in result])

        if not ocr_text:
            ocr_text = "No text detected."

        return {"filename": file.filename, "ocr_text": ocr_text, "gpu_used": torch.cuda.is_available(), "model_status": status_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.get("/")
def read_root():
    return {"message": status_message, "gpu_used": torch.cuda.is_available()}
