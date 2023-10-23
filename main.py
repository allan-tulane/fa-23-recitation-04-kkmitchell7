import random, time
import tabulate
import random
# random.seed(42)  # for repeatability


def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        l = list(filter(lambda x: x < pivot, a[1:]))  # O(|a|) work, O(log|a|) span
        r = list(filter(lambda x: x >= pivot, a[1:]))  # O(|a|) work, O(log|a|) span
        return qsort(l,pivot_fn) + [pivot] + qsort(r,pivot_fn)

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def selection_sort(L):
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        L[0], L[m] = L[m], L[0]
        return    selection_sort(L[1:])

def return_first_in_list(a):
    return a[0]

def random_in_list(a): 
    return random.choice(a)

def qsort_fixed_pivot(l):
    return qsort(l, return_first_in_list)
def qsort_random_pivot(l):
   return qsort(l, random_in_list)

def compare_sort(sizes=[50, 100, 200, 300, 400,500,600,700, 800]):
    #1000, 2000, 5000, 10000, 20000, 50000, 100000
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    #tim_sort = #
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(selection_sort, mylist),
            time_search(qsort_random_pivot, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'selection sort', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())


random.seed()
test_print()



