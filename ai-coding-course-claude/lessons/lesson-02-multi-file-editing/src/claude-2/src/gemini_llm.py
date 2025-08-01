import google.generativeai as genai
from .data_types import TranscriptAnalysis
import json

def analyze_transcript(transcript: str, word_count: dict) -> TranscriptAnalysis:
    """Analyze transcript using Google Gemini API with structured output."""
    
    # Configure Gemini API
    genai.configure(api_key="AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0")
    
    # Create model instance
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Prepare the prompt with both transcript and word frequency data
    prompt = f"""You are a helpful assistant analyzing transcripts. Provide concise analysis including summary, highlights, sentiment, and extract important keywords based on the content and word frequency data provided.

Transcript content:
{transcript}

Word frequency data:
{json.dumps(word_count, indent=2)}

Please provide your analysis in the following JSON format:
{{
    "quick_summary": "Brief summary of transcript content",
    "bullet_point_highlights": ["Key point 1", "Key point 2", "Key point 3"],
    "sentiment_analysis": "Overall sentiment assessment",
    "keywords": ["keyword1", "keyword2", "keyword3"]
}}"""
    
    try:
        # Generate response
        response = model.generate_content(prompt)
        
        # Parse JSON response
        json_str = response.text.strip()
        if json_str.startswith('```json'):
            json_str = json_str[7:-3].strip()
        elif json_str.startswith('```'):
            json_str = json_str[3:-3].strip()
            
        analysis_data = json.loads(json_str)
        
        # Return Pydantic model
        return TranscriptAnalysis(**analysis_data)
        
    except Exception as e:
        # Return default analysis if API fails
        return TranscriptAnalysis(
            quick_summary=f"Analysis failed: {str(e)}",
            bullet_point_highlights=["Error occurred during analysis"],
            sentiment_analysis="Unable to determine sentiment",
            keywords=list(word_count.keys())[:5] if word_count else []
        )