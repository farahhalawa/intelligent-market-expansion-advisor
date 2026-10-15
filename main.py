from agno.team import Team

from agents import location_agent, market_agent, strategy_agent


advisor_team = Team(
    name="UAE Restaurant Expansion Team",

    members=[
        location_agent,
        market_agent,
        strategy_agent
    ],

    instructions=[
        "You are the main advisor for a Jordanian restaurant expanding into Dubai and Abu Dhabi.",
        "The restaurant specializes in Meaty Pizza and Kebab Sandwiches.",

        "Delegate location-related questions to the Location Advisor.",
        "Delegate competitor, menu, and pricing questions to the Market Analysis Advisor.",
        "Delegate marketing, operations, delivery, and licensing questions to the Business Strategy Advisor.",

        "Combine the findings into clear business recommendations.",
        "Explain the reasoning behind your recommendations.",
        "Include risks, tradeoffs, and actionable next steps.",
        "Do not present estimates or assumptions as verified facts."
    ],

    markdown=True
)


print("UAE Restaurant Expansion Team created successfully!")