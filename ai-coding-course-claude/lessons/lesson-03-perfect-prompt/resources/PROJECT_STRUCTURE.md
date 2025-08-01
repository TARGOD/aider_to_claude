# Claude-2 Transcript Analyzer - Project Structure

## Overview
Python-based transcript analysis tool using Google Gemini AI for processing and analyzing transcript files.

## Directory Structure
```
claude-2/
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
├── uv.lock                               # Dependency lock file
└── README.md                             # Project documentation

## Key Components

### Core Modules
- **main.py**: Entry point, orchestrates transcript processing
- **gemini_llm.py**: Handles Google Gemini AI API interactions
- **data_types.py**: Defines data structures for transcript analysis
- **argparse.py**: Manages command-line interface
- **constants.py**: Stores configuration values and constants

### Configuration Files
- **pyproject.toml**: Python project metadata and dependencies
- **uv.lock**: Locked dependency versions for reproducible builds

### Data Files
- **transcript.txt, transcript2.txt**: Input transcript files for analysis

## Technology Stack
- **Language**: Python 3.11+
- **AI Model**: Google Gemini
- **Key Libraries**: google-generativeai, pydantic, python-dotenv
- **Package Manager**: uv

## Purpose
Analyzes transcript files using AI to extract insights, summaries, or structured data.