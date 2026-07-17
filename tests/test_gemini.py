import time
from eduvision_ai.services.llm_service import LLMService

print("Creating LLM Service...")
t1 = time.perf_counter()

service = LLMService()

t2 = time.perf_counter()

print(f"Initialization Time: {t2 - t1:.2f} seconds")

print("Sending request...")
t3 = time.perf_counter()

response = service.ask(
    "Explain Artificial Intelligence in exactly three short sentences."
)

t4 = time.perf_counter()

print(f"API Response Time: {t4 - t3:.2f} seconds")

print("\nGemini Response:\n")
print(response)