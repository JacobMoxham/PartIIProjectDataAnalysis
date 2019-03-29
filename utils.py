import numpy as np
from numpy import exp
import csv

def get_percenatge_completed_bars(file, xticks):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        times_for_percentiles = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            times_for_percentiles.append(float(row[1]))

        times_index = 0
        latency_proportions = []
        for tick in xticks:
            percentage_completed_in_tick = 0
            while times_index < len(times_for_percentiles) and tick > times_for_percentiles[times_index]:
                percentage_completed_in_tick += 1
                times_index += 1
            latency_proportions.append(percentage_completed_in_tick)

    return latency_proportions


def to_hist_data(xticks, data):
    output = []
    for i, x in enumerate(xticks):
        for j in range(data[i]):
            output.append(x)
    return output


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
       return v
    return v / norm


def gaussian(x, amp, cen, wid):
    return amp * exp(-(x-cen)**2 / wid)