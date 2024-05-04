import os
import shutil
from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from detect import process_image_and_generate_text
from detect import process_image_and_generate_obj_name
from search import search_using_pse
from PIL import Image

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/image-detect", response_class=HTMLResponse)
async def get_image_detect(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def get_image_detect(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@app.post("/upload/")
async def upload_file(request: Request,file: UploadFile = File(...)):
    try:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
          
        image_pathway = f"uploads/{file.filename}"
        response_data = process_image_and_generate_text(image_path=image_pathway)

        return templates.TemplateResponse("result1.html", {"request": request, "response_data": response_data})
    except Exception as e:
        return {"message": f"Failed to upload file: {e}"}


@app.post("/search/")
async def upload_file(request: Request,file: UploadFile = File(...)):
    try:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        image_pathway = f"uploads/{file.filename}"
        response_data = process_image_and_generate_obj_name(image_path=image_pathway)

        
        if response_data and "generated_text" in response_data:
            keyword = response_data["generated_text"]
            links = search_using_pse(keyword)

            return templates.TemplateResponse("result2.html", {"request": request, "links": links, "response_data": response_data}) 
    except Exception as e:
        return {"message": f"Failed to upload file: {e}"}
