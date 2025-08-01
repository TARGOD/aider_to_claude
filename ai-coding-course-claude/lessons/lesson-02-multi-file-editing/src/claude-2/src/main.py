#!/usr/bin/env python3

import os
import string
from collections import Counter
from .argparse import parse_arguments
from .constants import WORD_BLACKLIST
from .gemini_llm import analyze_transcript

def read_transcript_file(file_path: str) -> str:
    """Read transcript file and return its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def clean_and_count_words(text: str, min_threshold: int) -> dict:
    """Clean text, remove punctuation, filter blacklisted words, and count frequencies."""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation from each word
    cleaned_words = []
    for word in words:
        # Remove punctuation (periods, commas, exclamations, etc.)
        cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
        if cleaned_word:  # Only add non-empty words
            cleaned_words.append(cleaned_word)
    
    # Filter out blacklisted words
    filtered_words = [word for word in cleaned_words if word not in WORD_BLACKLIST]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Filter by minimum threshold
    return {word: count for word, count in word_counts.items() if count >= min_threshold}

def main():
    """Main application entry point."""
    # Parse command line arguments
    args = parse_arguments()
    
    # Read transcript file
    transcript_content = read_transcript_file(args.transcript_file)
    if not transcript_content:
        return
    
    print(f"Analyzing transcript: {args.transcript_file}")
    print(f"Minimum count threshold: {args.min_count_threshold}")
    print("-" * 50)
    
    # Perform word frequency analysis
    word_counts = clean_and_count_words(transcript_content, args.min_count_threshold)
    
    print("Word Frequency Analysis:")
    if word_counts:
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {word}: {count}")
    else:
        print("  No words found above the threshold.")
    
    print("-" * 50)
    
    # Perform Gemini LLM analysis
    print("Gemini AI Analysis:")
    try:
        analysis = analyze_transcript(transcript_content, word_counts)
        
        print(f"\nQuick Summary:")
        print(f"  {analysis.quick_summary}")
        
        print(f"\nBullet Point Highlights:")
        for highlight in analysis.bullet_point_highlights:
            print(f"  • {highlight}")
        
        print(f"\nSentiment Analysis:")
        print(f"  {analysis.sentiment_analysis}")
        
        print(f"\nKeywords from LLM Analysis:")
        for keyword in analysis.keywords:
            print(f"  • {keyword}")
            
    except Exception as e:
        print(f"Error during Gemini analysis: {e}")

if __name__ == "__main__":
    main()