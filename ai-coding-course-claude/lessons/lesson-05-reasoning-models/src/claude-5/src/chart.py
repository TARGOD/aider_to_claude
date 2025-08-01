"""
Visualization module for generating charts
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from typing import Dict
import os
from datetime import datetime

def generate_bar_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    """Generate horizontal bar chart with color coding by frequency tiers."""
    if not freq_dict:
        return ""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Sort by frequency
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:20]  # Top 20 words
    words, counts = zip(*sorted_items)
    
    # Create color map based on frequency tiers
    max_count = max(counts)
    colors = []
    for count in counts:
        ratio = count / max_count
        if ratio >= 0.8:
            colors.append('#1f77b4')  # Dark blue for highest frequency
        elif ratio >= 0.6:
            colors.append('#ff7f0e')  # Orange for high frequency
        elif ratio >= 0.4:
            colors.append('#2ca02c')  # Green for medium frequency
        elif ratio >= 0.2:
            colors.append('#d62728')  # Red for low frequency
        else:
            colors.append('#9467bd')  # Purple for lowest frequency
    
    # Create figure
    plt.figure(figsize=(10, 8))
    plt.barh(words, counts, color=colors)
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Words', fontsize=12)
    plt.title('Top 20 Most Frequent Words', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()  # Highest frequency at top
    
    # Add value labels on bars
    for i, (word, count) in enumerate(zip(words, counts)):
        plt.text(count + 0.1, i, str(count), va='center')
    
    # Add grid for better readability
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    
    # Save chart
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"word_frequency_bar_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    
    return filepath

def generate_pie_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    """Generate pie chart showing word frequency distribution."""
    if not freq_dict:
        return ""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get top 10 words and group others
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_items[:10]
    other_count = sum(count for _, count in sorted_items[10:])
    
    # Prepare data
    labels = [word for word, _ in top_items]
    sizes = [count for _, count in top_items]
    
    if other_count > 0:
        labels.append('Others')
        sizes.append(other_count)
    
    # Create color palette
    colors = plt.cm.Set3(range(len(labels)))
    
    # Create figure
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Word Frequency Distribution (Top 10 + Others)', fontsize=14, fontweight='bold')
    plt.axis('equal')
    
    # Save chart
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"word_frequency_pie_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    
    return filepath