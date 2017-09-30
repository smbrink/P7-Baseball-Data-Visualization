weight_bin code

import pandas as pd

baseball = pd.read_csv('baseball_data_deleted0.csv')

weight_bins = [0, 160, 170, 180, 190, 200, 210, 220, 230]
weight_labels = [160, 170, 180, 190, 200, 210, 220, 230]
baseball['weight_bin'] = pd.cut(baseball['weight'], weight_bins, labels=weight_labels)

baseball.to_csv('baseball_data_deleted0_new.csv', index=False)
