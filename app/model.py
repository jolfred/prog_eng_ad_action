import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")


import lightgbm as lgb

def load_model():
    print("MODEL_PATH", MODEL_PATH)

    model = lgb.Booster(model_file=MODEL_PATH)
    return model