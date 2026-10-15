from agno.agent import Agent


# Agent 1: Location Analysis
location_agent = Agent(
    name="Location Advisor",

    role="Analyze suitable restaurant locations in Dubai and Abu Dhabi.",

    instructions=[
        "Recommend suitable locations for restaurant expansion.",
        "Compare rental costs, foot traffic, and target customers.",
        "Explain the advantages and disadvantages of each location.",
        "Consider accessibility, competition, and delivery demand.",
        "Clearly identify estimates and information that needs verification."
    ],

    markdown=True
)


# Agent 2: Market Analysis
market_agent = Agent(
    name="Market Analysis Advisor",

    role="Analyze competitors, menu strategies, and pricing.",

    instructions=[
        "Analyze restaurant competitors in Dubai and Abu Dhabi.",
        "Identify competitors and their market positioning.",
        "Recommend menu adaptations for Meaty Pizza and Kebab Sandwiches.",
        "Consider UAE customer preferences and portion sizes.",
        "Suggest appropriate price ranges in AED.",
        "Explain the reasoning behind pricing recommendations.",
        "Do not invent competitor information or market prices."
    ],

    markdown=True
)


# Agent 3: Business Strategy
strategy_agent = Agent(
    name="Business Strategy Advisor",

    role="Develop business strategies for restaurant expansion.",

    instructions=[
        "Develop marketing and restaurant launch strategies.",
        "Recommend marketing channels and partnerships.",
        "Provide operations and staffing recommendations.",
        "Suggest delivery platform strategies.",
        "Explain basic restaurant licensing requirements.",
        "Recommend supplier and sourcing strategies.",
        "Include potential risks and actionable next steps.",
        "Distinguish verified facts from assumptions."
    ],

    markdown=True
)


print("Three AI Agents configured successfully!")