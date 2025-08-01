"""Application entry point."""
import sys
from pathlib import Path
from .argparse import parse_arguments
from .gemini_llm import GeminiAnalyzer
from .data_types import TranscriptAnalysis
from .output_format import (
    format_as_string,
    format_as_json,
    format_as_markdown,
    format_as_yaml
)
from .chart import (
    word_count_bar_chart,
    word_count_pie_chart,
    word_count_line_graph
)


def main():
    """Main application entry point."""
    # Parse arguments
    args = parse_arguments()
    
    # Check if file exists
    if not args.transcript_file.exists():
        print(f"Error: File '{args.transcript_file}' not found.")
        sys.exit(1)
    
    # Read transcript
    try:
        transcript_text = args.transcript_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Analyze transcript
    print("Analyzing transcript...")
    analyzer = GeminiAnalyzer()
    
    try:
        analysis = analyzer.analyze_transcript(transcript_text)
    except Exception as e:
        print(f"Error analyzing transcript: {e}")
        sys.exit(1)
    
    # Format results based on output format
    formatters = {
        "text": format_as_string,
        "json": format_as_json,
        "markdown": format_as_markdown,
        "yaml": format_as_yaml
    }
    
    formatter = formatters[args.output_format]
    output = formatter(analysis)
    
    # Determine output filename and extension
    extensions = {
        "text": ".txt",
        "json": ".json",
        "markdown": ".md",
        "yaml": ".yml"
    }
    
    # Create output filename based on input filename
    output_filename = args.transcript_file.stem + "_analysis" + extensions[args.output_format]
    output_path = args.transcript_file.parent / output_filename
    
    # Save to file
    try:
        output_path.write_text(output, encoding='utf-8')
        print(f"Analysis saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")
        sys.exit(1)
    
    # Also display to console
    print("\n" + output)
    
    # Generate visualizations after file output
    print("\nGenerating visualizations...")
    
    # Generate all 3 visualizations
    word_count_bar_chart(analysis.word_count, args.minimum_threshold)
    word_count_pie_chart(analysis.word_count, args.minimum_threshold)
    word_count_line_graph(analysis.word_count, args.minimum_threshold)
    
    print("Visualizations complete!")


if __name__ == "__main__":
    main()