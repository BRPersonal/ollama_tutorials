from pydantic import BaseModel, Field
from typing import List

# 1. Define the Pydantic Schema (same as before)
class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient")
    amount: str = Field(description="Amount with units, e.g., '2 cups'")

class Recipe(BaseModel):
    name: str = Field(description="Name of the dish")
    difficulty: str = Field(description="Difficulty level: Easy, Medium, or Hard")
    prep_time_minutes: int = Field(description="Preparation time in minutes")
    ingredients: List[Ingredient]
    steps: List[str] = Field(description="List of cooking steps")
