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
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Setting the x-axis labels to the keys of the data dictionary
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(data.keys())

    # Setting other graph parameters
    plt.title(title)
    plt.ylabel(y_label)
    plt.ylim(0, 120)
    plt.savefig(file_name)
    plt.close()

# Data for the graphs
data1 = {'Vicuna-7B': 100, 'llama-2-7B chat': 88}
data2 = {'Vicuna-7B': 100, 'llama-2-7B chat': 0}
data3 = {'No defense': 100, 'Canary Defense': 17}
data4 = {'No defense': 100, 'Speculative Defense': 10}

# Create and save the graphs
create_bar_graph(data1, 'Paper results on "Harmful Behaviors" Dataset', 'Accuracy', ['black', 'black'], 'graph1.png')
create_bar_graph(data2, 'Our results on "Harmful Behaviors Dataset"', 'Accuracy', ['red', 'darkred'], 'graph2.png')
create_bar_graph(data3, 'Attack Success Rate Comparison', 'Attack Success Rate', ['darkred', 'red'], 'graph3.png')
create_bar_graph(data4, 'Attack Success Rate with Speculative Defense', 'Attack Success Rate', ['darkred', 'red'], 'graph4.png')
