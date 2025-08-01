# Transcript Analyzer

A Python-based transcript analysis tool using Google Gemini AI for processing and analyzing transcript files.

## Features

- Analyze transcript files using Google Gemini AI
- Generate summaries, bullet points, and keywords
- Calculate word frequency statistics
- Support for multiple output formats (text, json, markdown, yaml)

## Installation

```bash
# Install dependencies using uv
uv sync
```

## Usage

```bash
# Analyze a transcript file
uv run main transcript.txt

# Specify output format
uv run main transcript.txt --output-format markdown
```

## Project Structure

```
claude-4/
├── AI_DOCS/                              # AI integration documentation
│   └── gemini_structured_output_example_code.md  # Gemini API usage examples
├── src/                                  # Source code directory
│   ├── __init__.py                       # Package initialization
│   ├── argparse.py                       # Command-line argument parsing
│   ├── constants.py                      # Project constants and configuration
│   ├── data_types.py                     # Data models and type definitions
│   ├── gemini_llm.py                     # Gemini AI integration module
│   └── main.py                           # Application entry point
├── transcript.txt                        # Sample transcript file
├── transcript2.txt                       # Additional transcript file
├── pyproject.toml                        # Project configuration and dependencies
└── README.md                             # Project documentation
```

## Requirements

- Python 3.11+
- Google Gemini API key
- Required packages: google-generativeai, pydantic, python-dotenv