# weight_bin code

import pandas as pd

baseball = pd.read_csv('baseball_data_deleted0.csv')

weight_bins = [0, 160, 170, 180, 190, 200, 210, 220, 230]
weight_labels = [160, 170, 180, 190, 200, 210, 220, 230]
baseball['weight_bin'] = pd.cut(baseball['weight'], weight_bins, labels=weight_labels)

baseball.to_csv('baseball_data_deleted0_new.csv', index=False)

# added height bin code

baseball = pd.read_csv('baseball_data_deleted0_new.csv')

height_bins = [0, 68, 69, 70, 71, 72, 73, 74, 75, 76, 80]
height_labels = [68, 69, 70, 71, 72, 73, 74, 75, 76, 80]
baseball['height_bin'] = pd.cut(baseball['height'], height_bins, labels = height_labels)

baseball.to_csv('new_baseball_data_deleted0.csv', index = False)
