"""Visualization functions for word count data."""
import matplotlib.pyplot as plt
from typing import Dict


def word_count_bar_chart(word_count_dict: Dict[str, int], threshold_word_count: int) -> None:
    """Create a bar chart of word frequencies with color coding based on frequency quartiles.
    
    Color coding:
    - Top 25% of frequent words → green
    - Bottom 25% → red  
    - Middle 50% → blue
    
    Args:
        word_count_dict: Dictionary of word frequencies
        threshold_word_count: Minimum count threshold for words to include
    """
    # Filter words based on threshold
    filtered_words = {word: count for word, count in word_count_dict.items() 
                     if count >= threshold_word_count}
    
    # Sort by count (descending) - ensures proper frequency ordering
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    
    # Handle edge case with too few data points
    if len(sorted_words) < 4:
        words = [item[0] for item in sorted_words]
        counts = [item[1] for item in sorted_words]
        colors = ['blue'] * len(words)  # Default to blue for small datasets
    else:
        # Prepare data for plotting
        words = [item[0] for item in sorted_words]
        counts = [item[1] for item in sorted_words]
        
        # Calculate quartile boundaries
        total_words = len(words)
        top_25_cutoff = total_words // 4
        bottom_25_cutoff = total_words - (total_words // 4)
        
        # Assign colors based on frequency quartiles
        colors = []
        for i in range(total_words):
            if i < top_25_cutoff:  # Top 25%
                colors.append('green')
            elif i >= bottom_25_cutoff:  # Bottom 25%
                colors.append('red')
            else:  # Middle 50%
                colors.append('blue')
    
    # Create bar chart with color coding
    plt.figure(figsize=(12, 6))
    plt.bar(words, counts, color=colors)
    plt.xlabel('Words', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title(f'Word Frequency Bar Chart with Color Coding (threshold: {threshold_word_count})', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    
    # Add legend for color coding
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', label='Top 25% (Most frequent)'),
        Patch(facecolor='blue', label='Middle 50%'),
        Patch(facecolor='red', label='Bottom 25% (Least frequent)')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
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