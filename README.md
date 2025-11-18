# ollama_tutorials
Sample python scripts that demoes using local AI models with Ollama

steps
------
Install Ollama and make sure it is running locally
$ ollama pull llama3.1

see the list of models avaialable locally
$ ollama list

$ uv init --python 3.13

verify that  python version to 3.13 in pyproject.toml
$ cat pyproject.toml
requires-python = ">=3.13"
verify .python-version
$ cat .python-version 
3.13

$ uv add langchain langchain-community pydantic
 

$ uv run output_parser_demo_1.py
--- Successfully Parsed Recipe ---
Dish Name: Complex Paella
Difficulty: Hard
Type of object: <class 'recipe.Recipe'>

--- Full Object ---
{
  "name": "Complex Paella",
  "difficulty": "Hard",
  "prep_time_minutes": 120,
  "ingredients": [
    {
      "name": "Saffron threads",
      "amount": "1/2 teaspoon"
    },
    {
      "name": "Chorizo, sliced",
      "amount": "1 cup"
    },
    {
      "name": "Shrimp, peeled and deveined",
      "amount": "1 pound"
    },
    {
      "name": "Mussels, scrubbed",
      "amount": "1 pound"
    },
    {
      "name": "Artichoke hearts, canned",
      "amount": "1 can"
    },
    {
      "name": "Tomatoes, diced",
      "amount": "2 cups"
    },
    {
      "name": "Olive oil",
      "amount": "3 tablespoons"
    },
    {
      "name": "Garlic, minced",
      "amount": "4 cloves"
    },
    {
      "name": "Smoked paprika",
      "amount": "1 teaspoon"
    },
    {
      "name": "Salt and pepper",
      "amount": "to taste"
    }
  ],
  "steps": [
    "Preheat the oven to 400°F (200°C).",
    "Heat the olive oil in a large paella pan over medium-high heat.",
    "Add the sliced chorizo and cook until browned, about 5 minutes. Remove from the pan and set aside.",
    "Add the minced garlic and cook for 1 minute.",
    "Add the shrimp, mussels, artichoke hearts, tomatoes, saffron threads, smoked paprika, salt, and pepper. Stir to combine.",
    "Bring the mixture to a boil, then reduce the heat to low and simmer for 10 minutes.",
    "Stir in the cooked chorizo and cook for an additional 2-3 minutes.",
    "Transfer the paella pan to the preheated oven and bake for 15-20 minutes, or until the rice is cooked and the liquid has been absorbed.",
    "Remove the paella from the oven and let it rest for 5 minutes before serving."
  ]
}

$ uv run output_parser_demo_2.py
--- Successfully Parsed Recipe ---
Dish Name: Simple Grilled Cheese Sandwich
First Ingredient: 2 slices of bread
Type of object: <class 'recipe.Recipe'>

--- Full Object ---
{
  "name": "Simple Grilled Cheese Sandwich",
  "difficulty": "EASY",
  "prep_time_minutes": 5,
  "ingredients": [
    {
      "name": "2 slices of bread",
      "amount": ""
    },
    {
      "name": "1-2 slices of cheese (such as cheddar, mozzarella, or provolone)",
      "amount": ""
    },
    {
      "name": "Butter or non-stick cooking spray",
      "amount": ""
    }
  ],
  "steps": [
    "Preheat a grill pan or skillet over medium heat.",
    "Butter one side of each slice of bread.",
    "Place one slice of bread, buttered side down, in the preheated pan.",
    "Add 1-2 slices of cheese on top of the bread in the pan.",
    "Place the second slice of bread, buttered side up, on top of the cheese.",
    "Cook for 2-3 minutes or until the bread is golden brown and the cheese is melted.",
    "Flip the sandwich over and cook for an additional 2-3 minutes or until the other side is also golden brown.",
    "Remove from heat and serve immediately."
  ]
}
