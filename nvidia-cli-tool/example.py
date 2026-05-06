"""
Example usage of the NVIDIA CLI tool
"""

import subprocess
import os

# Example 1: Simple text generation
print("Example 1: Simple text generation")
result = subprocess.run([
    "nvidia-cli", 
    "What is the capital of France?"
], capture_output=True, text=True)
print(result.stdout)

# Example 2: Using environment variable for token
print("\nExample 2: Using environment variable for token")
env = os.environ.copy()
env["NVAPI_TOKEN"] = "your_token_here"  # Replace with actual token
result = subprocess.run([
    "nvidia-cli", 
    "Write a short poem about spring",
    "--temperature", "0.7"
], capture_output=True, text=True, env=env)
print(result.stdout)

# Example 3: Image analysis (commented out as it requires an image file)
print("\nExample 3: Image analysis")
print("nvidia-cli \"Describe this image\" --image /path/to/image.jpg")

# Example 4: Getting help
print("\nExample 4: Getting help")
result = subprocess.run(["nvidia-cli", "--help"], capture_output=True, text=True)
print(result.stdout)