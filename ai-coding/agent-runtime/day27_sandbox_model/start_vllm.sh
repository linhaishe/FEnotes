#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
: "${VLLM_MODEL:=Qwen/Qwen2.5-1.5B-Instruct}"
: "${VLLM_API_KEY:=day27-local-token}"
: "${DAY27_MODEL_TOKEN:=$VLLM_API_KEY}"
: "${DAY27_MODEL_NAME:=$VLLM_MODEL}"
: "${DAY27_MODEL_URL:=http://127.0.0.1:8000/v1}"
: "${DAY27_MODEL_HOST:=127.0.0.1}"
export VLLM_MODEL VLLM_API_KEY DAY27_MODEL_TOKEN DAY27_MODEL_NAME DAY27_MODEL_URL DAY27_MODEL_HOST

docker compose -f docker-compose.vllm.yml up -d
python check_vllm.py
