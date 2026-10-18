# Intelligent Market Expansion Advisor

## Project Overview

Intelligent Market Expansion Advisor is a Python-based multi-agent AI system developed using the Agno framework.

The project helps a Jordanian restaurant specializing in Meaty Pizza and Kebab Sandwiches explore expansion opportunities in Dubai and Abu Dhabi, UAE.

The system uses three specialized AI agents to provide recommendations about restaurant locations, competitors, menu development, pricing, marketing, and business operations.

The agents work together through an Agno Team, which coordinates tasks and combines their findings into business recommendations.

The system also supports web research to help the agents find relevant market information. However, search results and estimated costs may require additional verification before making business decisions.

## AI Agents Architecture

The system consists of three specialized AI agents
coordinated through an Agno Team.

### 1. Location Advisor

The Location Advisor analyzes potential restaurant
locations in Dubai and Abu Dhabi.

Responsibilities:
- Recommend suitable restaurant locations.
- Compare rental costs and foot traffic.
- Analyze target customers.
- Evaluate accessibility and competition.
- Consider delivery demand.
- Provide source links when available.

### 2. Market Analysis Advisor

The Market Analysis Advisor focuses on competitors,
menu development, and pricing strategies.

Responsibilities:
- Analyze restaurant competitors.
- Compare competitor positioning and menu prices.
- Recommend menu adaptations.
- Suggest pricing strategies in AED.
- Consider UAE customer preferences.
- Support recommendations with web research.

### 3. Business Strategy Advisor

The Business Strategy Advisor provides recommendations
for restaurant operations and business expansion.

Responsibilities:
- Develop marketing strategies.
- Recommend staffing and operational plans.
- Suggest delivery strategies.
- Explain restaurant licensing requirements.
- Recommend supplier and sourcing strategies.
- Identify business risks and practical solutions.

### Agno Team Coordination

The three agents are connected using the Agno Team
framework.

The team receives the user's question and determines
which specialized agent should handle the task.

The selected agent analyzes the question and can use
web search tools to retrieve relevant information.

The team then uses the agent's findings to generate
a final business recommendation.

### System Workflow

```text
User Question
     |
     v
  Agno Team
     |
     v
Task Delegation
     |
     +-- Location Advisor
     |
     +-- Market Analysis Advisor
     |
     +-- Business Strategy Advisor
     |
     v
Analysis and Web Research
     |
     v
Final Recommendation
```

## Technologies and Tools

The project was developed using the following technologies:

### Python

Python is the main programming language used to
build and run the application.

### Agno Framework

Agno is used to create the three AI agents and
coordinate their tasks through an Agno Team.

### OpenAI GPT-4o-mini

The agents use the GPT-4o-mini model to understand
user questions, analyze information, and generate
business recommendations.

### DuckDuckGo Search

DuckDuckGoTools provides web search capabilities
to help agents research market information.

Search results may be incomplete or outdated,
so important information requires verification.

### python-dotenv

The python-dotenv library loads the OpenAI API key
from a local .env file.

The .env file is excluded from Git tracking
to protect sensitive information.

### Rich

Rich is used to format the final responses
in the terminal for better readability.

### Git and GitHub

Git is used for version control, while GitHub
is used to store and share the project repository.

### Command-Line Interface (CLI)

The application uses a text-based interface
where users can enter questions and receive
business recommendations.

## Installation and Setup

Follow the steps below to install and run the Intelligent Market Expansion Advisor.

### Prerequisites

Make sure the following are available:

- Python 3.12
- OpenAI API Key
- Internet connection
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/farahhalawa/intelligent-market-expansion-advisor.git
```

Navigate to the project directory:

```bash
cd intelligent-market-expansion-advisor
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Install Dependencies

Install the required Python libraries:

```bash
python -m pip install -r requirements.txt
```

The requirements include Agno, OpenAI, DuckDuckGo Search, python-dotenv, and Rich.

### Step 3: Configure Environment Variables

Create a `.env` file in the project's root directory.

Add the following variable:

