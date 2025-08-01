#!/usr/bin/env python3
"""
CLI Transcript Analyzer - Main Entry Point
"""
import sys
import os
from .argparse_module import parse_arguments
from .gemini_llm import GeminiAnalyzer
from .chart import generate_bar_chart, generate_pie_chart
from .output_format import format_as_json, format_as_markdown, format_as_yaml, format_as_text
from .constants import SUPPORTED_FORMATS

def read_transcript(file_path: str) -> str:
    """Read transcript file and return content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    """Main entry point for the CLI application."""
    # Parse arguments
    args = parse_arguments()
    
    # Read transcript
    print(f"Reading transcript from: {args.transcript_file}")
    transcript_text = read_transcript(args.transcript_file)
    
    # Analyze transcript
    print("Analyzing transcript...")
    analyzer = GeminiAnalyzer()
    analysis = analyzer.analyze_transcript(transcript_text, min_count=args.min_count)
    
    # Generate visualizations unless skipped
    bar_chart_path = None
    pie_chart_path = None
    if not args.no_charts:
        print("Generating visualizations...")
        bar_chart_path = generate_bar_chart(analysis.word_count)
        pie_chart_path = generate_pie_chart(analysis.word_count)
    
    # Format output based on requested format
    output_format = args.output_format.lower()
    if output_format == 'json':
        output = format_as_json(analysis)
    elif output_format == 'yaml':
        output = format_as_yaml(analysis)
    elif output_format == 'markdown':
        output = format_as_markdown(analysis, bar_chart_path, pie_chart_path)
    else:  # text format
        output = format_as_text(analysis)
    
    # Always save to file for all formats
    if args.output_file:
        output_filename = args.output_file
    else:
        # Auto-generate filename based on format
        file_extensions = {
            'markdown': '.md',
            'json': '.json',
            'yaml': '.yaml',
            'text': '.txt'
        }
        output_filename = f"analysis{file_extensions.get(output_format, '.txt')}"
    
    # Save the output
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(output)
    
    # Print confirmation
    print(f"\nAnalysis saved to: {output_filename}")
    if bar_chart_path:
        print(f"Bar Chart saved to: {bar_chart_path}")
    if pie_chart_path:
        print(f"Pie Chart saved to: {pie_chart_path}")

if __name__ == "__main__":
    main()