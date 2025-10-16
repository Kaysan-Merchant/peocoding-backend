#Importing FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# CORS (Cross-Origin Resource Sharing) allows us to restrict/enable which client urls are allowed to send requests to this backend code.
import random

# Initialize the FastAPI application

FOOD_CHOICES = [
    "Pizza 🍕",
    "Tacos 🌮",
    "Sushi 🍣",
    "Classic Burger 🍔",
    "Thai Curry 🌶️",    
    "Grilled Cheese & Tomato 🍅",
    "Chicken Shawarma 🐔",
    "Vegan Bowl 🥗",
    "Pho Noodle Soup 🍲"
]

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

# Define endpoints or routes(PATH)
@app.get('/') # a "/" on its own is the root directory
def default_route():
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

@app.get("/example")  
def get_example():    
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!", "year":2025}

@app.get("/example2")  
def get_example2(name):    # can also pass in parameters
    """
    This endpoint takes in a parameter called "name"  
    """ # The frontend will communicate with the backend with the name parameter to present a name
    return {"message": f"Hello {name}!"} # Remember to indent the return
    # f before the quotation enables the embedding of a variable inside the string

    # When a user sends a GET request to '/random-choice', this function runs.

@app.get("/random-choice")
def get_random_food_choice():
    """
    Returns a single random food choice from the FOOD_CHOICES list.
    """
    # Use the built-in Python 'random' module to pick one item.
    selected_choice = random.choice(FOOD_CHOICES)
    
    # Return a Python dictionary, which FastAPI converts to a JSON response.
    return {"status": "success", "choice": selected_choice}
