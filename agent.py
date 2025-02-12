# agent.py
from tools import workout_planner, meal_recommender, fitness_tip_generator
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize the chat model with GPT-4o-mini and a moderate temperature
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

def select_tool(query: str) -> str:
    """
    Uses the GPT-4o-mini model to decide which tool to use based on the query.
    If the query is outside the health, fitness, and nutrition domain,
    returns an out-of-domain message.
    """
    prompt = (
        "You are an AI fitness assistant specialized in health, fitness, and nutrition. "
        "Based on the following query, decide which tool to use: "
        "[workout planner, meal recommender, fitness tip generator] "
        "or respond with 'out-of-domain' if the query is not related.\n\n"
        f"Query: {query}\n\n"
        "Your answer:"
    )
    # Wrap the prompt as a HumanMessage for the ChatOpenAI model
    response = llm([HumanMessage(content=prompt)])
    decision = response.content.strip().lower()
    print("\n Decision : " + decision+ "\n")

    if "workout" in decision:
        return workout_planner(query)
    elif "meal" in decision:
        return meal_recommender(query)
    elif "tip" in decision:
        return fitness_tip_generator(query)
    else:
        return "I'm sorry, but I only serve queries related to health, fitness, and nutrition."
