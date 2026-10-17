import os
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from agno.models.openai import OpenAIChat
from agno.team import Team

from agents import location_agent, market_agent, strategy_agent

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY was not found!")

console = Console()


advisor_team = Team(
    name="UAE Restaurant Expansion Team",
    model=OpenAIChat(id="gpt-4o-mini"),
    debug_mode=False,
    members=[
        location_agent,
        market_agent,
        strategy_agent,
    ],
    instructions=[
        # Role
        "You are the main advisor for a Jordanian restaurant expanding into Dubai and Abu Dhabi.",
        "The restaurant specializes in Meaty Pizza and Kebab Sandwiches.",
        # Delegation
        "Delegate location-related questions to the Location Advisor.",
        "Delegate competitor, menu, and pricing questions to the Market Analysis Advisor.",
        "Delegate marketing, operations, delivery, licensing, and seasonality questions to the Business Strategy Advisor.",
        # Output format
        "Always structure the final answer as: Executive Summary, Recommendation (rank the options), Trade-offs, Risks, Next Steps.",
        "Explain the reasoning behind your recommendations.",
        "Make next steps specific to this restaurant, saying who should do what.",
        "End with a 'Data Confidence' line: say whether the answer is based on verified web sources (with links) or on general knowledge and estimates.",
        # Honesty about data
        "If the members could not verify information through web search, say so clearly at the start instead of saying 'based on findings'.",
        "Never state specific prices, competitor names, or links unless they appear in a member's web search results. Otherwise give general guidance labeled as unverified estimates.",
        "Do not present estimates or assumptions as verified facts.",
        "Only claim that information is verified when it is supported by direct source links obtained from agent web searches. Otherwise, clearly label it as unverified.",
        # Specific rules
        "You may name sub-areas, streets, or malls as suggestions from general knowledge, labeled as unverified. Describe rent as relative bands (low/medium/high) when exact numbers are unverified.",
        "Competitors must include kebab/shawarma shops and Levantine restaurants, not only pizza chains. Put the source link next to each competitor. Do not treat dishes (like 'seekh kebab') or directory sites as restaurants.",
        "Explain how our restaurant should differ from each competitor category on price, audience, and product.",
        "For pricing answers, present three tiers (value, mid-range, premium), say which tier we recommend and why, and label all AED figures as unverified estimates unless they come from a cited source.",
    ],
    markdown=True,
)


if __name__ == "__main__":

    console.print("[bold]Welcome to UAE Restaurant Expansion Advisor![/bold]")
    console.print("Type 'exit' to quit.\n")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            console.print("Goodbye!")
            break

        if not question:
            continue

        try:
            
            with console.status("Thinking..."):
                response = advisor_team.run(question)

            console.print("\n[bold cyan]Advisor:[/bold cyan]")
            console.print(Markdown(response.content))

        except Exception as e:
           
            console.print(f"[red]Something went wrong: {e}[/red]")