"""Gemini AI integration module."""
import google.generativeai as genai
from typing import Dict, List
import re
import logging
from collections import Counter
from .constants import GEMINI_API_KEY, GEMINI_MODEL
from .data_types import TranscriptAnalysis

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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
                },
                "sentiment": {
                    "type": "object",
                    "properties": {
                        "score": {"type": "number"},
                        "label": {"type": "string"}
                    },
                    "required": ["score", "label"]
                }
            },
            "required": ["summary", "bullet_points", "keywords", "sentiment"]
        }
        self.model = genai.GenerativeModel(
            GEMINI_MODEL,
            generation_config={
                "response_mime_type": "application/json",
                "response_schema": response_schema
            }
        )
    
    def analyze_transcript(self, transcript_text: str) -> TranscriptAnalysis:
        """Analyze transcript using Gemini AI with sentiment analysis and logging."""
        logger.info("Starting transcript analysis...")
        
        try:
            # Calculate word count
            logger.info("Calculating word frequencies...")
            word_count = self._calculate_word_count(transcript_text)
            logger.info(f"Found {sum(word_count.values())} total words, {len(word_count)} unique words")
            
            # Create prompt for Gemini
            prompt = f"""Analyze the following transcript and provide:
1. A concise summary (2-3 sentences)
2. 3-5 key bullet points
3. 5-10 relevant keywords
4. Sentiment analysis with:
   - A sentiment score between -1.0 (very negative) and 1.0 (very positive)
   - A sentiment label: "positive", "negative", or "neutral"
   - Consider neutral if score is between -0.2 and 0.2

Transcript:
{transcript_text}
"""
            
            # Generate analysis
            logger.info("Sending request to Gemini AI for analysis...")
            response = self.model.generate_content(prompt)
            
            # Parse response
            import json
            response_data = json.loads(response.text)
            logger.info("Successfully received analysis from Gemini AI")
            
            # Extract sentiment data
            sentiment_score = response_data['sentiment']['score']
            sentiment_label = response_data['sentiment']['label']
            
            logger.info(f"Sentiment Analysis - Score: {sentiment_score:.2f}, Label: {sentiment_label}")
            
            # Create TranscriptAnalysis object with all required fields
            analysis = TranscriptAnalysis(
                summary=response_data['summary'],
                bullet_points=response_data['bullet_points'],
                keywords=response_data['keywords'],
                word_count=word_count,
                total_words=sum(word_count.values()),
                unique_words=len(word_count),
                sentiment_score=sentiment_score,
                sentiment_label=sentiment_label
            )
            
            logger.info("Transcript analysis completed successfully")
            return analysis
            
        except Exception as e:
            logger.error(f"Error during transcript analysis: {str(e)}")
            raise
    
    def _calculate_word_count(self, text: str) -> Dict[str, int]:
        """Calculate word frequency in the text."""
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Count word frequencies
        word_count = Counter(words)
        
        # Return as regular dict sorted by frequency
        return dict(word_count.most_common())