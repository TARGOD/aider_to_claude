"""Data models and type definitions."""
from pydantic import BaseModel
from typing import List, Dict

class TranscriptAnalysis(BaseModel):
    """Model for transcript analysis results."""
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    sentiment: str
    word_count: Dict[str, int]
    total_words: int
    unique_words: int