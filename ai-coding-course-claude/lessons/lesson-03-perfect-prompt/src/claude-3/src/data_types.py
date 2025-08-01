"""Data models and type definitions."""
from typing import List, Dict
from pydantic import BaseModel


class TranscriptAnalysis(BaseModel):
    """Structure for transcript analysis results."""
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    word_count: Dict[str, int]
    total_words: int
    unique_words: int