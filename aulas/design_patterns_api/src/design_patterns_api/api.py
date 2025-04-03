
from fastapi import FastAPI

api = FastAPI()

@api.get("")
def index():
    return "Hello World"

@api.post("/pay")
def process_payment(method:str):
    match method.lower():
        case "paypal":
            pass
        case "gpay":
            pass
        case "applepay":
            pass
        case "mbway":
            pass
        











# if __name__ == "__main__"
#     fastapi.