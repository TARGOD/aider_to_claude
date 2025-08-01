"""Gemini AI integration module."""
import google.generativeai as genai
from typing import Dict, List
import re
from collections import Counter
from .constants import GEMINI_API_KEY, GEMINI_MODEL
from .data_types import TranscriptAnalysis


class GeminiAnalyzer:
    """Handles Google Gemini AI interactions."""
    
    def __init__(self):
        """Initialize Gemini with API key."""
        genai.configure(api_key=GEMINI_API_KEY)
        # Define a simplified schema for Gemini
        response_schema = {
            "type": "object",
            "properties": {
                "summary": {"type": "string"},
                "bullet_points": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "keywords": {
                    "type": "array", 
                    "items": {"type": "string"}
                }
            },
            "required": ["summary", "bullet_points", "keywords"]
        }
        self.model = genai.GenerativeModel(
            GEMINI_MODEL,
            generation_config={
                "response_mime_type": "application/json",
                "response_schema": response_schema
            }
        )
    
    def analyze_transcript(self, transcript_text: str) -> TranscriptAnalysis:
        """Analyze transcript using Gemini AI."""
        # Calculate word count
        word_count = self._calculate_word_count(transcript_text)
        
        # Create prompt for Gemini
        prompt = f"""Analyze the following transcript and provide:
1. A concise summary (2-3 sentences)
2. 3-5 key bullet points
3. 5-10 relevant keywords

Transcript:
{transcript_text}
"""
        
        # Generate analysis
        response = self.model.generate_content(prompt)
        
        # Parse response
        import json
        response_data = json.loads(response.text)
        
        # Create TranscriptAnalysis object with all required fields
        analysis = TranscriptAnalysis(
            summary=response_data['summary'],
            bullet_points=response_data['bullet_points'],
            keywords=response_data['keywords'],
            word_count=word_count,
            total_words=sum(word_count.values()),
            unique_words=len(word_count)
        )
        
        return analysis
    
    def _calculate_word_count(self, text: str) -> Dict[str, int]:
        """Calculate word frequency in the text."""
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Count word frequencies
        word_count = Counter(words)
        
        # Return as regular dict sorted by frequency
        return dict(word_count.most_common())