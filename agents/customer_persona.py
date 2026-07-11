from .base_agent import BaseAgent

class CustomerPersonaAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Customer Persona Agent")
        
    async def execute(self, idea: str) -> str:
        prompt = f"""
        You are an expert User Researcher.
        Your task is to define the target audience for the following startup idea:
        
        IDEA: "{idea}"
        
        Please provide:
        1. A primary Customer Persona (Name, Age, Occupation).
        2. Their main pain points and goals.
        3. Where this customer can be reached (acquisition channels).
        
        Keep it concise, professional, and structured.
        """
        return await self._call_llm(prompt)
