import json
import requests
from pydantic import BaseModel, ValidationError

BASE_URL = "https://crudcrud.com/api/7c8db016ed7c4188bb0ea746fa8d4584/recipes"

class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str

initial_data = [
    { "name": "Khachapuri",  "cuisine": "Georgian", "time_minutes": "30" },
    { "name": "Khinkali",    "cuisine": "Georgian", "time_minutes": "60" },
    { "name": "Mtsvadi",     "cuisine": "Georgian", "time_minutes": "45" }
]
with open("recipes.json", "w") as f:
    json.dump(initial_data, f)

try:
    with open("recipes.json", "r") as f:
        local_recipes = json.load(f)
    
    for r in local_recipes:
        validated_recipe = Recipe(**r)
        response = requests.post(BASE_URL, json=validated_recipe.model_dump(), timeout=5)
        response.raise_for_status()
    print("რეცეპტები წარმატებით აიტვირთა.\n")

    response = requests.get(BASE_URL, timeout=5)
    response.raise_for_status()
    all_recipes = response.json()
    
    print("ყველა რეცეპტი:")
    for r in all_recipes:
        print(f"- {r['name']} ({r['time_minutes']} mins)")
    print()

    if all_recipes:
        first_id = all_recipes[0]["_id"]
        response = requests.get(f"{BASE_URL}/{first_id}", timeout=5)
        response.raise_for_status()
        single_recipe = response.json()
        print(f"პირველი რეცეპტის დეტალები (ID: {first_id}):", single_recipe, "\n")

        updated_data = {
            "name": "Super Khachapuri",
            "cuisine": "Georgian",
            "time_minutes": "40"
        }
        Recipe(**updated_data)
        
        response = requests.put(f"{BASE_URL}/{first_id}", json=updated_data, timeout=5)
        response.raise_for_status()
        
        with open("updated_recipe.json", "w") as f:
            json.dump(updated_data, f)
        print("პირველი რეცეპტი განახლდა და შეინახა ფაილში.\n")

    if len(all_recipes) > 1:
        last_id = all_recipes[-1]["_id"]
        response = requests.delete(f"{BASE_URL}/{last_id}", timeout=5)
        response.raise_for_status()
        print(f"ბოლო რეცეპტი (ID: {last_id}) წაიშალა.\n")

        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        print("დარჩენილი რეცეპტები:")
        for r in response.json():
            print(f"- {r['name']}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP შეცდომა (4xx/5xx): {e}")
except requests.exceptions.ConnectTimeout:
    print("შეცდომა: სერვერმა პასუხი დააგვიანა (Timeout).")
except ValidationError as e:
    print(f"Pydantic-ის ვალიდაციის შეცდომა:\n{e}")
except Exception as e:
    print(f"გაუთვალისწინებელი შეცდომა: {e}")