import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from utils import get_percenatge_completed_bars, normalize


def main():
    matplotlib.rc('text', usetex=True)


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

    plt.figure(figsize=(5.3, 4))
    concurrent_requests = [i for i in range(11)]
    remote_times = [1110.0/1000, 1871.0/1000, 3973.0/1000, 7100.0/1000, 10295.0/1000, 14316.0/1000, 19637.0/1000, 24793.0/1000, 28960.0/1000, 32426.0/1000, 39791.0/1000]
    remote_error = [828.2/1000, 794.4/1000, 2023.5/1000, 3355.3/1000, 4442.6/1000, 5981.9/1000, 6651.1/1000, 8295.4/1000, 12878.6/1000, 15761.6/1000, 19756.9/1000]

    plt.errorbar(concurrent_requests, remote_times, color='red', ecolor='grey', yerr=remote_error, capsize=2, fmt='.',
                 label='Perform image processing in the cloud')

    plt.axhline(y=10491.0/1000, xmin=0, xmax=1.0, linewidth=2, color='blue', label='Perform image processing locally')
    plt.axhspan(10491.0/1000-1228.8/1000, 10491.0/1000+1228.8/1000, color='deepskyblue', alpha=0.5)

    plt.xlabel("Concurrent Requests to Server", fontsize=12)
    plt.ylabel("Request Latency (s)", fontsize=12)
    plt.title("$\it{ImPro}$ request latencies for varying server load", fontsize=14)
    # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    plt.legend()
    plt.tight_layout()

    plt.savefig('graphs/server-load.png')

    plt.figure(figsize=(6.4, 4.8))
    labels = ['Edge Node', 'Central Server']
    bar_width = 0.3
    mware_pos = np.arange(len(labels))
    no_mware_pos = [x + bar_width for x in mware_pos]

    no_mware_latencies = [140761.0/1000, 11292.0/1000]
    no_mware_error = [38917.9/1000, 4828.7/1000]

    mware_latencies = [165907.0/1000, 10344.0/1000]
    mware_error = [45752.4/1000, 4524.0/1000]

    plt.bar(mware_pos, mware_latencies, width=bar_width, color='blue', edgecolor=['black']*2, yerr=mware_error, capsize=7,
            label='With PAM')
    plt.bar(no_mware_pos, no_mware_latencies, width=bar_width, color='red', edgecolor=['black']*2, yerr=no_mware_error, capsize=7,
            label='Without PAM')

    plt.xticks([r + 1/2 * bar_width for r in range(len(labels))], labels)
    plt.ylabel("Request Latency (s)", fontsize=12)
    plt.xlabel("Processing Location", fontsize=12)
    plt.title("$\it{ImPro}$ request latencies with and without PAM", fontsize=14)
    plt.legend()
    plt.tight_layout()

    plt.savefig('graphs/comp-request-pol-latency-effect.png')


if __name__ == '__main__':
    main()
