from fastapi import APIRouter, Path, Query, status, HTTPException
from pydantic import BaseModel
import database


router = APIRouter()


class Recipeideas(BaseModel):
    name: str

#class Updateideas(BaseModel):
    #name: str
    #recipe: List[str]


#class Recipe(BaseModel):
    #name: str
    #recipe: List[str]


# RECIPE_IDEAS = {
#     "chicken": ["Chicken Burrito Wrap", 
#         "Japanese Cream Pasta", 
#         "Pesto Chicken Toastie", 
#         "Oyakodon"],
#     "shiitake mushrooms": ["japchae"],
#     "banana": ["oatmeal", "pancakes"],
#     "oats": ["cocoa coffee overnight oats", "banana pancakes", "granola", "warm oatmeals"],
#     "mushrooms": ["Japanese Cream Pasta", "Western Cream Pasta"],
#     "tomato": ["tik tok pasta", "foccacia", "shashuka", "pico de gallo", "guacamole"],
#     "cabbage": ["okonomiyaki", "egg mayo sandwich"],
#     "tofu": ["cold tofu w/ kimchi", "kimchi jiggae", "air-fried tofu"],
#     "kimchi": ["kimchi fried rice", "okonomiyaki", "kimchi jiggae", "pork lard rice w/ poached egg & edamame", "cold tofu"]
# }


@router.get("/get-recipe-ideas/{food_name}")
def get_recipeideas(food_name: str = Path(None, description = "Insert the food you have that you want a recipe idea of.")):
    # for food_name_in_dict in RecipeIdeas:
    #     if RecipeIdeas[food_name_in_dict] != food_name:
    
    recipe = database.db_get_recipe(food_name)
    if not recipe:
        raise HTTPException(status_code = 404, detail = "Data for this food item does not exist.")

    return recipe["recipe"]

@router.post("/create-new-recipe-ideas/{food_name}")
def post_recipeideas(food_name: str, recipe_idea: Recipeideas):
    # Search for existing recipe
    recipe = database.db_get_recipe(food_name)

    # Food exists
    if recipe:
        # Food recipe already exists in DB recipe field, return error
        if recipe_idea.name in recipe["recipe"]:
            raise HTTPException(status_code = 400, detail = "This recipe idea already exists.")

        # Append new recipe idea into recipe
        recipe["recipe"].append(recipe_idea.name)

        # Update DB document
        database.db_update_recipe(food_name, recipe["recipe"])
    # Food doesn't exists
    else:
        # Create new recipe DB document
        recipe = {
            "name": food_name,
            "recipe": [recipe_idea.name]
        }
        database.db_insert_recipe()
    
    raise HTTPException(status_code = 200, detail = "You have successfully added this new recipe idea.")


@router.delete("/delete-outdated-recipe-ideas/{food_name}")
def delete_recipeideas(food_name: str, recipe_idea: Recipeideas):
    recipe = database.db_get_recipe(food_name)
    if recipe:
        if recipe_idea.name not in recipe["recipe"]:
            raise HTTPException(status_code = 400, detail = "This recipe idea does not exist.")
        recipe["recipe"].delete(recipe_idea.name)

        database.db_update_recipe(food_name, recipe["recipe"])
    else:
        raise HTTPException(status_code = 400, detail = "This food item does not exist.")

