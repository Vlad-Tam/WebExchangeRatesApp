from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def test():
    return "hello world"
