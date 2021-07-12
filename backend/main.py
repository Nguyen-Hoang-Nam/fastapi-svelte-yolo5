import io
import uuid
from typing import Optional

from PIL import Image
from starlette.responses import Response
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import yolov5

app = FastAPI(
    title="Serving YOLO",
    description="""Recognition fruit in image""",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.post("/yolo")
def process_yolov5(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = Image.open(io.BytesIO(file_bytes))
    filename = str(uuid.uuid4())
    name = f"./static/{filename}.png"

    image.filename = name
    _, converted_img = yolov5(image)

    converted_img.save(name)
    return {"message": filename}
