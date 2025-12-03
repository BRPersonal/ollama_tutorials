from langchain_core.prompts import PromptTemplate
from calorie_info import CalorieInfo
from utils.llm_manager import get_llm
from utils.config import settings

llm = get_llm("gpt-4o-mini", temperature=0.7, format="json")
structured_llm = llm.with_structured_output(CalorieInfo)

prompt = PromptTemplate(
    template=(
        "You are an expert nutritionist. You must give accurate calorie info with macros splitup.\n"
        "IMPORTANT: Ensure macros add up correctly (carbs * 4 + protein * 4 + fat * 9 = total calories).\n"
        "Please provide calorie info for: {query}"
    ),
    input_variables=["query"]
)

# 4. Create the Chain
chain = prompt | structured_llm


def fetch_calories(food_item):
  response = chain.invoke({"query": food_item})
  validate_calories(response)
  return response.model_dump_json(indent=2, exclude_none=True)

def validate_calories(response: CalorieInfo) -> CalorieInfo:
    calculated = (
        response.macros.carbs * 4 + 
        response.macros.protein * 4 + 
        response.macros.fat * 9
    )
    if abs(calculated - response.calories) > 5:  # Allow 5 cal tolerance
        # Adjust calories to match macros
        response.calories = round(calculated)
    return response

if __name__ == "__main__":
  print(fetch_calories("two slices of Bread Sandwich"))
  print(fetch_calories(" வீட்டில செஞ்ச ரசம் சாதம்"))
