# PAICC-1 Repository Structure

```
paicc-1/
├── .gitignore                  # Git ignore rules
├── README.md                   # Project setup guide
├── main.py                     # Main Python script
└── transcript.txt              # OpenAI API video transcript
The above is the repository structure of the project that is to be done initially.After creating the folder structure in the current directory inside src that is to be created by you.

# TRANSCRIPT OF THE VIDEO THAT YOU SHOULD BE FOLLOWING AND PERFORMING THE TASK ACCORDINGLY.
# AI Coding Lesson 1: Setup and Introduction to AI-Assisted Development with Claude Code

## Course Information
- **Course**: Principled AI Coding
- **Lesson**: 1 - Getting Started with AI Coding
- **Key Principle**: KISS (Keep It Simple, Stupid)
- **Objective**: Set up AI tooling and learn fundamental AI coding patterns

## Prerequisites Installation
Before starting, ensure you have installed:
1. UV (Python package manager)
2. Git
3. Python
4. pip
5. VS Code (or preferred code editor)
6. Claude Code CLI

## Initial Setup Tasks

### 1. Verify Prerequisites
Run these commands to verify installations:
```bash
uv --version
git --version
python --version
pip --version
```

### 2. Create Working Directory
```bash
mkdir lesson1
cd lesson1
```

## Project Structure
Create the following structure in your current directory:
```
src/
└── paicc-1/
    ├── .gitignore
    ├── README.md
    ├── main.py
    └── transcript.txt
```
## Basic AI Coding with Claude Code

### Starting Claude Code
Simply type your instructions directly in the Claude Code interface. Claude will:
- Automatically understand context from your current directory
- Create, read, update files as needed
- Execute commands when appropriate

## Exercise 1: Basic AI Coding Tasks

### Task 1: Create Project Structure
**Instruction**: "Create a src directory with a paicc-1 folder inside containing .gitignore, README.md, main.py, and transcript.txt files"

### Task 2: Hello World
**Instruction**: "In main.py, write code to print 'Hello AI Coding World'"
- Claude will create/modify the file
- Ask Claude to run it: "Run the main.py file"

### Task 3: Print Multiple Times
**Instruction**: "Update main.py to print 'Hello AI Coding World' 10 times"
- Review the changes
- Ask to run: "Run the updated code"

### Task 4: Use Variables
**Instruction**: "Refactor the code to store 'Hello AI Coding World' in a variable, then use it in the print statements"

### Task 5: Create Function
**Instruction**: "Move the printing logic into a function that takes the message as a parameter"

### Task 6: Revert Changes (if needed)
**Instruction**: "Revert the last change" or "Go back to the previous version"

## Exercise 2: Word Frequency Counter Project

### Project Goal
Build a word frequency counter that analyzes a transcript file.

### Implementation Steps

1. **Prepare transcript file**
   **Instruction**: "Create a transcript.txt file with sample text about AI and coding"

2. **Read transcript file**
   **Instruction**: "In main.py, read the content from transcript.txt and store it in a variable"

3. **Count word frequencies**
   **Instruction**: "Add code to count the frequency of each word using a dictionary"

4. **Display frequencies**
   **Instruction**: "Display the word frequencies by printing hashtags (#) for each count"

5. **Sort results**
   **Instruction**: "Sort the word frequencies in descending order before displaying"

6. **Run the complete program**
   **Instruction**: "Run the word frequency counter"

### Enhancement Instructions

To improve the word frequency counter:

**Instruction**: "Modify the code to only show words that appear more than 3 times, and display the count number alongside each word before the hashtags"


follow the above transcript and to those changes in the src.
do the tasks in the order if any error occured solve it ,take your time and give me the result what i expect from the transcript.