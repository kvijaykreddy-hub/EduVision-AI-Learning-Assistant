import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

start = time.perf_counter()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain AI in one sentence."
)

end = time.perf_counter()

print(f"Time: {end-start:.2f} seconds")
print(response.text)