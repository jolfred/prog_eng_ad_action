from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_prediction():
    payload = {
        "hour": 10,
        "day_of_week": 1,
        "week_of_year": 35,
        "mean_hour_device": 11.2,
        "is_banner": 1,
        "is_interstitial": 0,
        "is_rewarded": 0,
        "popularity_of_brand": 0.7,
        "popularity_of_device": 0.6,
        "is_apple": 1,
        "is_US": 1,
        "mean_win_bid_device": 4.1,
        "median_win_bid_device": 4.0,
        "min_win_bid_device": 3.5,
        "max_win_bid_device": 4.9,
        "mean_sent_price_device": 4.2,
        "median_sent_price_device": 4.1,
        "min_sent_price_device": 3.6,
        "max_sent_price_device": 5.0,
        "is_WIFI": 1,
        "is_3G": 0,
        "mean_win_bid_c1": 4.3,
        "mean_win_bid_c3": 4.1,
        "size_width": 300,
        "size_height": 250,
        "mediation_minor": 0.2,
        "sentPrice": 4.25
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
 