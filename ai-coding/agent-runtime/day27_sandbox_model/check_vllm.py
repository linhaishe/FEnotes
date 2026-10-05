"""Verify vLLM health and its OpenAI-compatible models endpoint."""

import os

import httpx


def main() -> None:
    base_url = os.getenv("DAY27_MODEL_URL", "http://127.0.0.1:8000/v1").rstrip("/")
    token = os.getenv("DAY27_MODEL_TOKEN", "day27-local-token")
    headers = {"Authorization": f"Bearer {token}"}
    with httpx.Client(timeout=5.0, trust_env=False) as client:
        health = client.get(base_url.removesuffix("/v1") + "/health")
        health.raise_for_status()
        models = client.get(base_url + "/models", headers=headers)
        models.raise_for_status()
        data = models.json()
    names = [item["id"] for item in data.get("data", [])]
    if not names:
        raise RuntimeError("vLLM returned no served models")
    print({"health": health.status_code, "models": names})


if __name__ == "__main__":
    main()
