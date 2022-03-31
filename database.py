from pymongo import MongoClient
from bson import ObjectId


#The recipe here refers to database, not collection
client = MongoClient("mongodb://localhost:27017")
db = client.recipe


def db_get_recipes():
    recipes = list(db["recipe"].find({}))
    return recipes


def db_get_recipe(food_name):
    recipe = db["recipe"].find_one({"name": food_name})
    return recipe


def db_insert_recipe(recipe):
    db["recipe"].insert_one(recipe)


def db_update_recipe(food_name, recipe):
    db["recipe"].update_one(
        {
            "name": food_name
        },
        {
            "$set": {"recipe": recipe}
        }
    )


def db_get_inventory():
    inventory = db["inventory"].find_one({
        "_id": ObjectId("6245590b80b4512dc22718ac")
    })
    return inventory["inventory"]

def db_update_inventory(food_item):
    db["inventory"].update_one(
        {
            "_id": ObjectId("6245590b80b4512dc22718ac")
        },
        {
            "$set": {"inventory": food_item}
        }
    )


