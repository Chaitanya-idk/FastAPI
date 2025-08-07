from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import joblib

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "template"))

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')
encoder = joblib.load('encoder.joblib')

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict_sentiment(user_input: str = Form(...)):
    X_input = vectorizer.transform([user_input])
    prediction = model.predict(X_input)
    sentiment = encoder.inverse_transform(prediction)[0]
    return JSONResponse(content={"sentiment": sentiment})
