"""
Gemini API integration for transcript analysis
"""
import google.generativeai as genai
from collections import Counter
from typing import Dict
import json
import re

from .constants import (
    GEMINI_API_KEY, 
    GEMINI_MODEL_NAME, 
    STOPWORDS, 
    PUNCTUATION_BLACKLIST
)
from .datatypes import TranscriptAnalysis

class GeminiAnalyzer:
    """Handles transcript analysis using Gemini API."""
    
    def __init__(self):
        """Initialize Gemini API client."""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    
    def clean_text(self, text: str) -> str:
        """Clean text by removing punctuation and converting to lowercase."""
        text = text.lower()
        # Remove punctuation
        for punct in PUNCTUATION_BLACKLIST:
            text = text.replace(punct, ' ')
        return text
    
    def count_words(self, text: str, min_count: int = 3) -> Dict[str, int]:
        """Count word frequency excluding stopwords and below threshold."""
        cleaned_text = self.clean_text(text)
        words = cleaned_text.split()
        
        # Filter out stopwords and count
        filtered_words = [word for word in words if word not in STOPWORDS and len(word) > 1]
        word_counts = Counter(filtered_words)
        
        # Filter by minimum count
        filtered_counts = {word: count for word, count in word_counts.items() if count >= min_count}
        
        return dict(sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True))
    
    def analyze_transcript(self, text: str, min_count: int = 3) -> TranscriptAnalysis:
        """Analyze transcript text using Gemini API."""
        # Get word frequency
        word_count = self.count_words(text, min_count)
        total_words = len(self.clean_text(text).split())
        unique_words = len(set(self.clean_text(text).split()))
        
        # Prepare prompt for Gemini
        prompt = f"""
        Analyze the following transcript and provide:
        1. A concise executive summary (2-3 sentences)
        2. 3-5 key bullet points
        3. 5-8 important keywords
        4. Overall sentiment analysis (positive, negative, neutral, mixed)
        
        Transcript:
        {text}
        
        Please format your response as JSON with the following structure:
        {{
            "summary": "Executive summary here",
            "bullet_points": ["point 1", "point 2", "point 3"],
            "keywords": ["keyword1", "keyword2", "keyword3"],
            "sentiment": "positive/negative/neutral/mixed"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            response_text = response.text
            
            # Extract JSON from response
            json_match = re.search(r'\{[\s\S]*\}', response_text)
            if json_match:
                ai_analysis = json.loads(json_match.group())
            else:
                # Fallback if JSON extraction fails
                ai_analysis = {
                    "summary": "Unable to generate summary",
                    "bullet_points": ["Analysis failed"],
                    "keywords": ["error"],
                    "sentiment": "neutral"
                }
        except Exception as e:
            print(f"Gemini API error: {e}")
            ai_analysis = {
                "summary": f"Error generating summary: {str(e)}",
                "bullet_points": ["API error occurred"],
                "keywords": ["error"],
                "sentiment": "neutral"
            }
        
        # Create and return TranscriptAnalysis object
        return TranscriptAnalysis(
            summary=ai_analysis.get("summary", ""),
            bullet_points=ai_analysis.get("bullet_points", []),
            keywords=ai_analysis.get("keywords", []),
            sentiment=ai_analysis.get("sentiment", "neutral"),
            word_count=word_count,
            total_words=total_words,
            unique_words=unique_words
        )