import matplotlib
import csv
import matplotlib.pyplot as plt
import numpy as np


def plot_with_error_bars(fig, file_prefix,file_endings, labels, action, column):
    database_records = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                        2000, 3000, 4000, 5000, 8000, 10000, 15000, 20000, 25000]
    bytes_graph = fig.add_subplot(3, 2, 4+column)
    time_graph = fig.add_subplot(3, 2, column, sharex=bytes_graph)
    allocs_graph = fig.add_subplot(3, 2, 2+column, sharex=bytes_graph)

    colours = ['blue', 'orangered', 'green']

    for i, file_ending in enumerate(file_endings):
        ns_per_op = []
        allocs_per_op = []
        allocated_bytes_per_op = []
        ns_erros = []
        allocs_errors = []
        bytes_errors = []

        with open(file_prefix + file_ending + '-mean-error.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                ns_per_op.append(float(row[0]) / 1000000)
                ns_erros.append(float(row[1]) / 1000000)

                allocs_per_op.append(float(row[2]) / 1000)
                allocs_errors.append(float(row[3]) / 1000)

                allocated_bytes_per_op.append(float(row[4]) / 1000000)
                bytes_errors.append(float(row[5]) / 1000000)

        time_graph.errorbar(database_records, ns_per_op, label=labels[i], yerr=ns_erros,
                            ecolor='grey', capsize=2, color=colours[i])
        allocs_graph.errorbar(database_records, allocs_per_op, label=labels[i],
                              yerr=allocs_errors, ecolor='grey', capsize=2, color=colours[i])
        bytes_graph.errorbar(database_records, allocated_bytes_per_op, label=labels[i],
                             yerr=bytes_errors, ecolor='grey', capsize=2, color=colours[i])

    # time_graph.set_title("Time taken for database queries " + action + "\n"
    #                      "different numbers of records with and without PAM")
    # time_graph.set_xlabel("Number of records")
    plt.setp(time_graph.get_xticklabels(), visible=False)
    if column == 1:
        time_graph.set_ylabel("Time (ms)", fontsize=12)

    # allocs_graph.set_title("Memory allocations during database queries " + action + "\n"
    #                        "different numbers of records with and without PAM")
    # allocs_graph.set_xlabel("Number of records")
    plt.setp(allocs_graph.get_xticklabels(), visible=False)
    if column == 1:
        allocs_graph.set_ylabel("Memory allocations\n"
                                "(1000s)", fontsize=14)

    # bytes_graph.set_title("Bytes Allocated during database queries " + action + "\n"
    #                       "different numbers of records with and without PAM")
    bytes_graph.set_xlabel("Number of records", fontsize=14)
    if column == 1:
        bytes_graph.set_ylabel("Memory allocated (MB)", fontsize=14)
    bytes_graph.set_xbound(0, 25000)

    # Put a legend below current axis
    if column == 1:
        bytes_graph.legend(loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.3), fontsize=10)
    if column == 2:
        bytes_graph.legend(loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.3), fontsize=10)


def calculate_mean_and_error_bars(file_prefix, file_endings):
    for file_ending in file_endings:
        ns_collections = [[] for _ in range(19)]
        allocs_collections = [[] for _ in range(19)]
        bytes_collections = [[] for _ in range(19)]

        with open(file_prefix + file_ending + '-collection.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            i = 0
            j = 0
            for row in csv_reader:
                if i == 0:
                    j += 1
                (ns_collections[i]).append(float(row[0]))

                allocs_collections[i].append(float(row[1]))

                bytes_collections[i].append(float(row[2]))

                i = (i+1) % 19
            print(str(j) + " runs completed")

            ns_per_op = [np.mean(l) for l in ns_collections]
            allocs_per_op = [np.mean(l) for l in allocs_collections]
            allocated_bytes_per_op = [np.mean(l) for l in bytes_collections]
            ns_erros = [np.std(l) for l in ns_collections]
            allocs_errors = [np.std(l) for l in allocs_collections]
            bytes_errors = [np.std(l) for l in bytes_collections]

            with open(file_prefix + file_ending + '-mean-error.csv', 'w') as out_file:
                csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(len(ns_per_op)):
                    csv_writer.writerow([ns_per_op[i], ns_erros[i],
                                         allocs_per_op[i], allocs_errors[i],
                                         allocated_bytes_per_op[i], bytes_errors[i]])


def main():
    matplotlib.rc('text', usetex=True)

    fig = plt.figure(figsize=(10, 10))
    fig.suptitle("Duration, number of memory allocations and bytes allocated during database queries\n"
                 " reading (left) and writing (right)"
                 " different number of records with and without PAM", fontsize=16)

    calculate_mean_and_error_bars('data/read-benchmarks-', ['no-mware', 'no-caching', 'caching'])
    plot_with_error_bars(fig, 'data/read-benchmarks-', ['no-mware', 'no-caching', 'caching'],
                         ['Without PAM', 'With PAM (no caching)', 'With PAM (caching)'], 'reading', 1)

    calculate_mean_and_error_bars('data/write-benchmarks-', ['no-mware', 'mware'])
    plot_with_error_bars(fig, 'data/write-benchmarks-', ['no-mware', 'mware'], ['Without PAM', 'With PAM'], 'writing', 2)

    fig.set_tight_layout({"pad": 1.0, "h_pad": 1.0, "w_pad": 0.2, "rect": [0, 0.03, 1, 0.95]})
    plt.tight_layout()

    plt.savefig("graphs/read-write-mean-errors.png")


if __name__ == '__main__':
    main()