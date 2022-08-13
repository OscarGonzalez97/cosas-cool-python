import sys
import time


def progress_bar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count / float(total)))
    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

for i in range(10):
    time.sleep(1)
    progress_bar(i, 10)
