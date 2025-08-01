NOTE:- keep human in loop 1] first go through each task separatly and prepare a todos and varify it with human in loop if agree with todos complete the task and if any test is mentioned complete the test and ask human in loop weather work done is correct or not and if yes continue else iterate things by taking feed back agin create new todos repeat until user agrees, this rules apply for evry task

## Project Structure

## Overview
Python-based transcript analysis tool using Google Gemini AI for processing and analyzing transcript files.

## Directory Structure
```
claude-3/
├── AI_DOCS/                              # AI integration documentation
│   └── gemini_structured_output_example_code.md  # Gemini API usage examples
├── src/                                  # Source code directory
│   ├── __init__.py                       # Package initialization
│   ├── argparse.py                       # Command-line argument parsing
│   ├── constants.py                      # Project constants and configuration
│   ├── data_types.py                     # Data models and type definitions
│   ├── gemini_llm.py                     # Gemini AI  integration module
│   └── main.py                           # Application entry point
├── transcript.txt                        # Sample transcript file
├── transcript2.txt                       # Additional transcript file
├── pyproject.toml                        # Project configuration and dependencies
├── uv.lock                               # Dependency lock file
└── README.md                             # Project documentation

## Key Components

### Core Modules
- **main.py**: Entry point, orchestrates transcript processing
- **gemini_llm.py**: Handles Google Gemini AI API key:- "AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0" and model "gemini-2.0-flash" interactions
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

task 1 :- go through folder structure understand it this is the basic repo which we are working with first create this complete basic repo inside "C:\Users\vijay\OneDrive\Desktop\practice-claude-code\ai-coding-course-claude\lessons\lesson-03-perfect-prompt\src" and after this go to claude-3 and run "uv sync" and "uv run main" make sure its working without error. goal of task 1:- when i do "uv run main transcript.txt" in the terminal only it has to display all the word count and transcript anlysis and bullet points and key words 

Task 2: Add Output Format & File Saving Feature
1.1 Create output_format.py:
Implement formatters:

python
Copy
Edit
def format_as_string(transcript: TranscriptAnalysis) -> str
def format_as_json(transcript: TranscriptAnalysis) -> str
def format_as_markdown(transcript: TranscriptAnalysis) -> str
def format_as_yaml(transcript: TranscriptAnalysis) -> str
1.2 Update CLI in arg_parse.py:

Add --output-format argument: options are text, json, markdown, yaml (default: text)

1.3 Update main.py:

Use the selected format to save the analysis result into a .txt, .json, .md, or .yml file.
test it with command uv run main.py transcript.txt
uv run main.py transcript.txt --output-format markdown
uv run main.py transcript.txt --output-format json
uv run main.py transcript.txt --output-format yaml

Task 2: Word Count Visualizations
Use the saved file or processed word count data to visualize word frequency.

2.1 Create chart.py
Implement:make use of matplot lib and all 3 visuals must open in 3 different tabs

python
Copy
Edit
def word_count_bar_chart(word_count_dict: dict, threshold_word_count: int) -> None
def word_count_pie_chart(word_count_dict: dict, threshold_word_count: int) -> None
def word_count_line_graph(word_count_dict: dict, threshold_word_count: int) -> None
Each function should:

Filter words based on threshold_word_count.

Sort (bar and line charts: descending by count).

Render the respective chart using matplotlib.

2.2 Update main.py:
After transcript analysis and file output:

Generate all 3 visualizations:
✅ word_count_bar_chart()
✅ word_count_pie_chart()
✅ word_count_line_graph()

Ensure these occur after transcript formatting/output is saved.

Task 4: Defaults and Ordering
Set minimum_threshold default to 10 in arg_parse.py.

Move all chart rendering after the transcript summary and file saving step.

Final Test Commands
Ensure the following commands:

bash
Copy
Edit
uv run main.py transcript.txt
uv run main.py transcript.txt --output-format markdown
uv run main.py transcript.txt --output-format json
uv run main.py transcript.txt --output-format yaml
Produce:

The correct output file.

Word count bar chart, pie chart, and line graph visualization.