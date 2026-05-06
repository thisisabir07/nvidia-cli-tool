from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nvidia-cli-tool",
    version="0.1.0",
    author="Abir Chakraborty",
    author_email="abirsc7@gmail.com",
    description="A command-line interface for interacting with the NVIDIA API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thisisabir07/nvidia-cli-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "nvidia-cli=nvidia_cli.cli:main",
        ],
    },
)