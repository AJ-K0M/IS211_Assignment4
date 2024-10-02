import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    return time.time() - start_time

def shellSort(a_list):
    start_time = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    return time.time() - start_time

def gapInsertionSort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        currentvalue = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > currentvalue:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = currentvalue

def python_sort(a_list):
    start_time = time.time()
    sorted_list = sorted(a_list)
    return time.time() - start_time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare sorting algorithms")
    parser.add_argument("--sizes", nargs='+', type=int, default=[500, 1000, 5000], help="List sizes to sort")
    parser.add_argument("--iterations", type=int, default=100, help="Number of iterations for each list size")
    args = parser.parse_args()

    list_sizes = args.sizes
    iterations = args.iterations

    for the_size in list_sizes:
        # Python sort
        total_time = 0
        for i in range(iterations):
            mylist = get_me_random_list(the_size)
            total_time += python_sort(mylist)
        avg_time = total_time / iterations
        print(f"{the_size} ")
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average ")

        # Insertion sort
        total_time = 0
        for i in range(iterations):
            mylist = get_me_random_list(the_size)
            total_time += insertion_sort(mylist)
        avg_time = total_time / iterations
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average ")

        # Shell sort
        total_time = 0
        for i in range(iterations):
            mylist = get_me_random_list(the_size)
            total_time += shellSort(mylist)
        avg_time = total_time / iterations
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average ")
