# Gemini Structured Output Example

This document contains example code for using the Gemini API with structured outputs.

## Basic Usage
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("Your prompt here")
print(response.text)
```