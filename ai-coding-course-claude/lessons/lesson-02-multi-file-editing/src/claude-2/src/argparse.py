import argparse

def parse_arguments():
    """Parse command line arguments for the transcript analyzer."""
    parser = argparse.ArgumentParser(description="Analyze transcript files with word frequency and AI analysis")
    
    parser.add_argument(
        "transcript_file",
        help="Path to the transcript file to analyze"
    )
    
    parser.add_argument(
        "--min_count_threshold",
        type=int,
        default=3,
        help="Minimum word count threshold (default: 3)"
    )
    
    return parser.parse_args()