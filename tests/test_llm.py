from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from eduvision_ai.services.llm_service import LLMService

service = LLMService()

response = service.ask(
    "Explain Artificial Intelligence in three simple sentences."
)

print(response)