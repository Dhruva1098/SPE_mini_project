from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import math

app = FastAPI(title="Scientific Calculator API", description="API for basic scientific calculations")

templates = Jinja2Templates(directory="templates") # Initialize Jinja2 templates, directory is 'templates'


@app.get("/sqrt/{number}")
async def square_root(number: float):
    if number < 0:
        raise HTTPException(status_code=400, detail="Cannot calculate square root of a negative number")
    return {"result": math.sqrt(number)}

@app.get("/factorial/{number}")
async def calculate_factorial(number: int):
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        raise HTTPException(status_code=400, detail="Factorial is not defined for negative numbers")
    if number > 100:  # Example threshold - adjust as needed. Factorial of 100 is already huge!
        raise HTTPException(status_code=400, detail="Factorial calculation is limited to numbers <= 100 for performance reasons.")
    try:
        return {"result": math.factorial(number)}
    except ValueError: # This might still catch issues for extremely large inputs beyond Python's integer limit, though less likely now
        raise HTTPException(status_code=400, detail="Factorial calculation out of range for this input")

@app.get("/ln/{number}")
async def natural_logarithm(number: float):
    if number <= 0:
        raise HTTPException(status_code=400, detail="Natural logarithm is not defined for non-positive numbers")
    return {"result": math.log(number)}

@app.get("/power/{base}/{exponent}")
async def power_function(base: float, exponent: float):
    return {"result": math.pow(base, exponent)}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Scientific Calculator API. Access operations via /sqrt, /factorial, /ln, /power endpoints. For UI, go to /ui"}

# New endpoint to serve the HTML UI
@app.get("/ui", response_class=HTMLResponse)
async def calculator_ui(request: Request):
    return templates.TemplateResponse("calculatpr.html", {"request": request}) # 'request' context is needed for templates