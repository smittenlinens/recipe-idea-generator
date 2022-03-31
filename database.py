from pymongo import MongoClient


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

