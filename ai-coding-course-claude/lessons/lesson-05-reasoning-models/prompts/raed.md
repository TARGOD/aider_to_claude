# CLI Transcript Analyzer - Hierarchical Development Specification

# ROLE :- Senior Python Developer

## 🎯 HIGH-LEVEL TASK

**Primary Goal**: Goal: Build a CLI application that ingests transcript files, uses an AI model (Gemini) to extract structured insights (e.g., themes, bullet points ,keywords, summaries,sentiment analysis ), and outputs results in .md, .json, .yaml. All generated visualizations (e.g., word_count frequency) should be saved as .png and all this should display in terminal.


## 🎯 MID-LEVEL TASK
### 0. **Bsic Repo Build**
Follow the project structure in the context and build a basic repo through which you are working further "note:- ask for user to confirm basic repo build is fine is yes continue with low level task" 

### 1. **Text Processing Engine**
Transform raw transcript text into structured word frequency data with AI-powered insights.

### 2. **AI Analysis Integration** 
Leverage Gemini model "gemini-2.0-flash" with API key :-"AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0"to generate executive summaries, sentiment analysis, and key highlights.

### 3. **Visualization Generation**
Create professional charts (horizontal bar chart with color coding, pie chart) displyed in different windows and  saved as PNG files.

### 4. **Multi-Format Output System**
Support text, JSON, markdown, and YAML output formats with consistent structure.

### 5. **CLI Interface**
User-friendly command-line interface with proper argument parsing and error handling.for example "uv run main transcript.txt --output format markdown"

## 🎯 LOW-LEVEL TASK
✅ [Step 1] main.py: CLI Entry - Display Word Count
Goal: Implement initial CLI entry point to display word frequency of a transcript.go through basic repo structure in context

Command: uv run main transcript.txt

Output: Print {word: count} dictionary to terminal.

✅ [Step 2] argparse.py: Argument Parser
Goal: Create a parse_arguments() function using argparse.

Required: transcript_file (positional)

Optional: --min_count (int, default = 3)

Returns: Namespace object used in main.py

✅ [Step 3] constants.py: Configuration Constants
Goal: Define all reusable constants.

API Key, Gemini model name

Supported formats: ["json", "yaml", "markdown", "text"]

DEFAULT_MIN_COUNT

STOPWORDS list: e.g., ["the", "and", "of"]

PUNCTUATION_BLACKLIST: e.g., [".", "!", ",", "?"]

✅ [Step 4] datatypes.py: Data Model
Goal: Create a TranscriptAnalysis model using pydantic.BaseModel.

Fields:

summary: str

bullet_points: List[str]

keywords: List[str]

word_count: Dict[str, int]

total_words: int

unique_words: int

Add module docstring: "Data models and type definitions."

✅ [Step 5] gemini_llm.py: Gemini API Integration
Goal: Create class GeminiAnalyzer to process transcript text.

Method: analyze_transcript(text: str) -> TranscriptAnalysis

Responsibilities:

Perform word frequency count (respecting stopwords and min_count)

Call Gemini API using constants

Parse response: summary, bullet_points, keywords

Return populated TranscriptAnalysis object

✅ [Step 6] chart.py: Visualization Module
Goal: Generate word frequency bar and pie charts using matplotlib.

Functions:

generate_bar_chart(freq_dict) -> str (returns image path)

generate_pie_chart(freq_dict) -> str

Features:

Sort and color-code bars by frequency tiers

Save .png files in output folder

Return file paths

✅ [Step 7] output_format.py: Formatter
Goal: Support multi-format output (text, json, yaml, markdown).

Functions:

format_as_json(TranscriptAnalysis) -> str

format_as_markdown(TranscriptAnalysis) -> str

format_as_yaml(TranscriptAnalysis) -> str

format_as_text(TranscriptAnalysis) -> str


Optionally embed chart image paths in markdown output 

## 📋 CONTEXT

### **Basic Repo Structure**
```
claude-5/
├── AI_DOCS/
│   └── gemini_structured_output_example_code.md
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
├── pyproject.toml
├── README.md
├── transcript.txt           # Sample data
├── transcript2.txt          # Additional sample
└── uv.lock
```


