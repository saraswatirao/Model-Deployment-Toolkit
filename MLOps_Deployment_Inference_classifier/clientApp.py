from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from components.utils import decodeImage
from predict import DogCatClassifier

app = FastAPI()
templates = Jinja2Templates(directory="templates")

origins = ["*"]  # You should replace "*" with the specific origins that are allowed to access your API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DogCatClassifier(self.filename)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict_route(image: dict):
    try:
        decodeImage(image['image'], ClientApp().filename)
        result = ClientApp().classifier.prediction_dog_cat()
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000, log_level="info")
