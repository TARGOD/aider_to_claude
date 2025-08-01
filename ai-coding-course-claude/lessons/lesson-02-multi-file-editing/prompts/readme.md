NOTE:- keep human in loop 1] first go through each task separatly and prepare a todos and varify it with human in loop if agree with todos complete the task and if any test is mentioned complete the test and ask human in loop weather work done is correct or not and if yes continue else iterate things by taking feed back agin create new todos repeat until user agrees, this rules apply for evry task 

## Folder Structure
claude-2/
├── AI_DOCS/                        # Documentation for AI integration
│   └── gemini_structured_output_example_code.md
├── src/
│       |
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
  - Lists dependencies: gemini, pydantic, python-dotenv
  - Configures the build system (hatchling)
  - Sets up CLI script entry point

task 1 :- go through folder structure understand it this is the basic repo which we are working with first create this complete basic repo inside "C:\Users\vijay\OneDrive\Desktop\practice-claude-code\ai-coding-course-claude\lessons\lesson-02-multi-file-editing\src" and after this go to claude-2 and run "uv sync" and "uv run main" make sure its working without error

task 2:- 
# Complete Transcript Analyzer Application Development

Create a multi-file Python application for transcript analysis with the following specifications:

## File Structure and Components

### 1. Main Application (`main.py`)
- Update to accept CLI arguments for transcript file path and minimum count threshold (default: 3)
- Implement word frequency analysis with blacklist filtering
- Strip punctuation (periods, commas, exclamations) from words before counting
- Integrate Gemini LLM analysis and print results after keyword analysis
- Print keywords from LLM analysis results

### 2. Argument Parser (`argparse.py`)
- Create dedicated file for CLI argument parsing
- Handle `transcript_file` argument (required)
- Handle `min_count_threshold` argument with default value of 3
- Export `parse_arguments()` function

### 3. Constants (`constants.py`)
- Create word blacklist variable as a set containing common English words
- Include words like: "to", "the", "and", "a", "of", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "as", "with", "his", "they", "i", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "which", "she", "do", "has", "will", "if", "about", "get", "go", "me"

### 4. Data Types (`data_types.py`)
- Use Pydantic to create `TranscriptAnalysis` base model with fields:
  - `quick_summary: str` - Brief summary of transcript content
  - `bullet_point_highlights: List[str]` - Key points as bullet list
  - `sentiment_analysis: str` - Overall sentiment assessment
  - `keywords: List[str]` - Important keywords extracted from content

### 5. Gemini Integration (`gemini_llm.py`)
- Create `analyze_transcript(transcript: str, word_count: dict) -> TranscriptAnalysis` function
- Use Google Gemini API with user's API key "AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0" and  model "gemini-2.0-flash"
- Pass both transcript content and word frequency data to the model
- Use structured output to return TranscriptAnalysis object
- Include system message: "You are a helpful assistant analyzing transcripts. Provide concise analysis including summary, highlights, sentiment, and extract important keywords based on the content and word frequency data provided."

## Implementation Requirements

- Use proper Python imports and relative imports between files
- Handle file reading and text processing efficiently
- Implement proper error handling for file operations and API calls
- Use UV package manager compatible structure
- Filter words through blacklist before counting frequencies
- Only count words that appear more than the specified threshold
- Clean and normalize text by converting to lowercase and stripping punctuation
- Integrate all components seamlessly in main.py

## Usage Example
```bash
uv run main.py transcript.txt --min_count_threshold 5
```

## Dependencies Required
- google-generativeai (for Gemini API)
- pydantic (for data models)
- argparse (built-in)

Create all files with proper structure, imports, and functionality as specified above.and run it and test it if any error iterate it corect it youreself 


