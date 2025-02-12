# main.py
from agent import select_tool

if __name__ == "__main__":
    print("Welcome to FitBot CLI - Your Health, Fitness, and Nutrition Assistant!")
    user_query = input("Ask FitBot a question: ")
    response = select_tool(user_query)
    print("\n" + response)
