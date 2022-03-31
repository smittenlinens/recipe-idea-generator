from fastapi import APIRouter, Path, Query, status, HTTPException
from pydantic import BaseModel


router = APIRouter()


class Recipeideas(BaseModel):
    name: str

#class Updateideas(BaseModel):
    #name: str
    #recipe: List[str]


#class Recipe(BaseModel):
    #name: str
    #recipe: List[str]


RECIPE_IDEAS = {
    "chicken": ["Chicken Burrito Wrap", 
        "Japanese Cream Pasta", 
        "Pesto Chicken Toastie", 
        "Oyakodon"],
    "shiitake mushrooms": ["japchae"],
    "banana": ["oatmeal", "pancakes"],
    "oats": ["cocoa coffee overnight oats", "banana pancakes", "granola", "warm oatmeals"],
    "mushrooms": ["Japanese Cream Pasta", "Western Cream Pasta"],
    "tomato": ["tik tok pasta", "foccacia", "shashuka", "pico de gallo", "guacamole"],
    "cabbage": ["okonomiyaki", "egg mayo sandwich"],
    "tofu": ["cold tofu w/ kimchi", "kimchi jiggae", "air-fried tofu"],
    "kimchi": ["kimchi fried rice", "okonomiyaki", "kimchi jiggae", "pork lard rice w/ poached egg & edamame", "cold tofu"]
}


@router.get("/get-recipe-ideas/{food_name}")
def get_recipeideas(food_name: str = Path(None, description = "Insert the food you have that you want a recipe idea of.")):
    # for food_name_in_dict in RecipeIdeas:
    #     if RecipeIdeas[food_name_in_dict] != food_name:
    
    if food_name not in RECIPE_IDEAS:
        raise HTTPException(status_code = 404, detail = "Data for this food item does not exist.")

    return RECIPE_IDEAS[food_name]   

@router.post("/create-new-recipe-ideas/{food_name}")
def post_recipeideas(food_name: str, recipe_idea: Recipeideas):
    # Food exists, just append
    if food_name in RECIPE_IDEAS:
        # Food recipe already exists, return error
        if recipe_idea.name in RECIPE_IDEAS[food_name]:
            raise HTTPException(status_code = 400, detail = "This recipe idea already exists.")

        RECIPE_IDEAS[food_name].append(recipe_idea.name)
    # Food doesn't exists, add new
    else:
        RECIPE_IDEAS[food_name] = [recipe_idea.name]

    raise HTTPException(status_code = 200, detail = "You have successfully added this new recipe idea.")


@router.delete("/delete-outdated-recipe-ideas/{food_name}")
def delete_recipeideas(food_name: str, recipe_idea: Recipeideas):
    RECIPE_IDEAS[food_name].remove(recipe_idea.name)
    return {"You have successfully deleted this unwanted recipe idea."}

