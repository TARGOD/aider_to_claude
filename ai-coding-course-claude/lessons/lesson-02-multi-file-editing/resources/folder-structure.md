# lesson-02-multi-file-editing

## Structure

```
lesson-02-multi-file-editing/
├── prompts/
│   └── prompt-history.md          # History of prompts used
├── resources/                     # Resource files
├── src/
│   └── paicc-2/                  # Main project
│       ├── AI_DOCS/
│       │   └── openai_structured_output_example_code.md
│       ├── src/
│       │   └── transcript_analytics/
│       │       ├── __init__.py
│       │       ├── arg_parse.py     # CLI argument parsing
│       │       ├── constants.py     # Project constants
│       │       ├── data_types.py    # Data type definitions
│       │       ├── gemini_llm.py    # Gemini AI integration
│       │       └── main.py          # Entry point
│       ├── transcript.txt           # Sample transcript
│       ├── transcript2.txt          # Additional transcript
│       ├── pyproject.toml           # Python package config
│       ├── uv.lock                  # Dependency lock file
│       └── README.md                # Project documentation
└── summary.md                       # Lesson summary

## Core Components

- **transcript_analytics**: Python package for transcript analysis
- **AI Integration**: Gemini LLM for processing
- **CLI**: Command-line interface via arg_parse
- **Data Models**: Structured types in data_types.py