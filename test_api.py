
import httpx
import pytest
import io
from PIL import Image

@pytest.mark.asyncio
async def test_ocr_endpoint():
    async with httpx.AsyncClient(app="app:app", base_url="http://test") as client:
        # Create a mock image using Pillow
        img = Image.new('RGB', (100, 100), color = 'red')
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        
        files = {'file': ('test_image.png', buf, 'image/png')}
        
        response = await client.post("/ocr/", files=files)
        
        assert response.status_code == 200
        assert "filename" in response.json()
        assert "ocr_text" in response.json()
        assert response.json()["filename"] == "test_image.png"

@pytest.mark.asyncio
async def test_root_endpoint():
    async with httpx.AsyncClient(app="app:app", base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "OCR API ready"}
