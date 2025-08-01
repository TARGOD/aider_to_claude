# Gemini API Structured Output Examples

## Basic Usage

```python
import google.generativeai as genai

# Configure API
genai.configure(api_key="YOUR_API_KEY")

# Create model
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate content
response = model.generate_content("Analyze this text...")
print(response.text)
```

## Structured Output with Response Schema

```python
from typing import List
from pydantic import BaseModel
import google.generativeai as genai

class Analysis(BaseModel):
    summary: str
    keywords: List[str]
    sentiment: str

# Configure model with response schema
model = genai.GenerativeModel(
    'gemini-2.0-flash',
    generation_config={
        "response_mime_type": "application/json",
        "response_schema": Analysis
    }
)

# Generate structured output
response = model.generate_content("Analyze this transcript...")
result = Analysis.model_validate_json(response.text)
```

## Token Counting

```python
# Count tokens before sending
model.count_tokens("Your text here")
```

## Best Practices

1. Always validate API responses
2. Handle rate limits and errors gracefully
3. Use structured outputs for consistent data formats
4. Implement retry logic for transient failures