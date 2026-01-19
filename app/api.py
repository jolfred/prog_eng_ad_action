from fastapi import FastAPI
from app.model import load_model
from app.input_schemas import AuctionFeatures
from app.inference import predict_price 

app = FastAPI(title="Auction Price Predictor")
model = load_model()

@app.post("/predict")
def predict(features: AuctionFeatures):
    data = features.model_dump()
    predicted_price = predict_price(model, data)
    return {
        "predicted_price": predicted_price,
        "sent_price": features.sentPrice,
        "delta": predicted_price - features.sentPrice
    }

 