from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from pydantic import BaseModel, Field
from typing import List
from recipe import Recipe

# 1. Set up the LLMs
# The first LLM tries to generate JSON.
# We set temperature=1.0 to *encourage* it to make a mistake for this demo.
json_llm = ChatOllama(
    model="llama3.1",
    temperature=1.0, # Higher temp = more creative = higher chance of error
    format="json" 
)

# The second LLM is the "fixer". It's a standard, smart model.
# No JSON mode here, as the OutputFixingParser sends it a natural language prompt.
fixer_llm = ChatOllama(
    model="llama3.1",
    temperature=0.0 # We want the fixer to be precise
)

# 2. Set up the Parsers
# The base parser is the one we WANT to use.
base_parser = PydanticOutputParser(pydantic_object=Recipe)

# The OutputFixingParser wraps the base parser and the fixer LLM.
# It will try to use base_parser.parse().
# If it fails, it will call fixer_llm to fix the broken text.
auto_fixing_parser = OutputFixingParser.from_llm(
    llm=fixer_llm,
    parser=base_parser
)

# 3. Create the Prompt Template
# We still provide format_instructions to give the first LLM
# the best chance of succeeding.
prompt = PromptTemplate(
    template="""
    You are an expert chef.
    Create a recipe for: {query}
    
    {format_instructions}
    """,
    input_variables=["query"],
    partial_variables={"format_instructions": base_parser.get_format_instructions()}
)

# 4. Create the Chain
# The chain flows: Prompt -> json_llm (generates string) -> auto_fixing_parser
# The auto_fixing_parser handles the try/fail/fix/retry logic.
chain = prompt | json_llm | auto_fixing_parser

# 6. Execute
# Even if json_llm produces slightly malformed JSON (due to temp=1.0),
# the auto_fixing_parser will catch it, send it to fixer_llm,
# get a corrected string, and parse that into the Recipe object.
try:
    response = chain.invoke({"query": "A very complex 10-step paella"})
    
    print("--- Successfully Parsed Recipe ---")
    print(f"Dish Name: {response.name}")
    print(f"Difficulty: {response.difficulty}")
    print(f"Type of object: {type(response)}")

    # You can inspect the full object
    print("\n--- Full Object ---")
    print(response.model_dump_json(indent=2, exclude_none=True))


except Exception as e:
    # This would only happen if the fixer_llm *also* failed
    print(f"Critical error: The fixer failed to correct the output: {e}")