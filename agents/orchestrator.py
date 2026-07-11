import asyncio
from rich.console import Console
from rich.panel import Panel

from .market_research import MarketResearchAgent
from .competitor_analysis import CompetitorAnalysisAgent
from .customer_persona import CustomerPersonaAgent
from .business_model import BusinessModelAgent
from .synthesis import SynthesisAgent

console = Console()

class OrchestratorAgent:
    def __init__(self):
        self.market_agent = MarketResearchAgent()
        self.competitor_agent = CompetitorAnalysisAgent()
        self.persona_agent = CustomerPersonaAgent()
        self.business_agent = BusinessModelAgent()
        self.synthesis_agent = SynthesisAgent()
        
    async def run_validation(self, idea: str) -> str:
        console.print(Panel(f"[bold cyan]Starting Validation for Idea:[/bold cyan]\n{idea}", title="Orchestrator"))
        
        console.print("[yellow]Spinning up specialist agents in parallel...[/yellow]")
        
        # Run agents in parallel
        results = await asyncio.gather(
            self._run_agent(self.market_agent, idea),
            self._run_agent(self.competitor_agent, idea),
            self._run_agent(self.persona_agent, idea),
            self._run_agent(self.business_agent, idea)
        )
        
        # Collect results
        agent_results = {
            self.market_agent.name: results[0],
            self.competitor_agent.name: results[1],
            self.persona_agent.name: results[2],
            self.business_agent.name: results[3]
        }
        
        console.print("[green]All specialist agents completed their tasks![/green]")
        console.print("[yellow]Passing data to the Synthesis Agent...[/yellow]")
        
        # Run synthesis
        final_report = await self.synthesis_agent.execute(idea, agent_results)
        
        console.print("[bold green]Validation Report Generated Successfully![/bold green]")
        return final_report
        
    async def _run_agent(self, agent, idea):
        console.print(f"[{agent.name}] Starting analysis...")
        result = await agent.execute(idea)
        console.print(f"[bold green][{agent.name}] Completed![/bold green]")
        return result
