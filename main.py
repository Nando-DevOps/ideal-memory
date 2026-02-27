from fastapi import FastAPI
import random

app = FastAPI()

hello = "Olá mundo!"

print(hello)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/random")
def get_random_number():
    random_number = random.randint(1, 100)
    return {"random_number": random_number}
