import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


# Function to create a bar graph with improved label handling
def create_bar_graph(data, title, y_label, colors, file_name, ylim=None):
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
    ax.set_xticklabels(data.keys(), rotation=45, ha='right')

    # Making the x-axis black
    ax.spines['bottom'].set_color('black')
    ax.axhline(0, color='black', linewidth=0.4)


    # Setting other graph parameters
    if ylim is not None:
        plt.ylim(ylim)
    else: 
        plt.ylim(0, max(data.values()) + 5)  # Setting the y-limit to be slightly higher than the max value
    plt.title(title)
    plt.ylabel(y_label)
    plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping
    plt.savefig(file_name)
    plt.close()

# Data for the first graph (Attack Success Rate)
attack_success_rate = {
    'SPACY': 17, 
    'Spec. Defense 1: \n Early Exiting \n Only': 14, 
    'Spec. Defense 2: \n Early Exiting with \n  Fine-tuning': 16.5,
    'Spec. Defense 3: \n Early Exiting and \n Drafting with \n Fine-tuning': 19
}

# Data for the second graph (False Positive Rate)
# Converting counts to percentages
false_positive_rate = {
    'SPACY': (6/23) * 100, 
    'Spec. Defense 1: \n Early Exiting \n Only': 6, 
    'Spec. Defense 2: \n Early Exiting with \n Fine-tuning': 4,
    'Spec. Defense 3: \n Early Exiting and \n Drafting with \n Fine-tuning': 6
}

def midpoint_color(color1, color2):
    return mcolors.to_hex((np.array(mcolors.to_rgb(color1)) + np.array(mcolors.to_rgb(color2))) / 2)

# Calculate the midpoint color between red and darkred
mid_color = midpoint_color('red', 'darkred')

# Updating the color for the third column in both graphs
colors_attack = ['grey', 'red', mid_color, 'darkred']
colors_false_positive = ['grey', 'red', mid_color, 'darkred']

# Create and save the graphs with the updated colors
create_bar_graph(attack_success_rate, 'Attack Success Rate Comparison', 'Attack Success Rate (%)', colors_attack, 'graph_attack_success_rate.png')
create_bar_graph(false_positive_rate, 'False Positive Rate Comparison', 'False Positive Rate (%)', colors_false_positive, 'graph_false_positive_rate.png')

# Data for the new graph (Inference Throughput Comparison)
inference_throughput = {
    'Baseline with Early Exit': 81.7,
    'Spec. Decoding w/o Defense': 85.8,
    'Spec. Defense w/ Fine-tuned \n Generating All Tokens': 78.9,
    'Spec. Defense Variant 1: \n Early Exiting Only': 83.2,
    'Spec. Defense Variant 2: \n Exiting & Some Generation': 82.1
}

# Calculate the percentage gain from the baseline (Baseline with Early Exit)
baseline_value = inference_throughput['Baseline with Early Exit']
percentage_gain = {key: ((value - baseline_value) / baseline_value) * 100 for key, value in inference_throughput.items()}

# Define colors for the bars
colors_inference = ['grey', 'darkgrey', 'lightgrey', 'red', 'darkred']

# Create and save the new graph
create_bar_graph(percentage_gain, 'Inference Throughput vs. Baseline', 'Throughput Gain vs. Baseline (%)', colors_inference, 'graph_inference_throughput.png', (-5, 8))