# PAICC-2 Repository Structure

## Overview
This repository contains a simple transcript analytics tool built with Python. It processes text transcripts and performs word frequency analysis using the OpenAI API for potential structured output capabilities.

## Folder Structure

```
paicc-2/
├── AI_DOCS/                        # Documentation for AI integration
│   └── openai_structured_output_example_code.md
├── src/                           # Source code directory
│   └── transcript_analytics/      # Main package
│       ├── __init__.py           # Package initialization
│       └── main.py               # Main application entry point
├── README.md                      # Project documentation
├── pyproject.toml                 # Project configuration and dependencies
├── uv.lock                        # Dependency lock file
├── transcript.txt                 # Sample transcript file
└── transcript2.txt                # Additional transcript file
```

## File Descriptions

### Root Files
- **README.md**: Basic setup instructions for the project
- **pyproject.toml**: Python project configuration using modern standards
  - Defines project metadata (name, version, description)
  - Specifies Python 3.11+ requirement
  - Lists dependencies: openai, pydantic, python-dotenv
  - Configures the build system (hatchling)
  - Sets up CLI script entry point

### AI Documentation
- **AI_DOCS/openai_structured_output_example_code.md**: Contains example code demonstrating OpenAI's structured output feature using Pydantic models for type-safe responses

### Source Code
- **src/transcript_analytics/main.py**: Core application logic
  - Loads environment variables (for OpenAI API key)
  - Reads transcript files
  - Performs word frequency analysis
  - Filters words by minimum occurrence threshold (>3)
  - Displays results as a histogram using '#' characters

### Data Files
- **transcript.txt**: Primary transcript file for analysis
- **transcript2.txt**: Secondary transcript file (unused in current implementation)

## Key Features
1. **Word Frequency Analysis**: Counts occurrences of each word in transcripts
2. **Case-Insensitive Processing**: Converts all words to lowercase
3. **Threshold Filtering**: Only displays words appearing more than 3 times
4. **Visual Representation**: Shows frequency using ASCII histogram
5. **OpenAI Integration Ready**: Infrastructure for AI-powered analysis

## Dependencies
- **openai**: For potential AI-powered transcript analysis
- **pydantic**: For data validation and structured outputs
- **python-dotenv**: For environment variable management

## Usage
The project is configured to run via UV package manager:
```bash
uv sync          # Install dependencies
uv run main      # Execute the analysis
```