import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from utils import get_percenatge_completed_bars, normalize


def main():
    # server_memory = [9, 12, 19, 74, 149, 434]
    # # bar_width = 0.3
    # remote_bars = [5824, 5951, 6146, 5086, 79863, 110741]
    # remote_error = [1911.5, 1616.6, 1672.4, 1459.4, 19775.7, 13417.2]
    # # remote_pos = np.arange(len(server_memory))
    #
    # local_bars = []
    # local_error = []
    # # local_pos = [x + bar_width for x in remote_pos[1:]]
    #
    # plt.errorbar(server_memory, remote_bars, color='red', ecolor='grey', yerr=remote_error, capsize=2, fmt='.', label='Remote')
    # # plt.errorbar(server_memory, local_bars, color='blue', yerr=local_error, capsize=7, label='Local')
    #
    # # plt.xticks([r + bar_width for r in range(len(remote_bars))], server_memory)
    # plt.xlabel("File Size (KB)")
    # plt.ylabel("Request Latency (Ms)")
    # plt.title("Time taken to complete 100 image processing requests (5 at a time)\n"
    #           "for various file sizes")
    # # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    # plt.legend()
    # plt.tight_layout()
    #
    # plt.savefig('graphs/file-size-latency.png')

    # concurrent_requests = [i for i in range(11)]
    # remote_times = [1110, 1871, 3973, 7100, 10295, 14316, 19637, 24793, 28960, 32426, 39791]
    # remote_error = [828.2, 794.4, 2023.5, 3355.3, 4442.6, 5981.9, 6651.1, 8295.4, 12878.6, 15761.6, 19756.9]
    #
    # plt.errorbar(concurrent_requests, remote_times, color='red', ecolor='grey', yerr=remote_error, capsize=2, fmt='.',
    #              label='Remote')
    #
    # plt.axhline(y=10491, xmin=0, xmax=1.0, linewidth=2, color='blue', label='Local')
    # plt.axhspan(10491-1228.8, 10491+1228.8, color='deepskyblue', alpha=0.5)
    #
    # plt.xlabel("Concurrent Requests to Server")
    # plt.ylabel("Request Latency (Ms)")
    # plt.title("Time taken to complete 100 remote image processing requests (5 at a time)\n"
    #           "while the Server is under various loads")
    # # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    # plt.legend()
    # plt.tight_layout()
    #
    # plt.savefig('graphs/server-load.png')

    labels = ['Local', 'Remote']
    bar_width = 0.3
    mware_pos = np.arange(len(labels))
    no_mware_pos = [x + bar_width for x in mware_pos]

    no_mware_latencies = [140761, 11292]
    no_mware_error = [38917.9, 4828.7]

    mware_latencies = [165907, 10344]
    mware_error = [45752.4, 4524.0]

    plt.bar(mware_pos, mware_latencies, width=bar_width, color='blue', edgecolor='black', yerr=mware_error, capsize=7,
            label='With PAM')
    plt.bar(no_mware_pos, no_mware_latencies, width=bar_width, color='red', edgecolor='black', yerr=no_mware_error, capsize=7,
            label='Without PAM')


    plt.xticks([r + 1/2 * bar_width for r in range(len(labels))], labels)
    plt.ylabel("Request Latency (ms)")
    plt.title("Time taken to complete 100 image processing requests (5 at a time)\n"
              "with and without PAM.")
    plt.legend()
    plt.tight_layout()

    plt.savefig('graphs/comp-request-pol-latency-effect.pgf')


if __name__ == '__main__':
    main()
