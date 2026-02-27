hello = "Olá mundo!"

print(hello)
from fastapi import FastAPI
import random

ola = "Hello World"

print(ola)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/random")
def get_random_number():
    random_number = random.randint(1, 100)
    return {"random_number": random_number}
