"""
Configuration constants for the CLI Transcript Analyzer
"""

# Gemini API Configuration
GEMINI_API_KEY = "AIzaSyCgWYGWiJ07fsIUOIMSdZZjAlUAm2hE4v0"
GEMINI_MODEL_NAME = "gemini-2.0-flash"

# Supported output formats
SUPPORTED_FORMATS = ["json", "yaml", "markdown", "text"]

# Default minimum word count
DEFAULT_MIN_COUNT = 3

# Common stopwords to filter out
STOPWORDS = [
    "the", "and", "of", "to", "a", "in", "that", "is", "it", "for",
    "on", "with", "as", "at", "by", "this", "from", "be", "are", "an",
    "or", "was", "but", "not", "have", "has", "had", "do", "does", "did",
    "will", "would", "could", "should", "may", "might", "must", "can",
    "am", "been", "being", "were", "what", "which", "who", "where", "when",
    "why", "how", "all", "each", "every", "some", "any", "no", "there",
    "if", "then", "so", "than", "very", "just", "only", "also", "more",
    "most", "many", "much", "few", "less", "least", "own", "same", "such",
    "both", "either", "neither", "another", "other", "others", "else"
]

# Punctuation to remove
PUNCTUATION_BLACKLIST = [".", "!", ",", "?", ";", ":", "'", '"', "-", "(", ")", "[", "]", "{", "}", "/", "\\", "|", "@", "#", "$", "%", "^", "&", "*", "_", "+", "=", "~", "`", "<", ">"]