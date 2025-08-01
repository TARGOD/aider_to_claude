"""Output formatting functions for transcript analysis."""
import json
import yaml
from .data_types import TranscriptAnalysis


def format_as_string(transcript: TranscriptAnalysis) -> str:
    """Format analysis results as readable text."""
    output = []
    output.append("=== TRANSCRIPT ANALYSIS ===\n")
    
    output.append(f"SUMMARY:\n{transcript.summary}\n")
    
    output.append("BULLET POINTS:")
    for i, point in enumerate(transcript.bullet_points, 1):
        output.append(f"  {i}. {point}")
    output.append("")
    
    output.append("KEYWORDS:")
    output.append(f"  {', '.join(transcript.keywords)}\n")
    
    output.append("WORD COUNT STATISTICS:")
    output.append(f"  Total words: {transcript.total_words}")
    output.append(f"  Unique words: {transcript.unique_words}\n")
    
    output.append("TOP 20 MOST FREQUENT WORDS:")
    for i, (word, count) in enumerate(list(transcript.word_count.items())[:20], 1):
        output.append(f"  {i:2d}. {word}: {count}")
    
    return "\n".join(output)


def format_as_json(transcript: TranscriptAnalysis) -> str:
    """Format analysis results as JSON."""
    data = {
        "summary": transcript.summary,
        "bullet_points": transcript.bullet_points,
        "keywords": transcript.keywords,
        "statistics": {
            "total_words": transcript.total_words,
            "unique_words": transcript.unique_words
        },
        "word_count": transcript.word_count
    }
    return json.dumps(data, indent=2)


def format_as_markdown(transcript: TranscriptAnalysis) -> str:
    """Format analysis results as Markdown."""
    output = []
    output.append("# Transcript Analysis\n")
    
    output.append("## Summary")
    output.append(f"{transcript.summary}\n")
    
    output.append("## Key Points")
    for point in transcript.bullet_points:
        output.append(f"- {point}")
    output.append("")
    
    output.append("## Keywords")
    output.append(f"**Keywords:** {', '.join(transcript.keywords)}\n")
    
    output.append("## Statistics")
    output.append(f"- **Total words:** {transcript.total_words}")
    output.append(f"- **Unique words:** {transcript.unique_words}\n")
    
    output.append("## Top 20 Most Frequent Words")
    output.append("| Rank | Word | Count |")
    output.append("|------|------|-------|")
    for i, (word, count) in enumerate(list(transcript.word_count.items())[:20], 1):
        output.append(f"| {i} | {word} | {count} |")
    
    return "\n".join(output)


def format_as_yaml(transcript: TranscriptAnalysis) -> str:
    """Format analysis results as YAML."""
    data = {
        "transcript_analysis": {
            "summary": transcript.summary,
            "bullet_points": transcript.bullet_points,
            "keywords": transcript.keywords,
            "statistics": {
                "total_words": transcript.total_words,
                "unique_words": transcript.unique_words
            },
            "top_20_words": dict(list(transcript.word_count.items())[:20])
        }
    }
    return yaml.dump(data, default_flow_style=False, sort_keys=False)