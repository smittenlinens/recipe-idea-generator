from fastapi import FastAPI, Path, Query, status, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from routers import recipe, inventory

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Food Recommendation"}

@app.get("/about")
def about():
    return {"message": "This API helps you to generate recipe ideas based on the items you have in your fridge. You can add new food items and delete outdated recipe ideas too."}


app.include_router(recipe.router)

app.include_router(inventory.router)



