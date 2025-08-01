"""
Output formatting module supporting multiple formats
"""
import json
import yaml
from typing import Optional
from .datatypes import TranscriptAnalysis

def format_as_json(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as JSON."""
    return json.dumps(analysis.model_dump(), indent=2)

def format_as_yaml(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as YAML."""
    return yaml.dump(analysis.model_dump(), default_flow_style=False, sort_keys=False)

def format_as_markdown(analysis: TranscriptAnalysis, bar_chart_path: Optional[str] = None, pie_chart_path: Optional[str] = None) -> str:
    """Format analysis results as Markdown."""
    md_content = f"""# Transcript Analysis Report

## Executive Summary
{analysis.summary}

## Key Points
"""
    for point in analysis.bullet_points:
        md_content += f"- {point}\n"
    
    md_content += f"""
## Keywords
{', '.join(analysis.keywords)}

## Sentiment Analysis
{analysis.sentiment.capitalize()}

## Statistics
- **Total Words**: {analysis.total_words}
- **Unique Words**: {analysis.unique_words}
- **Words Above Threshold**: {len(analysis.word_count)}

## Top Words by Frequency
| Word | Count |
|------|-------|
"""
    # Add top 15 words to table
    sorted_words = sorted(analysis.word_count.items(), key=lambda x: x[1], reverse=True)[:15]
    for word, count in sorted_words:
        md_content += f"| {word} | {count} |\n"
    
    # Add chart references if provided
    if bar_chart_path:
        md_content += f"\n## Visualizations\n\n### Word Frequency Bar Chart\n![Word Frequency Bar Chart]({bar_chart_path})\n"
    
    if pie_chart_path:
        md_content += f"\n### Word Distribution Pie Chart\n![Word Distribution Pie Chart]({pie_chart_path})\n"
    
    return md_content

def format_as_text(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as plain text."""
    text_content = f"""TRANSCRIPT ANALYSIS REPORT
========================

EXECUTIVE SUMMARY:
{analysis.summary}

KEY POINTS:
"""
    for i, point in enumerate(analysis.bullet_points, 1):
        text_content += f"{i}. {point}\n"
    
    text_content += f"""
KEYWORDS: {', '.join(analysis.keywords)}

SENTIMENT: {analysis.sentiment.capitalize()}

STATISTICS:
- Total Words: {analysis.total_words}
- Unique Words: {analysis.unique_words}
- Words Above Threshold: {len(analysis.word_count)}

TOP WORDS BY FREQUENCY:
"""
    sorted_words = sorted(analysis.word_count.items(), key=lambda x: x[1], reverse=True)[:15]
    for word, count in sorted_words:
        text_content += f"  {word}: {count}\n"
    
    return text_content