```env
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with a valid OpenAI API key.

**Security Note:** The `.env` file must remain private and should never be committed to GitHub.

### Step 4: Run the Application

Start the application:

```bash
python main.py
```

The application will start an interactive command-line interface.

### Step 5: Ask a Question

Once the application starts, enter a restaurant expansion question.

Example:

```text
What are the best locations to open a Jordanian restaurant in Dubai?
```

The Agno Team coordinates the relevant AI agents and generates a business recommendation.

Additional example questions:

```text
Who are the main competitors for Meaty Pizza and Kebab Sandwiches in Dubai?
```

```text
What pricing strategy should we use for our restaurant in Abu Dhabi?
```

```text
Recommend a marketing strategy for launching our restaurant in Dubai.
```

### Step 6: Exit the Application

Type the following command to close the application:

```text
exit
```

### Important Notes

- An OpenAI API key is required to generate AI responses.
- The application requires an internet connection.
- Web search results may be incomplete or outdated.
- Market prices and business recommendations should be verified before making real business decisions.
- The API key is not included in the repository for security reasons.

## Testing and Evaluation

The system was evaluated using nine test scenarios
covering restaurant expansion in Dubai and Abu Dhabi.

### Test Results

| Test | Topic | Result |
|---|---|---|
| 1 | Location Analysis | Partial Pass |
| 2 | Competitor Analysis | Partial Pass |
| 3 | Menu Strategy | Partial Pass |
| 4 | Pricing Strategy (Retest) | Pass |
| 5 | Marketing Strategy | Pass |
| 6 | Operations and Staffing | Pass |
| 7 | Delivery Strategy | Partial Pass |
| 8 | Licensing Requirements | Partial Pass |
| 9 | Supplier Strategy | Partial Pass |

### Results Summary

- Pass: 3 tests
- Partial Pass: 6 tests
- Fail: 0 tests

### Key Findings

The advisor generated structured recommendations
across different restaurant expansion topics.

Pricing, marketing, and staffing tests produced
useful answers within their tested scope.

The pricing retest successfully provided estimated
prices with clear reasoning and uncertainty statements.

However, several limitations were identified:

- Web searches occasionally failed.
- Some responses lacked verified sources.
- Certain recommendations were too general.
- Some market information required further validation.
- Licensing information was not always up to date.

These results demonstrate the system's capabilities
while highlighting areas for future improvement.

### Detailed Results

Full test questions, results, evaluations, and
suggested improvements are available in [TESTING.md](TESTING.md).

## Design Decisions

### Multi-Agent Architecture

The system uses three specialized agents instead of
a single general-purpose agent.

Each agent focuses on a specific advisory area,
making the system easier to organize, maintain,
and evaluate.

Agno Team coordinates the agents and delegates
tasks based on the user's question.

### Command-Line Interface

A CLI was selected because it is simple to implement,
easy to test, and sufficient for the assignment requirements.

### Model Selection

GPT-4o-mini was selected to balance response quality,
speed, and API cost.

### Web Search

DuckDuckGoTools was selected to provide web search
capabilities without requiring a separate paid
search API key.

Search results are not always reliable or current,
so the agents are instructed to identify uncertain
information and avoid unsupported claims.


## API Cost Management

The following decisions were made to help control
API usage and costs:

- Use GPT-4o-mini instead of a more expensive model.
- Process questions only when submitted by the user.
- Avoid automatic background API requests.
- Use specialized agents for task delegation.
- Avoid unnecessary repeated testing.

The application does not currently implement
automatic token limits, response caching, or
a programmatic spending cap.

Future improvements could include:

- Tracking token usage and estimated API costs.
- Caching repeated research requests.
- Setting limits on agent execution and tool calls.
- Adding configurable response length limits.

## AI Tool Usage Disclosure

### AI Tools Used

ChatGPT (OpenAI) was used as a development assistant
during the implementation of this project.

It assisted with:
- Understanding the Agno framework and multi-agent concepts.
- Planning the agent architecture and responsibilities.
- Reviewing Python code and troubleshooting errors.
- Refining agent instructions.
- Designing test scenarios and evaluating responses.
- Organizing project documentation.

### Personal Implementation

I worked on the project using Python and VS Code.

My implementation work included:
- Creating and configuring three specialized agents.
- Connecting the agents through an Agno Team.
- Integrating DuckDuckGo web search tools.
- Building and testing the command-line interface.
- Running evaluation questions and reviewing the results.
- Improving agent instructions based on testing.
- Managing project files and GitHub version control.

### Understanding and Validation

I reviewed the implementation and tested the
main system components.

I understand the roles of the agents, how task
delegation works, how web search tools are used,
and how the application generates its responses.

AI-generated suggestions were reviewed and adjusted
during development.

## Limitations and Future Improvements

### Current Limitations

- Web search results may be outdated or incomplete.
- DuckDuckGo searches may occasionally fail.
- Some market prices and rental costs cannot be verified.
- The system may sometimes describe information as verified
  without sufficient supporting evidence.
- AI-generated recommendations require human review.

### Future Improvements

- Improve verification of web sources and publication dates.
- Add automatic validation of citations and source links.
- Improve error handling for unsuccessful web searches.
- Add token usage monitoring to better control API costs.
- Introduce response caching for repeated questions.
- Improve recommendation accuracy using verified UAE market data.

## Demo Video

A short demonstration of the Intelligent Market Expansion Advisor,
showing the system running, answering business questions,
and providing information from official sources.

[Watch Demo Video](https://drive.google.com/file/d/1_FUZE0XeQPaPGT_zvWdmeu_rBeZMeld3/view?usp=sharing)