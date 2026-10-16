import fastapi as FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my Personal API!"}