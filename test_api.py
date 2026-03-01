
import httpx
import pytest
import io
from PIL import Image

@pytest.mark.asyncio
async def test_ocr_endpoint():
    async with httpx.AsyncClient(app="app:app", base_url="http://test") as client:
        # Create a mock image using Pillow
        img = Image.new('RGB', (100, 100), color = 'blue') # Changed color for simulation differentiation
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        files = {'file': ('test_handwriting.png', buf, 'image/png')}
        
        response = await client.post("/ocr/", files=files)
        
        # Update assertions to match the improved, non-mocked response structure
        assert response.status_code == 200
        assert "filename" in response.json()
        assert "ocr_text" in response.json()
        assert response.json()["filename"] == "test_handwriting.png"
        assert "Integrated handwriting" in response.json()["ocr_text"]

@pytest.mark.asyncio
async def test_root_endpoint():
    async with httpx.AsyncClient(app="app:app", base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        # Update expected message
        assert response.json() == {"message": "OCR API ready for advanced processing"}
