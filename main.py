import asyncio
import os
import sys
from dotenv import load_dotenv
from rich.console import Console

from agents.orchestrator import OrchestratorAgent
from utils.report_writer import save_report

# Load environment variables
load_dotenv()

console = Console()

async def main():
    # Check for API key
    if not os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY") == "your_gemini_api_key_here":
        console.print("[bold red]Error: GEMINI_API_KEY is not set.[/bold red]")
        console.print("Please create a .env file with your GEMINI_API_KEY.")
        sys.exit(1)
        
    console.print("[bold blue]Welcome to the Agentic Startup Architect![/bold blue]")
    
    # Prompt user for idea or use a default one
    default_idea = "A subscription box for high-quality, sustainably sourced specialty coffee, curated by AI based on user taste profiles."
    print(f"\nEnter your startup idea (or press Enter to use the default):\nDefault: {default_idea}")
    user_idea = input("> ").strip()
    
    idea = user_idea if user_idea else default_idea
    
    # Initialize and run orchestrator
    orchestrator = OrchestratorAgent()
    
    try:
        report = await orchestrator.run_validation(idea)
        
        # Save the report
        filename = save_report(report)
        console.print(f"\n[bold green]Success![/bold green] Report saved to: [cyan]{filename}[/cyan]")
        
    except Exception as e:
        console.print(f"\n[bold red]An error occurred during execution:[/bold red] {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
