"""Minimal LangChain Agent example based on the official custom-tool pattern."""

import os

from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def main() -> None:
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("请先设置 GEMINI_API_KEY")

    agent = create_agent(
        model="google_genai:gemini-2.5-flash-lite",
        tools=[get_weather],
        system_prompt="You are a helpful assistant. Use tools when they are useful.",
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in Beijing?"}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
