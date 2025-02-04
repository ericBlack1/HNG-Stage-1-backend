from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(abs(n**0.5)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors = [i for i in range(1, abs(n)) if n % i == 0]
    return sum(divisors) == abs(n)

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d**length for d in digits) == abs(n)

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{abs(n)}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    abs_number = abs(number)

    properties = []
    if is_prime(abs_number):
        properties.append("prime")
    if is_perfect(abs_number):
        properties.append("perfect")
    if is_armstrong(abs_number):
        properties.append("armstrong")
    if abs_number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    fun_fact = get_fun_fact(abs_number)

    return {
        "number": number,
        "is_prime": is_prime(abs_number),
        "is_perfect": is_perfect(abs_number),
        "properties": properties,
        "digit_sum": digit_sum(abs_number),
        "fun_fact": fun_fact,
    }

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    invalid_input = None
    for error in exc.errors():
        if error["type"] == "int_parsing":
            invalid_input = error["input"]
            break

    return JSONResponse(
        status_code=400,
        content={"number": invalid_input, "error": True},
    )