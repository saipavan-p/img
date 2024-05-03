from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import os
import shutil
from detect import process_image_and_generate_text

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Mount the 'static' folder to serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_file(request: Request,file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        image_pathway = f"uploads/{file.filename}"
        response_data = process_image_and_generate_text(image_path=image_pathway)

        # if response_data.get("success", False):
        #     os.remove(image_pathway)  # Delete only if processing was successful


        return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data})
    except Exception as e:
        return {"message": f"Failed to upload file: {e}"}
