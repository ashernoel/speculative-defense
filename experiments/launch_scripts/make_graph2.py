import matplotlib.pyplot as plt
import numpy as np

# Function to create a bar graph
def create_bar_graph(data, title, y_label, colors, file_name):
    # Number of groups
    n_groups = len(data)

    # Creating a figure and axis
    fig, ax = plt.subplots()

    # Index for groups and bar width
    index = np.arange(n_groups)
    bar_width = 0.35

    # Adjusting the position of the bars
    bar_positions = index + bar_width / 2

    # Creating bars and adding the percentage values above them
    bars = ax.bar(bar_positions, data.values(), bar_width, align='center', color=colors)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Setting the x-axis labels to the keys of the data dictionary
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(data.keys())

    # Setting other graph parameters
    plt.ylim(0, 30)  # Se
    plt.title(title)
    plt.ylabel(y_label)
    plt.savefig(file_name)
    plt.close()

# Data for the first graph (Attack Success Rate)
attack_success_rate = {
    'SPACY': 17, 
    'VICUNA': 14, 
    'FINETUNED VICUNA': 19
}

# Data for the second graph (False Positive Rate)
# Converting counts to percentages
false_positive_rate = {
    'SPACY': (6/23) * 100, 
    'VICUNA': (6/31) * 100, 
    'FINETUNED VICUNA': (2/16) * 100
}

# Create and save the graphs
create_bar_graph(attack_success_rate, 'Attack Success Rate Comparison', 'Attack Success Rate (%)', ['grey', 'red', 'darkred'], 'graph_attack_success_rate.png')
create_bar_graph(false_positive_rate, 'False Positive Rate Comparison', 'False Positive Rate (%)', ['grey', 'red', 'darkred'], 'graph_false_positive_rate.png')
