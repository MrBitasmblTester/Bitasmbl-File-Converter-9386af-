from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import tempfile, os

router = APIRouter(prefix="/convert")

@router.post("/pdf-to-text")
async def pdf_to_text(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Unsupported file type")
    tmp_in = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    tmp_in.write(await file.read())
    tmp_in.close()
    out_path = tmp_in.name + ".txt"
    # TODO: use PyPDF2 to write text to out_path
    open(out_path, "w").write("")
    return FileResponse(out_path, filename="converted.txt")