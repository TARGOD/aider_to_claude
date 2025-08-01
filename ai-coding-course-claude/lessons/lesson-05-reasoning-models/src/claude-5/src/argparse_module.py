"""
Argument parser for CLI Transcript Analyzer
"""
import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="CLI Transcript Analyzer - Analyze transcript files with AI-powered insights"
    )
    
    # Required positional argument
    parser.add_argument(
        'transcript_file',
        type=str,
        help='Path to the transcript file to analyze'
    )
    
    # Optional arguments
    parser.add_argument(
        '--min_count',
        type=int,
        default=3,
        help='Minimum word count threshold (default: 3)'
    )
    
    parser.add_argument(
        '--output-format',
        type=str,
        choices=['json', 'yaml', 'markdown', 'text'],
        default='text',
        help='Output format for the analysis results (default: text)'
    )
    
    parser.add_argument(
        '--output-file',
        type=str,
        help='Save output to a file instead of printing to console'
    )
    
    parser.add_argument(
        '--no-charts',
        action='store_true',
        help='Skip generating visualization charts'
    )
    
    return parser.parse_args()