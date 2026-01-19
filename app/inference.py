import numpy as np

FEATURES_ORDER = [
    'hour','day_of_week','week_of_year','mean_hour_device',
    'is_banner','is_interstitial','is_rewarded',
    'popularity_of_brand','popularity_of_device',
    'is_apple','is_US',
    'mean_win_bid_device','median_win_bid_device',
    'min_win_bid_device','max_win_bid_device',
    'mean_sent_price_device','median_sent_price_device',
    'min_sent_price_device','max_sent_price_device',
    'is_WIFI','is_3G',
    'mean_win_bid_c1','mean_win_bid_c3',
    'size_width','size_height',
    'mediation_minor','sentPrice'
]

def predict_price(model, data: dict) -> float:
    x = np.array([[data[f] for f in FEATURES_ORDER]], dtype=np.float32)
    return float(model.predict(x)[0])
