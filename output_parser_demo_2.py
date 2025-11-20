from langchain_core.prompts import ChatPromptTemplate
from recipe import Recipe
from utils.llm_manager import get_llm


# 1. Initialize the LLM
# !!NOTE!! We DO NOT use format="json".
# The with_structured_output method handles the formatting.
llm = get_llm(
    model="llama3.1",
    temperature=0.0
)

# 2. Bind the schema to the LLM
# This one line adds all the validation, parsing, and
# auto-correction logic.
structured_llm = llm.with_structured_output(Recipe)

# 3. Create the Prompt Template
# !!NOTze!! We DO NOT need {format_instructions}.
# The structured_llm automatically injects the schema
# as a "tool" for the LLM to use.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert chef. You must generate a recipe for the user's request."),
    ("human", "Please create a recipe for: {query}")
])

# 4. Create the Chain
chain = prompt | structured_llm

# 5. Execute
try:
    # The output is directly a Pydantic object, fully validated.
    response = chain.invoke({"query": "A simple grilled cheese sandwich"})
    
    print("--- Successfully Parsed Recipe ---")
    print(f"Dish Name: {response.name}")
    print(f"First Ingredient: {response.ingredients[0].name}")
    print(f"Type of object: {type(response)}")
    
    # You can inspect the full object
    print("\n--- Full Object ---")
    print(response.model_dump_json(indent=2, exclude_none=True))

except Exception as e:
    print(f"Error during structured output: {e}")