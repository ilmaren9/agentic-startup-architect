from .base_agent import BaseAgent
import json

class SynthesisAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Synthesis Agent")
        
    async def execute(self, idea: str, agent_results: dict) -> str:
        # Convert results to a formatted string for the prompt
        results_str = "\n\n".join([f"--- {name} ---\n{result}" for name, result in agent_results.items()])
        
        prompt = f"""
        You are the Lead Startup Architect.
        Your task is to synthesize the findings from various specialist agents to produce a final Startup Validation Report.
        
        ORIGINAL IDEA: "{idea}"
        
        AGENT FINDINGS:
        {results_str}
        
        Please generate a comprehensive, well-structured Markdown report that includes:
        1. Executive Summary
        2. Market Opportunity
        3. Competitive Landscape
        4. Target Audience
        5. Business Model & Viability
        6. Final Recommendation (Go / No-Go with reasoning)
        
        Format the output entirely in Markdown.
        """
        return await self._call_llm(prompt)
