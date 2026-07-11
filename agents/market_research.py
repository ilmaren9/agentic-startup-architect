from .base_agent import BaseAgent

class MarketResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Market Research Agent")
        
    async def execute(self, idea: str) -> str:
        prompt = f"""
        You are an expert Market Research Analyst.
        Your task is to analyze the market potential for the following startup idea:
        
        IDEA: "{idea}"
        
        Please provide:
        1. Market Size (TAM, SAM, SOM) estimates.
        2. Key market trends driving this sector.
        3. Potential barriers to entry.
        
        Keep it concise, professional, and structured.
        """
        return await self._call_llm(prompt)
