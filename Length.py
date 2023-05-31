import pandas as pd
import matplotlib.pyplot as plt


def length_stats(filecsv):
    df = pd.read_csv(filecsv)
    print(f"Length of shortest sequence: {df['LENGTH'].min()}")
    print(f"Length of longest sequence: {df['LENGTH'].max()}")
    print(f"Average length of sequences: {df['LENGTH'].mean():0.2f}")
    upper = df[df.LENGTH <= 700]
    lowerupper = upper[upper.LENGTH >= 400]
    print(f"There are {lowerupper.shape[0]} sequences with lengths between 450 and 650 .")
    print(f"This is {lowerupper.shape[0]/df.shape[0]*100:0.2f}% of the original dataset. ")

    # Project settings for plots
    plt.style.use('bmh')
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'UGent Panno Text'
    plt.rcParams['font.monospace'] = 'UGent Panno Text'
    plt.rcParams['font.size'] = 20
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 20
    plt.rcParams['xtick.labelsize'] = 20
    plt.rcParams['ytick.labelsize'] = 20
    plt.rcParams['legend.fontsize'] = 20
    # For main: (UGent blue: color='#1E64C8')
    # For main: (black: color='black')
    # For accents: (UGent yellow: color='#FFD200', linestyle='dashed', linewidth=2)
    # Set an aspect ratio

    df.plot.hist(color='#1E64C8', bins=100, align='right', edgecolor='#1E64C8', legend=None)
    plt.title(f'Distribution of the lengths of ITS sequences from QIIME release with {filecsv[9:-10]}% similarity threshold', fontweight='bold')
    plt.xlabel('Length of ITS')
    plt.xticks(range(0, 1501, 50), rotation='vertical')
    plt.axvline(x=400, color='#FFD200', linestyle='dashed', linewidth=2)
    plt.gca().get_xticklabels()[8].set_weight('bold')
    plt.axvline(x=700, color='#FFD200', linestyle='dashed', linewidth=2)
    plt.gca().get_xticklabels()[14].set_weight('bold')
    # svg ensures no loss of quality when enlarging
    plt.savefig(f'LengthDistribution{filecsv[9:-10]}.svg')
    plt.show()


#length_stats('Taxonomy_97_final.csv')
length_stats('Taxonomy_99_final.csv')
# length_stats('Taxonomy_dynamic_final.csv')
