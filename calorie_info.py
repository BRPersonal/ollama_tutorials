from pydantic import BaseModel, Field

class Macros(BaseModel):
  carbs: float
  protein: float
  fat: float

class CalorieInfo(BaseModel):
  food_item_name: str
  calories: float
  macros: Macros
