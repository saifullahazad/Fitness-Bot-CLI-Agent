# FitBot CLI

FitBot CLI is a domain-specific command-line application that serves as your personal health, fitness, and nutrition assistant. It intelligently routes user queries to the appropriate tool based on the query content—whether it's for generating a workout plan, suggesting meal recommendations, or providing general fitness tips. If a query falls outside the defined domain, FitBot gracefully notifies the user that it only handles health, fitness, and nutrition inquiries.

## Overview

FitBot CLI leverages the cost-effective GPT-4o-mini model via LangChain to analyze and process user input. By using prompt engineering and tool selection, the application showcases my expertise in AI-based design and development, as well as domain-specific query handling.

**Key Features:**
- **Domain-Specific Query Handling:** Routes queries to the correct tool:
  - **Workout Planner:** Generates a simple workout plan.
  - **Meal Recommender:** Provides meal suggestions and dietary tips.
  - **Fitness Tip Generator:** Offers motivational fitness advice.
- **Out-of-Domain Detection:** Replies with a polite message if a query is not related to health, fitness, or nutrition.
- **Cost-Efficient AI Integration:** Uses GPT-4o-mini for processing.
- **Extensible Design:** Built to easily add more tools or features in the future.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Fitness-Bot-CLI-Agent.git
   cd Fitness-Bot-CLI-Agent
## Example
### In-Domain Query

Ask FitBot a question: I need a workout plan to build muscle.

#### Expected Response

Here’s a simple workout plan based on your goal: [Plan details].

### Out-of-Domain Query

#### Ask FitBot a question: What's the weather today?
#### Expected Response

I'm sorry, but I only serve queries related to health, fitness, and nutrition.
