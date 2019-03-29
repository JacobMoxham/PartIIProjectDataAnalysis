import subprocess
import csv

SERVER_MEMORY = 10
NUM_REQUESTS = 15
FILE_PREFIX = "raw"


def run():
    correct_output = 0

    for i in range(NUM_REQUESTS):
        proc = subprocess.Popen(["curl", "http://127.0.0.1:4000/request?startDate=2007-01-01&endDate=2007-06-30"],
                                stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        if err is None and out == b'10.60':
            correct_output += 1
        else:
            print(err)
            print(out)

    no_error_proportion = float(correct_output)/float(NUM_REQUESTS)
    print(no_error_proportion)

    filename = FILE_PREFIX + "-error-rates-large.csv"
    with open('data/' + filename, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([SERVER_MEMORY, no_error_proportion])


if __name__ == '__main__':
    run()
