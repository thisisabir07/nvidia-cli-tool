# NVIDIA API CLI Tool

A command-line interface for interacting with the NVIDIA API to generate text completions using their models.

## Installation

```bash
# Clone the repository
git clone https://github.com/thisisabir07/nvidia-cli-tool.git
cd nvidia-cli-tool

# Install the package
pip install .
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/thisisabir07/nvidia-cli-tool.git
```

## Usage

First, you'll need to set your NVIDIA API token. You can do this in one of two ways:

1. Set it as an environment variable:
```bash
export NVAPI_TOKEN=your_token_here
```

2. Pass it directly with the `-t` flag:
```bash
nvidia-cli "Your prompt here" -t your_token_here
```

### Basic Usage

```bash
# Simple text generation
nvidia-cli "What is the capital of France?"

# With custom parameters
nvidia-cli "Write a poem about春天" --model moonshotai/kimi-k2.6 --temperature 0.7 --max-tokens 2048
```

### Image Analysis

```bash
# Analyze an image with a prompt
nvidia-cli "Describe this image" --image /path/to/your/image.jpg
```

### Available Options

```bash
nvidia-cli --help
```

## Configuration

- **Default Model**: `moonshotai/kimi-k2.6`
- **Default Max Tokens**: `16384`
- **Default Temperature**: `1.00`
- **Default Top-p**: `1.00`

## Dependencies

- Python 3.7+
- requests

## License

MIT License