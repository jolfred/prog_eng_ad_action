import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("/workspaces/prog_eng_ad_action/model/model.txt")


import lightgbm as lgb

def load_model():
    print("MODEL_PATH", MODEL_PATH)

    model = lgb.Booster(model_file=MODEL_PATH)
    return model