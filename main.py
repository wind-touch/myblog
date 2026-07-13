from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "你好，博客系统启动了！"}