from dataclasses import dataclass


@dataclass
class LLMResponse:
    """
    Represents the response returned by an LLM.
    """

    content: str
    response_time: float
    model: str
    