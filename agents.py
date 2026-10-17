from agno.agent import Agent
from agno.models.openai import OpenAIChat

from agno.tools.duckduckgo import DuckDuckGoTools

MODEL_ID = "gpt-4o-mini"


# Agent 1: Location Analysis
location_agent = Agent(
    name="Location Advisor",
    role="Analyze suitable restaurant locations in Dubai and Abu Dhabi.",
    model=OpenAIChat(id=MODEL_ID),
    tools=[DuckDuckGoTools()],
    instructions=[
        "The restaurant sells Meaty Pizza and Kebab Sandwiches, so match locations to that audience.",
        "Recommend suitable locations for restaurant expansion.",
        "Compare rental costs, foot traffic, and target customers.",
        "Explain the advantages and disadvantages of each location.",
        "Consider accessibility, competition, and delivery demand.",
        "Use web search to research current market information and prioritize reliable sources.",
        "Include source links when available.",
        "Do not invent rental prices, statistics, or market data.",
        "Clearly identify estimates and information that needs verification.",
        "If web search fails or returns no results, say so clearly and do not give specific prices, competitor names, or links.",
    ],
    add_datetime_to_context=True,
    markdown=True,
)


# Agent 2: Market Analysis (competitors, menu, pricing)
market_agent = Agent(
    name="Market Analysis Advisor",
    role="Analyze competitors, menu strategies, and pricing.",
    model=OpenAIChat(id=MODEL_ID),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Always focus on the user's specific question and give direct recommendations first.",
        "Competitor categories to consider: shawarma and kebab shops, Levantine/Lebanese restaurants, pizza chains, premium pizza restaurants, and burger/grill chains.",
        "Do not list restaurant directories or review sites (such as Zomato) as competitors.",
        "Identify competitors and explain their market positioning.",
        "If the user asks about menu adaptations, focus on the menu and give the exact number of items requested.",
        "For each menu item explain: ingredients, portion size, target customers, and why it suits the UAE market.",
        "Recommend menu adaptations for Meaty Pizza and Kebab Sandwiches, considering UAE preferences and portion sizes.",
        "Suggest price ranges in AED and explain the pricing logic.",
        "Use web search to research current competitors, menus, and prices. Prioritize official restaurant websites.",
        "Include source links when available.",
        "Do not invent competitor names, menu prices, or market statistics.",
        "If reliable data is unavailable, give practical suggestions labeled as recommendations, not verified facts.",
        "If web search fails or returns no results, say so clearly and do not give specific prices, competitor names, or links.",
    ],
    add_datetime_to_context=True,
    markdown=True,
)


# Agent 3: Business Strategy (marketing, operations, licensing, etc.)
strategy_agent = Agent(
    name="Business Strategy Advisor",
    role="Develop business strategies for restaurant expansion.",
    model=OpenAIChat(id=MODEL_ID),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Always focus on the user's specific question and give direct recommendations first.",
        "Develop marketing and launch strategies: channels, messaging, and partnerships.",
        "Provide operations and staffing recommendations.",
        "If asked about staffing, give roles, headcount, responsibilities, and estimated monthly salaries in AED with assumptions.",
        "Recommend shift schedules based on restaurant size and operating hours.",
        "Suggest delivery platform strategies.",
        "Explain basic licensing requirements and prioritize official government websites.",
        "Recommend supplier and sourcing strategies.",
        "Consider cultural seasonality: Ramadan, Eid, summer, and UAE National Day.",
        "Explain operational challenges, risks, and practical solutions, and end with next steps.",
        "Use web search for current UAE regulations, staffing, and market information. Include source links when available.",
        "Do not invent licensing fees, regulations, or statistics.",
        "Do not present estimated salaries or costs as verified facts.",
        "If web search fails or returns no results, say so clearly and do not give specific prices, competitor names, or links.",
    ],
    add_datetime_to_context=True,
    markdown=True,
)