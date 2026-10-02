"""Minimal usage example for :mod:`demo_dependencies`."""

from .demo_dependencies import compress_context, trim_context


def main() -> None:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is context caching?"},
        {"role": "assistant", "content": "It reuses repeated results."},
        {"role": "user", "content": "Show me a small example."},
    ]

    trimmed = trim_context(messages, max_chars=80)
    compressed = compress_context(trimmed, keep_last=2)

    print("trimmed:", trimmed)
    print("compressed:", compressed)


if __name__ == "__main__":
    main()
