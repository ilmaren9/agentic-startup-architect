import os
from datetime import datetime

def save_report(content: str, filename_prefix: str = "startup_report"):
    """
    Saves the markdown report to the output directory.
    """
    # Create an output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/{filename_prefix}_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    return filename
