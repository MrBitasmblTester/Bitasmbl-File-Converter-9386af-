from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import tempfile, os
from .services_converters import image_to_png_file

router = APIRouter(prefix="/images")

@router.post("/to-png")
async def to_png(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, "Unsupported file type")
    tmp_in = tempfile.NamedTemporaryFile(delete=False)
    tmp_in.write(await file.read())
    tmp_in.close()
    out_path = tmp_in.name + ".png"
    image_to_png_file(tmp_in.name, out_path)
    return FileResponse(out_path, filename="converted.png")