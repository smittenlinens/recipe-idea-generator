from fastapi import APIRouter, Path, Query, status, HTTPException
from pydantic import BaseModel


router = APIRouter()


class FridgeInventory(BaseModel):
    name: str


INVENTORY = ["wrap", "sausage", "bacon", "coral lettuce", "baby tomatoes", "rosemary"]


@router.get("/get-inventory")
def get_inventory():
    return INVENTORY   


@router.post("/create-new-food-items")
def post_newfooditem(food_item: FridgeInventory):
    # Food item already exists, return error
    if food_item.name in INVENTORY:
        raise HTTPException(status_code = 400, detail = "This food item already exists in your inventory.")
    else:
        INVENTORY.append(food_item.name)
        raise HTTPException(status_code = 200, detail = "You have successfully added this new food item in your inventory.")


@router.delete("/delete-used-up-food")
def delete_usedfood(food_item: FridgeInventory):
    if food_item.name not in INVENTORY:
         raise HTTPException(status_code = 400, detail = "This food item does not exist in your inventory.")
    else:
        INVENTORY.remove(food_item.name)
        return {"You have successfully deleted this used food from your inventory."}