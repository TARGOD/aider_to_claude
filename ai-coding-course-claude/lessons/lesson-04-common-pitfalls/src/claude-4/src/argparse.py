"""Command-line argument parsing."""
import argparse
from pathlib import Path
from .constants import OUTPUT_FORMATS, DEFAULT_OUTPUT_FORMAT


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze transcript files using Google Gemini AI"
    )
    
    parser.add_argument(
        "transcript_file",
        type=Path,
        help="Path to the transcript file to analyze"
    )
    
    parser.add_argument(
        "--output-format",
        choices=OUTPUT_FORMATS,
        default=DEFAULT_OUTPUT_FORMAT,
        help=f"Output format for the analysis (default: {DEFAULT_OUTPUT_FORMAT})"
    )
    
    parser.add_argument(
        "--minimum-threshold",
        type=int,
        default=10,
        help="Minimum word count threshold for visualizations (default: 10)"
    )
    
    return parser.parse_args()