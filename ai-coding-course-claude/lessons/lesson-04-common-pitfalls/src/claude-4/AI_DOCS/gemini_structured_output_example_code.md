# Gemini Structured Output Example Code

This document provides examples of how to use Google Gemini AI for structured output generation in transcript analysis.

## Basic Usage

```python
import google.generativeai as genai

# Configure API key
genai.configure(api_key="your-api-key-here")

# Define response schema
response_schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "bullet_points": {"type": "array", "items": {"type": "string"}},
        "keywords": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["summary", "bullet_points", "keywords"]
}

# Create model with structured output
model = genai.GenerativeModel(
    "gemini-2.0-flash",
    generation_config={
        "response_mime_type": "application/json",
        "response_schema": response_schema
    }
)

# Generate analysis
response = model.generate_content("Analyze this text...")
```

## Features

- Structured JSON output
- Schema validation
- Consistent formatting
- Easy integration with Python data models