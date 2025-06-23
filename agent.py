from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Simulated Weather Tool
def getweather_tool(location):
    # Simulated temperatures for multiple cities
    fake_weather_data = {
        "chennai": 32,
        "mumbai": 30,
        "delhi": 35,
        "bangalore": 28,
        "hyderabad": 31,
        "kolkata": 33,
        "london": 20,
        "new york": 25,
        "tokyo": 27
    }

    # Normalize input to lowercase
    city = location.lower().strip()

    if city in fake_weather_data:
        temp = fake_weather_data[city]
        return f"The current temperature in {city.title()} is {temp} degrees Celsius"
    else:
        return f"Sorry, I don't have weather information for {location.title()}."

# Simple Calculator Tool
def calculator_tool(input: str) -> str:
    try:
        result = eval(input)
        return f"{result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Define Tools
tools = [
    Tool(
        name="getweather_tool",
        func=getweather_tool,
        description="Returns the temperature in specified city (location) (simulated)"
    ),
    Tool(
        name="calculator_tool",
        func=calculator_tool,
        description="Does math calculations"
    )
]

 # Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Run the Agent
response = agent.run("what is the temperature in chennai and the square of the temperature?")
print("Agent Response:", response)