"""Visualization functions for word count data."""
import matplotlib.pyplot as plt
from typing import Dict


def word_count_bar_chart(word_count_dict: Dict[str, int], threshold_word_count: int) -> None:
    """Create a bar chart of word frequencies.
    
    Args:
        word_count_dict: Dictionary of word frequencies
        threshold_word_count: Minimum count threshold for words to include
    """
    # Filter words based on threshold
    filtered_words = {word: count for word, count in word_count_dict.items() 
                     if count >= threshold_word_count}
    
    # Sort by count (descending)
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    
    # Prepare data for plotting
    words = [item[0] for item in sorted_words]
    counts = [item[1] for item in sorted_words]
    
    # Create bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(words, counts, color='steelblue')
    plt.xlabel('Words', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Word Frequency Bar Chart (threshold: {threshold_word_count})', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Show the plot
    plt.show()


def word_count_pie_chart(word_count_dict: Dict[str, int], threshold_word_count: int) -> None:
    """Create a pie chart of word frequencies.
    
    Args:
        word_count_dict: Dictionary of word frequencies
        threshold_word_count: Minimum count threshold for words to include
    """
    # Filter words based on threshold
    filtered_words = {word: count for word, count in word_count_dict.items() 
                     if count >= threshold_word_count}
    
    # Sort by count (descending) and limit to top 15 for readability
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)[:15]
    
    # Prepare data for plotting
    words = [item[0] for item in sorted_words]
    counts = [item[1] for item in sorted_words]
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    colors = plt.cm.Set3(range(len(words)))
    plt.pie(counts, labels=words, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title(f'Word Frequency Pie Chart - Top 15 Words (threshold: {threshold_word_count})', 
              fontsize=14)
    plt.axis('equal')
    
    # Show the plot
    plt.show()


def word_count_line_graph(word_count_dict: Dict[str, int], threshold_word_count: int) -> None:
    """Create a line graph of word frequencies.
    
    Args:
        word_count_dict: Dictionary of word frequencies
        threshold_word_count: Minimum count threshold for words to include
    """
    # Filter words based on threshold
    filtered_words = {word: count for word, count in word_count_dict.items() 
                     if count >= threshold_word_count}
    
    # Sort by count (descending)
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    
    # Prepare data for plotting
    words = [item[0] for item in sorted_words]
    counts = [item[1] for item in sorted_words]
    positions = list(range(len(words)))
    
    # Create line graph
    plt.figure(figsize=(12, 6))
    plt.plot(positions, counts, marker='o', linestyle='-', color='darkgreen', 
             markersize=8, linewidth=2)
    
    # Add value labels on points
    for i, (pos, count) in enumerate(zip(positions, counts)):
        plt.annotate(str(count), (pos, count), textcoords="offset points", 
                    xytext=(0,10), ha='center')
    
    plt.xlabel('Words (sorted by frequency)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Word Frequency Line Graph (threshold: {threshold_word_count})', fontsize=14)
    plt.xticks(positions, words, rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Show the plot
    plt.show()