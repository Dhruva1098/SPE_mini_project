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
    if number < 0:
        raise HTTPException(status_code=400, detail="Factorial is not defined for negative numbers")
    try:
        return {"result": math.factorial(number)}
    except ValueError: # For very large numbers that exceed factorial limits
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