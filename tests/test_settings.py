from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from eduvision_ai.config.settings import Settings

print("Provider:", Settings.MODEL_PROVIDER)

print("Gemini Key Loaded:", bool(Settings.GOOGLE_API_KEY))

if Settings.GOOGLE_API_KEY:
    print("Gemini Preview:", Settings.GOOGLE_API_KEY[:8] + "...")

print("HF Token Loaded:", bool(Settings.HUGGINGFACEHUB_API_TOKEN))