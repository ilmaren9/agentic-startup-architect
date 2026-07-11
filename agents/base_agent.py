import os
import google.generativeai as genai
from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

class BaseAgent(ABC):
    """
    Abstract base class for all specialist agents.
    """
    def __init__(self, name: str, model_name: str = "gemini-3.5-flash"):
        self.name = name
        self.model_name = model_name
        self.model = genai.GenerativeModel(self.model_name)
    
    @abstractmethod
    async def execute(self, idea: str) -> str:
        """
        Executes the agent's specific task based on the startup idea.
        Must be implemented by subclasses.
        """
        pass
    
    async def _call_llm(self, prompt: str) -> str:
        """
        Helper method to call the Gemini API.
        Since the google-generativeai package currently has limited native async support 
        for generate_content in some environments, we might use the sync version or run it in a thread.
        However, for this demonstration, we'll try to use generate_content_async if available, 
        or fallback to wrapping the sync call.
        """
        try:
            # We use generate_content_async for parallel execution
            response = await self.model.generate_content_async(prompt)
            return response.text
        except AttributeError:
            # Fallback if generate_content_async is not available in the specific sdk version
            import asyncio
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, self.model.generate_content, prompt)
            return response.text
        except Exception as e:
            return f"Error in {self.name}: {str(e)}"
