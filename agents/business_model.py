from .base_agent import BaseAgent

class BusinessModelAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Business Model Agent")
        
    async def execute(self, idea: str) -> str:
        prompt = f"""
        You are an expert Business Strategist.
        Your task is to design a viable business model for the following startup idea:
        
        IDEA: "{idea}"
        
        Please provide:
        1. Proposed Revenue Streams (e.g., subscription, one-off, freemium).
        2. Key Cost Structure elements (e.g., development, marketing, operations).
        3. A brief verdict on the financial viability of the idea.
        
        Keep it concise, professional, and structured.
        """
        return await self._call_llm(prompt)
