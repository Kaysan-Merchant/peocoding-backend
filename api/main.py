#Importing FastAPI
from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware
# CORS (Cross-Origin Resource Sharing) allows us to restrict/enable which client urls are allowed to send requests to this backend code.
import psycopg2
from psycopg2.extras import RealDictCursor
# Database library that allows Python to speak with postgres

import os 
# to access the DATABASE_URL from Vercel

# Database connection
conn = psycopg2.connect( os.environ.get("DATABASE_URL") ) # must add database to project beforehand
cur = conn.cursor()

# Table created with SQL(the statement inside the """)
# IF NOT EXISTS is necessary so that it will not create the items table over4 and over
cur.execute("""
CREATE TABLE IF NOT EXISTS items (
    item_id SERIAL PRIMARY KEY,
    item_name TEXT NOT NULL,
    item_desc TEXT NOT NULL
)
""")
conn.commit()
# To make the change occur(Table being created), allows for rollbacks

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

# Define endpoints or routes(PATH)
@app.get('/') # a "/" on its own is the root directory
def default_route():
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."

@app.get("/items")
def select_all_item_records():
    """
    GET all records from database table
    """
    cur = conn.cursor(cursor_factory=RealDictCursor)  # return result as JSON
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    return data    

@app.post("/item")
def insert_new_item_record(new_item_name = Body(...), new_item_desc = Body(...),):    
    """
    POST a record to database table
    """
    cur.execute("INSERT INTO items (item_name,item_desc) VALUES (%s,%s)", (new_item_name, new_item_desc) ) 
    conn.commit()
    return {"success":True, "message": "new record added"}