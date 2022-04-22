from fastapi import APIRouter, Path, Query, status, HTTPException
from pydantic import BaseModel
import database


router = APIRouter()


class FridgeInventory(BaseModel):
    name: str


#INVENTORY = ["wrap", "sausage", "bacon", "coral lettuce", "baby tomatoes", "rosemary"]


@router.get("/get-inventory")
def get_inventory():
    inventory = database.db_get_inventory()
    return {"inventory": inventory}


@router.post("/create-new-food-items/{food_name}")
def post_newfooditem(food_item: FridgeInventory):
    #search for existing food in fridge
    inventory = database.db_get_inventory()

    # Food item already exists, return error
    if food_item.name in inventory:
        raise HTTPException(status_code = 400, detail = "This food item already exists in your inventory.")
    else:
        inventory.append(food_item.name)

        database.db_update_inventory(inventory)
        raise HTTPException(status_code = 200, detail = "You have successfully added this new food item in your inventory.")


@router.delete("/delete-used-up-food")
def delete_usedfood(food_item: FridgeInventory):
    inventory = database.db_get_inventory()
    if food_item.name not in inventory:
         raise HTTPException(status_code = 400, detail = "This food item does not exist in your inventory.")   
    else:
        inventory.remove(food_item.name)
        database.db_update_inventory(inventory)
        raise HTTPException(status_code = 200, detail = "You have successfully deleted this used food from your inventory.")
        