from .base_agent import BaseAgent

class CompetitorAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Competitor Analysis Agent")
        
    async def execute(self, idea: str) -> str:
        prompt = f"""
        You are an expert Competitive Intelligence Analyst.
        Your task is to identify and analyze potential competitors for the following startup idea:
        
        IDEA: "{idea}"
        
        Please provide:
        1. 2-3 direct competitors (real or hypothetical equivalents).
        2. Their strengths and weaknesses.
        3. How this startup can differentiate itself (Unique Value Proposition).
        
        Keep it concise, professional, and structured.
        """
        return await self._call_llm(prompt)
