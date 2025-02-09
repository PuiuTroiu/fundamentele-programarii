import pandas as pd
import time

def print_hi():
    for i in range(0,1000000000):
        i += 1
if __name__ == '__main__':
    start_time = time.time()
    print_hi()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
