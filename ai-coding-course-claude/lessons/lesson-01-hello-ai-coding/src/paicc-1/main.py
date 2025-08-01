# PAICC-1: Hello AI Coding World
# Lesson 1 - Basic AI coding with Claude Code

def print_message(message):
    for i in range(10):
        print(message)

def word_frequency_counter():
    # Read the transcript file
    with open('transcript.txt', 'r') as file:
        content = file.read()
    
    # Clean and split the text into words
    import re
    words = re.findall(r'\b[a-zA-Z]+\b', content.lower())
    
    # Count word frequencies using a dictionary
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print("Word frequencies (sorted by count):")
    # Sort by count in descending order
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Show only words that appear more than 3 times with counts
    print("\nWords appearing more than 3 times:")
    for word, count in sorted_words:
        if count > 3:
            hashtags = "#" * count
            print(f"{word} ({count}): {hashtags}")
    
    print("\nAll word frequencies:")
    for word, count in sorted_words:
        hashtags = "#" * count
        print(f"{word}: {hashtags}")

# Run the Hello World part
message = "Hello AI Coding World"
print_message(message)

print("\n" + "="*50 + "\n")

# Run the word frequency counter
word_frequency_counter()