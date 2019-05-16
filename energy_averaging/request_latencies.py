import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from utils import get_percenatge_completed_bars, normalize


def main():
    xticks = [500*i for i in range(2000)]
    # mware_latency_proportions_100_10 = get_percenatge_completed_bars('data/mware-100-10.csv', xticks)
    # no_mware_latency_proportions_100_10 = get_percenatge_completed_bars('data/no-mware-100-10.csv', xticks)
    # mware_caching_latency_proportions_100_10 = get_percenatge_completed_bars('data/mware-caching-100-10.csv', xticks)
    #
    # # TODO: consider whether align should be to the left
    # # xticks = [100 * i for i in range(300)]
    # # mware_5_1 = get_percenatge_completed_bars('data/mware-5-1.csv', xticks)
    #
    # xticks = [100 * i for i in range(300)]
    # # mware_100_1 = get_percenatge_completed_bars('data/mware-100-1.csv', xticks)
    # mware_50_10 = get_percenatge_completed_bars('data/mware-50-10.csv', xticks)
    #
    # plt.bar(xticks, mware_latency_proportions_100_10, width=100)
    # plt.bar(xticks, no_mware_latency_proportions_100_10, width=100)
    # plt.bar(xticks, mware_caching_latency_proportions_100_10, width=100)
    #
    # plt.xlabel("time (ms)")
    # plt.ylabel("Proportion of requests completed")
    # plt.title("The proportion of requests completed over time when benchmarking with and without PAM")
    # plt.legend(["Without PAM", "With PAM and Caching"])
    # plt.tight_layout()
    #
    # plt.savefig('graphs/percentages-completed-even-closer-100-10.png')
    #
    # compute_on_server_20p = get_percenatge_completed_bars('data/compute-20p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_server_20p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Centralised 20%")
    # # h = to_hist_data(xticks, compute_on_server_20p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_server_10p = get_percenatge_completed_bars('data/compute-10p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_server_10p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Centralised 10%")
    # # h = to_hist_data(xticks, compute_on_server_10p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_server_5p = get_percenatge_completed_bars('data/compute-5p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_server_5p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Centralised 5%")
    # # h = to_hist_data(xticks, compute_on_server_5p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_server_2p = get_percenatge_completed_bars('data/compute-2p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_server_2p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Centralised 2%")
    # # h = to_hist_data(xticks, compute_on_server_2p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_nodes_20p = get_percenatge_completed_bars('data/raw-20p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_nodes_20p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Decentralised 20%")
    # # h = to_hist_data(xticks, compute_on_nodes_20p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_nodes_10p = get_percenatge_completed_bars('data/raw-10p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_nodes_10p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Decentralised 10%")
    # # h = to_hist_data(xticks, compute_on_nodes_10p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # compute_on_nodes_5p = get_percenatge_completed_bars('data/raw-5p-network-simulated-post-update.csv', xticks)
    # plt.bar(xticks, normalize(compute_on_nodes_5p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #         label="Decentralised 5%")
    # # h = to_hist_data(xticks, compute_on_nodes_5p)
    # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # plt.plot(h, normalize(fit), 'k--')
    #
    # # This data is corrupt because there was lots of errors
    # # compute_on_nodes_2p = get_percenatge_completed_bars('data/raw-2p-network-simulated-post-update.csv', xticks)
    # # plt.bar(xticks, normalize(compute_on_nodes_2p), width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    # #         label="Decentralised 2%")
    # # # h = to_hist_data(xticks, compute_on_nodes_2p)
    # # # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    # # # plt.plot(h, normalize(fit), 'k--')


    # plt.xlabel("Time (ms)")
    # plt.ylabel("Proportion of requests completed")
    # plt.title("Time taken to complete 100 data averaging requests (10 at a time)\n"
    #           "for various Server:Data Node power ratios using 5 data nodes")
    # # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    # plt.legend()
    # plt.tight_layout()
    #
    # plt.savefig('graphs/cpu-effect-push-data.png')
    #
    # for server_mem in ["4M", "10M", "20M", "50M", "100M", "200M"]:
    #     # compute_percent = get_percenatge_completed_bars("data/compute-" + server_mem + "-network-simulated-post-update.csv", xticks)
    #     # plt.bar(xticks, normalize(compute_percent),  width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #     #         label="Compute " + server_mem)
    #     # h = to_hist_data(xticks, compute_percent)
    #     # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    #     # plt.plot(h, normalize(fit), 'k--')
    #
    #     try:
    #         raw_percent = get_percenatge_completed_bars("data/raw-" + server_mem + "-network-simulated-post-update.csv", xticks)
    #         plt.bar(xticks, normalize(raw_percent),  width=500, edgecolor=(0, 0, 0, 1), linewidth=0.2, alpha=0.5,
    #                 label="Raw Data " + server_mem)
    #     except:
    #         continue
    #     # h = to_hist_data(xticks, raw_percent)
    #     # fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    #     # plt.plot(h, normalize(fit), 'k--')
    #
    # plt.xlabel("Time (ms)")
    # plt.ylabel("Proportion of requests completed")
    # plt.title("Time taken to complete 100 data averaging requests (5 at a time)\n"
    #           "for various amounts of server memory")
    # # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    # plt.legend()
    # plt.tight_layout()
    #
    # plt.savefig('graphs/memory-effect-server-raw.png')
    #

    matplotlib.rc('text', usetex=True)

    plt.figure(figsize=(5, 4.8))
    server_memory = ["10", "20", "50", "100", "200"]
    bar_width = 0.3
    compute_bars = [38084.0/1000, 38966.0/1000, 30934.0/1000, 32888.0/1000, 34011.0/1000]
    compute_error = [4920.7/1000, 4914.3/1000, 4554.9/1000, 3920.7/1000, 3189.2/1000]
    compute_pos = np.arange(len(server_memory))

    raw_bars = [345922.0/1000, 206366.0/1000, 204967.0/1000, 194344.0/1000]
    raw_error = [78691.9/1000, 33470.6/1000, 51563.3/1000, 28244.3/1000]
    raw_pos = [x + bar_width for x in compute_pos[1:]]

    plt.bar(compute_pos, compute_bars, width=bar_width, color='red', edgecolor=['black']*5, yerr=compute_error, capsize=7, label='Compute aggregates\non Data Nodes')
    plt.bar(raw_pos, raw_bars, width=bar_width, color='blue', edgecolor=['black']*4, yerr=raw_error, capsize=7, label='Compute aggregate\non Central Server')

    plt.xticks([r + bar_width/2 for r in range(len(compute_bars))], server_memory)
    plt.xlabel("Server Memory (MB)", fontsize=12)
    plt.ylabel("Request Latency (s)", fontsize=12)
    plt.title("$\it{EnConsComp}$ request latency for data nodes\n"
              "with various amounts of server memory", fontsize=14)
    # server has 50% of my CPU so when nodes get x% of it they have 2x% of what the server has
    plt.legend()
    plt.tight_layout()

    plt.savefig('graphs/memory-effect-server-averaged.png', bbox_inches='tight')

    plt.figure(figsize=(5.0, 4.8))
    compute_percentages = ["2%", "5%", "10%", "20%"]
    bar_width = 0.3
    compute_bars = [516133.0/1000, 240404.0/1000, 64960.0/1000, 31041.0/1000]
    compute_error = [39614.4/1000, 20018.8/1000, 5894.8/1000, 3052.5/1000]
    compute_pos = np.arange(len(compute_percentages))

    raw_bars = [843436.0/1000, 566796.0/1000, 265503.0/1000]
    raw_error = [181738.7/1000, 54932.6/1000, 49471.6/1000]
    raw_pos = [x + bar_width for x in compute_pos[1:]]

    plt.bar(compute_pos, compute_bars, width=bar_width, color='red', edgecolor=['black']*4, yerr=compute_error, capsize=7, label='Compute aggregates\non Data Nodes')
    plt.bar(raw_pos, raw_bars, width=bar_width, color='blue', edgecolor=['black']*3, yerr=raw_error, capsize=7, label='Compute aggregate\non Central Server')

    plt.xticks([r + bar_width/2 for r in range(len(compute_bars))], compute_percentages)
    plt.xlabel("Data Node CPU power as a percentage of Server Node CPU power", fontsize=12)
    plt.ylabel("Request Latency (s)", fontsize=12)
    plt.title("$\it{EnConsComp}$ request latencies for data nodes with\n"
              "varying percentages of the server compute power", fontsize=14)
    plt.legend(bbox_to_anchor=(0.5, 0.75))
    plt.tight_layout()
    plt.savefig('graphs/cpu-effect-push-data-averaged.png', bbox_inches='tight')


    #
    # # TODO: retake data showing the memory of nodes doesn't have any effect as long as they have enough
    # memory_levels = []
    # bar_width = 0.3
    # compute_bars = []
    # compute_error = []
    # compute_pos = np.arange(len(memory_levels))
    #
    # raw_bars = [843436, 566796, 265503]
    # raw_error = [181738.7, 54932.6, 49471.6]
    # raw_pos = [x + bar_width for x in compute_pos[1:]]
    #
    # plt.bar(compute_pos, compute_bars, width=bar_width, color='red', edgecolor='black', yerr=compute_error, capsize=7,
    #         label='Compute')
    # plt.bar(raw_pos, raw_bars, width=bar_width, color='blue', edgecolor='black', yerr=raw_error, capsize=7, label='Raw')
    #
    # plt.xticks([r + bar_width for r in range(len(compute_bars))], memory_levels)
    # plt.xlabel("Percentage of server CPU power")
    # plt.ylabel("Request Latency (Ms)")
    # plt.title("Time taken to complete 100 data averaging requests (5 at a time)\n"
    #           "for data nodes with varying percentages of the server CPU power")
    # plt.legend()
    # plt.tight_layout()
    #
    # plt.savefig('graphs/memory-effect-push-data-averaged.png')


if __name__ == "__main__":
    main()
