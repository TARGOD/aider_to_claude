# Lesson 03 Perfect Prompt - Project Structure

## Directory Overview
Python project with Gemini AI integration for transcript analysis.

```
src/
└── claude-4/
    ├── AI_DOCS/
    │   └── gemini_structured_output_example_code.md  # Gemini API examples
    ├── src/
    │   ├── __init__.py                               # Package initialization
    │   ├── argparse.py                               # Command line argument parsing
    │   ├── chart.py                                  # Chart generation utilities
    │   ├── constants.py                              # Application constants
    │   ├── data_types.py                             # Data type definitions
    │   ├── gemini_llm.py                             # Gemini LLM integration
    │   ├── main.py                                   # Main application entry point
    │   └── output_format.py                          # Output formatting utilities
    ├── pyproject.toml                                # Python project configuration
    ├── README.md                                     # Project documentation
    ├── transcript.txt                                # Sample transcript data
    ├── transcript2.txt                               # Additional transcript data
    ├── transcript_analysis.json                      # JSON analysis output
    ├── transcript_analysis.md                        # Markdown analysis output
    ├── transcript_analysis.txt                       # Text analysis output
    ├── transcript_analysis.yml                       # YAML analysis output
    └── uv.lock                                       # UV package manager lockfile
```

## Key Components
- **Core Module**: Python package in `src/` with modular architecture
- **AI Integration**: Gemini LLM for structured output generation
- **Multiple Formats**: Supports JSON, Markdown, YAML, and text outputs
- **Configuration**: Modern Python tooling with pyproject.toml and uv