import io

from PIL import Image

# from starlette.responses import Response
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from model import yolov5

app = FastAPI(
    title="Serving YOLO",
    description="""Recognition fruit in image""",
    version="0.1.0",
)

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


@app.post("/yolo")
def process_yolov5(file: UploadFile = File(...)):
    file_bytes = file.file.read()
    image = Image.open(io.BytesIO(file_bytes))

    coordinate = yolov5(image)

    return coordinate
