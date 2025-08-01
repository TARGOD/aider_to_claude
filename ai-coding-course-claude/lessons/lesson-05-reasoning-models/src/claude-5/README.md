# CLI Transcript Analyzer

A CLI application that analyzes transcript files using the Gemini AI model to extract structured insights.

## Features
- Word frequency analysis with stopword filtering
- AI-powered analysis:
  - Executive summaries
  - Key bullet points
  - Keyword extraction
  - Sentiment analysis
- Multiple output formats (JSON, YAML, Markdown, Text)
- Visualization generation (bar charts, pie charts saved as PNG)

## Installation
```bash
# Install dependencies
pip install google-generativeai pydantic matplotlib pyyaml

# Or using uv
uv pip install google-generativeai pydantic matplotlib pyyaml
```

## Usage

### Primary Command (with uv)
```bash
uv run main transcript.txt --output-format markdown
```

This command will:
- Analyze the transcript file
- Generate visualizations and save them as PNG files in the `output/` directory
- Save the analysis as `analysis.md` (automatically when using markdown format)

### Alternative Usage (without uv)
```bash
python -m src.main transcript.txt --output-format markdown
```

## Important Notes
- When using `--output-format markdown`, the analysis is **automatically saved** to `analysis.md`
- PNG visualizations are **always generated** unless you use `--no-charts`
- The Gemini API key is already configured in the constants.py file

## Testing
After setup, test the application:
```bash
uv run main transcript.txt --output-format markdown
```

If you encounter any errors, check:
1. The transcript file exists
2. Dependencies are installed
3. You have internet connection for Gemini API

## Output Files
- `analysis.md` - Markdown formatted analysis report
- `output/word_frequency_bar_[timestamp].png` - Bar chart visualization
- `output/word_frequency_pie_[timestamp].png` - Pie chart visualization