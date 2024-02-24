import pickle
import gzip
import xgboost as xgb

# Path to the .pgz file
model_path = "./model/xgboost-iris.pgz"

with gzip.open(model_path, "rb") as f:
    xgboost_model = pickle.load(f)


def predict(input):
    pred = xgboost_model.predict(input)[0]
    print(pred)
    return pred
