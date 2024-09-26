#!/share/apps/python/anaconda/bin/python

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# RUNS = ['original_ijk',
#         'kij',
#         'kji',
#         'jki',
#         'block-original',
#         'block-jki-8'] 

#general
# RUNS = ['jki',
#         'block-original-ijk-16',
#         'block-jki-16',
#         'block-jki-8',
#         'block-jki-32',
#         'block-jki-64'] 

#blocks
# RUNS = ['original_ijk',
#         'jki',
#         'block-jki-64',
#         'block-jki-128'] 

# RUNS = [
#         'block-jki-8',
#         'block-jki-16',
#         'block-jki-32',
#         'block-jki-64',
#         'block-jki-128'] 


# RUNS = ['jki',
#         'block-jki-64',
#         'block-flags',
#         'block-flags1',
#         'restrict',
#         'restrict-plus']

RUNS = ['blas','restrict',
        'restrict-plus8']

def make_plot(runs):
    "Plot results of timing trials"
    for arg in runs:
        df = pd.read_csv(f"timing-{arg}.csv")
        plt.plot(df['size'], df['mflop']/1e3, label=arg)
    plt.xlabel('Dimension')
    plt.ylabel('Gflop/s')

def show(runs):
    make_plot(runs)
    lgd = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

def main():
    make_plot(RUNS)  # Use the predefined runs
    lgd = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('timing_custom.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

if __name__ == "__main__":
    main()
