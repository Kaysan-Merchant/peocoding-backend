#Importing FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# CORS (Cross-Origin Resource Sharing) allows us to restrict/enable which client urls are allowed to send requests to this backend code.
import random

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 24, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"},
    ]

# Define endpoints or routes(PATH)
@app.get('/') # a "/" on its own is the root directory
def default_route():
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

@app.get("/list")  
def get_list():    
    """
    This endpoint returns a list of JSON objects.
    """
    return data