import time
import random


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start_time = time.time()  
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1  
    return found, time.time() - start_time  

def ordered_sequential_search(a_list, item):
    start_time = time.time() 
    pos = 0
    found = False
    a_list.sort()  

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            break  
        pos += 1  

    return found, time.time() - start_time  

def binary_search_iterative(a_list, item):
    start_time = time.time()  
    low = 0
    high = len(a_list) - 1
    found = False
    a_list.sort()  

    while low <= high and not found:
        mid = (low + high) // 2
        if a_list[mid] == item:
            found = True
        elif a_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return found, time.time() - start_time  

def binary_search_recursive(a_list, item, low, high):
    start_time = time.time()  
    if low > high:
        end_time = time.time()  
        return False, end_time - start_time  

    mid = (low + high) // 2
    if a_list[mid] == item:
        end_time = time.time()  
        return True, end_time - start_time  
    elif a_list[mid] < item:
        return binary_search_recursive(a_list, item, mid + 1, high)
    else:
        return binary_search_recursive(a_list, item, low, mid - 1)

if __name__ == "__main__":
    """Main entry point"""
    sizes = [500, 1000, 5000]  

    for the_size in sizes:  
        total_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist.sort()  

            start = time.time()
            check, _ = binary_search_iterative(mylist, 99999999)
            time_spent = time.time() - start
            total_time += time_spent

        avg_time = total_time / 100
        print(f"{the_size} ")
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average ")

      
        total_seq_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            start = time.time()
            check, time_spent = sequential_search(mylist, 99999999)
            total_seq_time += time_spent

        avg_seq_time = total_seq_time / 100
        print(f"Sequential Search took {avg_seq_time:10.7f} seconds to run, on average ")

        total_ordered_seq_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist.sort()  # Ensure the list is sorted
            start = time.time()
            check, time_spent = ordered_sequential_search(mylist, 99999999)
            total_ordered_seq_time += time_spent

        avg_ordered_seq_time = total_ordered_seq_time / 100
        print(f"Ordered Sequential Search took {avg_ordered_seq_time:10.7f} seconds to run, on average ")

        total_bin_recur_time = 0
        for i in range(100):
            mylist = get_me_random_list(the_size)
            mylist.sort()  # Ensure the list is sorted
            start = time.time()
            check, time_spent = binary_search_recursive(mylist, 99999999, 0, len(mylist) - 1)
            total_bin_recur_time += time_spent

        avg_bin_recur_time = total_bin_recur_time / 100
        print(f"Binary Search Recursive took {avg_bin_recur_time:10.7f} seconds to run, on average ")
