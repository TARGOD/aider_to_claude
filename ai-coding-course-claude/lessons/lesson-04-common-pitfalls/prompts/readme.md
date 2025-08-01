NOTE:- keep human in loop . first go through each task separatly and prepare a todos and varify it with human in loop if agree with todos complete the task and if any test is mentioned complete the test and ask human in loop weather work done is correct or not and if yes continue else iterate things by taking feed back agin create new todos repeat until user agrees, this rules apply for evry task

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
    └── uv.lock                                       # UV package manager
    |__summary.md 
     lockfile
```

## Key Components
- **Core Module**: Python package in `src/` with modular architecture
- **AI Integration**: Gemini LLM for structured output generation
- **Multiple Formats**: Supports JSON, Markdown, YAML, and text outputs
- **Configuration**: Modern Python tooling with pyproject.toml and uv


task 1 :- go through folder structure understand it this is the basic repo which we are working with first create this complete basic repo inside "C:\Users\vijay\OneDrive\Desktop\practice-claude-code\ai-coding-course-claude\lessons\lesson-04-common-pitfalls\src" and after this go to claude-3 . goal  when i do "uv run main.py transcript.txt --output-format markdown" it has to save file with proper content accordingly and must open 3 window one with bar char,paichar and grph chart with word count values

Task 2: Add YAML Output Format Support
Add a new format_as_yaml function to the output formatting module.

Update the argument parser to include yaml as a valid --output-format option.

Update the main script to handle .yml output and use the new formatter.

Run Test Command:

bash
Copy
Edit
uv run main.py transcript.txt --output-format yaml
Check:

YAML file is generated with correct formatting.

No errors during execution.

If Errors:

Verify correct serialization method.

Ensure YAML library is installed.

Task 3: Enhance Bar Chart with Color-Coding
Update the bar chart function to apply color coding:

Top 25% of frequent words → green

Bottom 25% → red

Middle 50% → blue

Ensure the chart is sorted by frequency (descending).

Run Test Command:

bash
Copy
Edit
uv run main.py transcript.txt
Check:

Bar chart displays with correct color categories.

Colors correspond correctly to frequency quartiles.

If Errors:

Check for correct sorting.

Handle cases with too few data points.

Validate color application logic.

Task 4: Claude Model Switching Support (if using Claude agent ),switch with youre models and anlyze which id is better get a graph for that and disply it 
In any Claude-based code or prompt files, include model switch annotations:

Use appropriate tag for haiku, sonnet-3-5, or opus models.

No execution needed unless Claude integration is in use.

Task 5: Add Sentiment Analysis and Logging
Enhance the transcript analysis function to include:

Logging of key steps (e.g., start, end, issues)

Sentiment analysis and classification (positive, negative, neutral)

Log the final sentiment score and label.

Run Test Command:

bash
Copy
Edit
uv run main.py transcript.txt
Check:

Console output includes log entries for each processing step.

Sentiment label appears correctly in logs.

If Errors:

Ensure the sentiment tool is set up and available.

Verify logging is configured and not suppressed.