# Agentic Startup Architect

A multi-agent startup validation system built for the Agentic Architect Sprint.

This project demonstrates a hub-and-spoke multi-agent architecture using the Gemini API. An **Orchestrator Agent** takes a startup idea and runs several specialist agents in parallel to analyze it. Their isolated findings are then passed to a **Synthesis Agent** that generates a comprehensive, final Markdown report.

## Architecture

1. **Orchestrator Agent (The Hub):** Manages the workflow and parallel execution.
2. **Specialized Subagents (The Spokes):** Each runs independently with strict context isolation.
   - **Market Research Agent:** Evaluates market size and trends.
   - **Competitor Analysis Agent:** Identifies competitors and UVP.
   - **Customer Persona Agent:** Details the target audience and pain points.
   - **Business Model Agent:** Proposes revenue streams and cost structures.
3. **Synthesis Agent:** Combines all findings into a final Startup Validation Report.

## Folder Structure

```text
agentic-startup-architect/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py          # Abstract base class with Gemini integration
│   ├── orchestrator.py        # Manages parallel execution
│   ├── market_research.py     # Specialist Agent
│   ├── competitor_analysis.py # Specialist Agent
│   ├── customer_persona.py    # Specialist Agent
│   ├── business_model.py      # Specialist Agent
│   └── synthesis.py           # Synthesizes the final report
├── utils/
│   ├── __init__.py
│   └── report_writer.py       # Saves output to a markdown file
├── main.py                    # Application entry point
├── requirements.txt           # Dependencies
└── .env.example               # Example environment variables
```

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key:**
   Copy the example environment file and add your Google Gemini API key.
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set `GEMINI_API_KEY=your_actual_api_key`.

## Running the Example Workflow

Run the main application script:

```bash
python main.py
```

You will be prompted to enter a startup idea (or press Enter to use the default).
The orchestrator will spin up the specialized agents in parallel.
Once all data is collected, the Synthesis Agent will generate a comprehensive report saved in the `output/` directory.