import joblib
import numpy as np
import pandas as pd
import os

MODEL_PATH = os.getenv("MODEL_PATH")

import lightgbm as lgb

def load_model():
    model = lgb.Booster(model_file=MODEL_PATH)
    return model