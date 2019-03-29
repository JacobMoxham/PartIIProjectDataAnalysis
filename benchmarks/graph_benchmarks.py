import csv
import matplotlib.pyplot as plt
import numpy as np


def main():
    database_records = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                        2000, 3000, 4000, 5000, 8000, 10000, 15000, 20000, 25000]
    fig = plt.figure(figsize=(10, 10))
    time_graph = fig.add_subplot(3, 1, 1)
    allocs_graph = fig.add_subplot(3, 1, 2)
    bytes_graph = fig.add_subplot(3, 1, 3)

    for file_ending in ['no-mware', 'no-caching', 'caching']:
        ns_per_op = []
        allocs_per_op = []
        allocated_bytes_per_op = []

        with open('data/read-benchmarks-' + file_ending + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                ns_per_op.append(float(row[0])/1000000)
                allocs_per_op.append(float(row[1])/1000)
                allocated_bytes_per_op.append(float(row[2])/1000000)

        time_graph.plot(database_records, ns_per_op, label=' '.join(file_ending.split('-')))
        allocs_graph.plot(database_records, allocs_per_op, label=' '.join(file_ending.split('-')))
        bytes_graph.plot(database_records, allocated_bytes_per_op, label=' '.join(file_ending.split('-')))

    time_graph.set_title("Time taken for database queries reading\n"
                         "different numbers of records with and without PAM")
    time_graph.set_xlabel("Number of records")
    time_graph.set_ylabel("Time (ms)")

    allocs_graph.set_title("Memory allocations during database queries reading\n"
                           "different numbers of records with and without PAM")
    allocs_graph.set_xlabel("Number of records")
    allocs_graph.set_ylabel("Memory allocations\n"
                            "(1000s)")

    bytes_graph.set_title("Bytes Allocated during database queries reading\n"
                          "different numbers of records with and without PAM")
    bytes_graph.set_xlabel("Number of records")
    bytes_graph.set_ylabel("Memory allocated (MB)")

    fig.set_tight_layout({"pad": 1.0, "h_pad": 1.0, "w_pad": 0.2, "rect": [0, 0.05, 1, 1]})
    plt.tight_layout()

    # Put a legend below current axis
    fig.legend(loc='lower center', ncol=3, bbox_to_anchor=(0.5, 0))
    plt.savefig("graphs/benchmark-database-read.png")


if __name__ == '__main__':
    main()