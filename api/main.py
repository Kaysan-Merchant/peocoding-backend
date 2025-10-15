#Importing FastAPI
from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Define endpoints or routes(PATH)
@app.get('/') # a "/" on its own is a root directory, sort of like a menu
def default_route():
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

