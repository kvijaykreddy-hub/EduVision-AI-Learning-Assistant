"""
Prompt templates for text summarization.
"""


def build_summary_prompt(
    text: str,
    style: str = "paragraph",
) -> str:
    """
    Build summarization prompt.

    Supported styles:
        - paragraph
        - bullet
    """

    if style.lower() == "bullet":
        return f"""
You are an expert educational AI assistant that creates concise study notes.

Your task is to read the given text and produce high-quality revision notes.

IMPORTANT INSTRUCTIONS:

- Return ONLY bullet points.
- Do NOT write any introduction.
- Do NOT write any conclusion.
- Do NOT write paragraphs.
- Generate between 5 and 10 bullet points.
- Start EVERY bullet with "-".
- Each bullet should contain only one important idea.
- Keep each bullet short (maximum 20 words).
- Remove unnecessary details and examples.
- Focus only on concepts that are useful for studying and exam revision.
- Use simple, clear English.

Example Output:

- Social environment influences human behavior.
- People imitate those around them.
- Group norms shape habits.
- Supportive communities reinforce positive habits.
- Identity-based habits last longer.

Text:

{text}
"""

    return f"""
You are an expert educational AI assistant.

Create a concise study summary of the following text.

Instructions:

- Write exactly one paragraph.
- Keep the summary between 100 and 150 words.
- Focus only on the main ideas.
- Remove unnecessary details and examples.
- Explain the concepts in simple English.
- Do not copy sentences directly from the text.

Text:

{text}
"""