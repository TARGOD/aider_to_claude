# CLI Transcript Analyzer - Hierarchical Development Specification

# ROLE :- Senior Python Developer

## 🎯 HIGH-LEVEL TASK

**Primary Goal**: Build a CLI application that ingests transcript files, uses an AI model (Gemini) to extract structured insights (e.g., themes, bullet points, keywords, summaries, sentiment analysis), and outputs results in .md, .json, .yaml, .txt formats. All generated visualizations (e.g., word frequency charts) should be saved as .png files. All output formats are automatically saved to files.


## 🎯 MID-LEVEL TASK
### 0. **Basic Repo Build**
Follow the project structure in the context and build a basic repo through which you are working further. Ask user to confirm basic repo build is fine. If yes, continue with low level tasks.

### 1. **Text Processing Engine**
Transform raw transcript text into structured word frequency data with AI-powered insights.

### 2. **AI Analysis Integration** 
Leverage Gemini model "gemini-2.0-flash" with API key: "AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0" to generate executive summaries, sentiment analysis, and key highlights.

### 3. **Visualization Generation**
Create professional charts (horizontal bar chart with color coding, pie chart) saved as PNG files in an output directory.

### 4. **Multi-Format Output System**
Support text, JSON, markdown, and YAML output formats with consistent structure. All formats automatically save to files: analysis.txt, analysis.json, analysis.md, analysis.yaml.

### 5. **CLI Interface**
User-friendly command-line interface with proper argument parsing and error handling. Example: "uv run main transcript.txt --output-format markdown"

## 🎯 LOW-LEVEL TASK
✅ [Step 1] main.py: CLI Entry - Display Word Count
Goal: Implement initial CLI entry point to display word frequency of a transcript.go through basic repo structure in context

Command: uv run main transcript.txt

Output: Print {word: count} dictionary to terminal.

✅ [Step 2] argparse_module.py: Argument Parser
Goal: Create a parse_arguments() function using argparse.

Required: transcript_file (positional)

Optional: 
- --min_count (int, default = 3)
- --output-format (choices: json, yaml, markdown, text, default: text)
- --output-file (str, optional - but auto-generated for markdown/json)
- --no-charts (flag to skip chart generation)

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
- summary: str
- bullet_points: List[str]
- keywords: List[str]
- sentiment: str
- word_count: Dict[str, int]
- total_words: int
- unique_words: int

Add module docstring: "Data models and type definitions."

✅ [Step 5] gemini_llm.py: Gemini API Integration
Goal: Create class GeminiAnalyzer to process transcript text.

Method: analyze_transcript(text: str, min_count: int = 3) -> TranscriptAnalysis

Responsibilities:
- Perform word frequency count (respecting stopwords and min_count)
- Call Gemini API using constants
- Parse response: summary, bullet_points, keywords, sentiment
- Return populated TranscriptAnalysis object

✅ [Step 6] chart.py: Visualization Module
Goal: Generate word frequency bar and pie charts using matplotlib.

Functions:
- generate_bar_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str (returns image path)
- generate_pie_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str

Features:
- Sort and color-code bars by frequency tiers
- Save .png files in output folder with timestamp
- Return file paths
- Create output directory if it doesn't exist

✅ [Step 7] output_format.py: Formatter
Goal: Support multi-format output (text, json, yaml, markdown).

Functions:
- format_as_json(analysis: TranscriptAnalysis) -> str
- format_as_markdown(analysis: TranscriptAnalysis, bar_chart_path: Optional[str] = None, pie_chart_path: Optional[str] = None) -> str
- format_as_yaml(analysis: TranscriptAnalysis) -> str
- format_as_text(analysis: TranscriptAnalysis) -> str

Features:
- Include sentiment analysis in all formats
- Embed chart image paths in markdown output
- Format word frequency tables appropriately for each format 

## 📋 CONTEXT

### **Repo Structure**
```
claude-5/
├── AI_DOCS/
│   └── gemini_structured_output_example_code.md
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── argparse_module.py   # Argument parser
│   ├── constants.py         # Configuration constants
│   ├── datatypes.py         # Data models
│   ├── gemini_llm.py        # Gemini API integration
│   ├── chart.py             # Visualization module
│   └── output_format.py     # Output formatters
├── output/                  # Generated charts directory
├── pyproject.toml
├── README.md
├── transcript.txt           # Sample data
├── transcript2.txt          # Additional sample
└── uv.lock
```

### **Important Implementation Notes**
1. All output formats are automatically saved to files:
   - `--output-format text` → `analysis.txt`
   - `--output-format json` → `analysis.json`
   - `--output-format markdown` → `analysis.md`
   - `--output-format yaml` → `analysis.yaml`
2. Custom output filenames can be specified with `--output-file` and even same json cammand run two times it has to save agin another json with different name dont overwrite or replace privious  saved file 
3. PNG charts are always generated (unless --no-charts is used) and saved in the `output/` directory
4. The pyproject.toml must include `[tool.hatch.build.targets.wheel]` with `packages = ["src"]` for uv to work properly


