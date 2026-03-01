
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import io

app = FastAPI()

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    """
    Mock OCR endpoint: Accepts an image file, simulates OCR, and returns mock text.
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/tiff"]:
        raise HTTPException(status_code=400, detail="Invalid image format. Supported: JPEG, PNG, TIFF.")

    try:
        # Simulate image processing with Pillow
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Mock OCR result
        mock_text = f"Mock OCR results for {file.filename}: Extracted text simulation."
        
        return {"filename": file.filename, "ocr_text": mock_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "OCR API ready"}
