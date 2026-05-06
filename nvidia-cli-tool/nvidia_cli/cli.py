import requests
import base64
import argparse
import sys
import os
from pathlib import Path

def read_b64(path):
    """Read a file and return its base64-encoded content."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {path}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Interact with NVIDIA API from the command line.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "What is the capital of France?"
  %(prog)s "Describe this image" --image /path/to/image.jpg
  %(prog)s "Write a poem" --model moonshotai/kimi-k2.6 --temperature 0.7
  NVAPI_TOKEN=your_token_here %(prog)s "Hello"  # Using environment variable
        """
    )
    
    parser.add_argument('prompt', nargs='?', help='The prompt to send to the NVIDIA API')
    parser.add_argument('--image', '-i', type=Path, help='Path to an image file to include in the request')
    parser.add_argument('--token', '-t', help='API token (if not provided, will look for environment variable NVAPI_TOKEN)')
    parser.add_argument('--model', '-m', default='moonshotai/kimi-k2.6', 
                       help='Model to use (default: moonshotai/kimi-k2.6)')
    parser.add_argument('--max-tokens', '-M', type=int, default=16384, 
                       help='Maximum number of tokens (default: 16384)')
    parser.add_argument('--temperature', '-T', type=float, default=1.00, 
                       help='Temperature for sampling (default: 1.00)')
    parser.add_argument('--top-p', '-P', type=float, default=1.00, 
                       help='Top-p for sampling (default: 1.00)')
    parser.add_argument('--no-thinking', action='store_true', 
                       help='Disable thinking mode')
    
    args = parser.parse_args()
    
    # Get API token from argument or environment variable
    token = args.token or os.getenv('NVAPI_TOKEN')
    if not token:
        print("Error: API token must be provided with -t or set as NVAPI_TOKEN environment variable", file=sys.stderr)
        print("You can set it with: export NVAPI_TOKEN=your_token_here", file=sys.stderr)
        sys.exit(1)
    
    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
    stream = True
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "text/event-stream" if stream else "application/json"
    }
    
    # Prepare content based on whether we have a prompt and/or image
    content = []
    
    if args.prompt:
        content.append({
            "type": "text",
            "text": args.prompt
        })
    
    if args.image:
        if not args.prompt:
            print("Error: A prompt is required when providing an image", file=sys.stderr)
            sys.exit(1)
        
        # Check if image file exists
        if not args.image.exists():
            print(f"Error: Image file does not exist: {args.image}", file=sys.stderr)
            sys.exit(1)
        
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image;base64,{read_b64(args.image)}"
            }
        })
    
    # Ensure we have some content
    if not content:
        print("Error: Either a prompt or an image must be provided", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": content}],
        "max_tokens": args.max_tokens,
        "temperature": args.temperature,
        "top_p": args.top_p,
        "stream": stream,
        "chat_template_kwargs": {"thinking": not args.no_thinking},
    }
    
    try:
        response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)
        response.raise_for_status()
        
        if stream:
            for line in response.iter_lines():
                if line:
                    print(line.decode("utf-8"))
        else:
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nRequest interrupted by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()