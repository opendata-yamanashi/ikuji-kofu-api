from fastapi import FastAPI
import os 
import sys
from pathlib import Path
DIR = Path(__file__).absolute().parent
sys.path.append(str(DIR))
from data import ReadDatas
data = ReadDatas()
data.main()

root_path = os.getenv("ROOT_PATH", "")
app = FastAPI(
    title="子育て施設一覧(保育園・幼稚園・認定こども園等) API",
    root_path=root_path
)

@app.get("/")
def hello():
    return "Hello! Please access /docs"

@app.get("/list/")
def get_data():
    return data.df.T

@app.get("/query/")
def do_query(q=None):
    return data.query(q).T

@app.get("/version/")
def get_version():
    return {"version": data.get_version()}