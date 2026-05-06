"""
Configuration for NVIDIA API CLI Tool
"""

# Default configuration values
DEFAULT_MODEL = "moonshotai/kimi-k2.6"
DEFAULT_MAX_TOKENS = 16384
DEFAULT_TEMPERATURE = 1.00
DEFAULT_TOP_P = 1.00
DEFAULT_INVOKE_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

# Environment variable name for API token
API_TOKEN_ENV_VAR = "NVAPI_TOKEN"