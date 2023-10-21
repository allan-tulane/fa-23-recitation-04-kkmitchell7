# CMPS 2200 Reciation 5
## Answers

**Name:** Kailen Mitchell


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

Already sorted lists:
|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  50 |               0.201 |                0.188 |
| 100 |               0.831 |                0.751 |
| 200 |               3.541 |                4.737 |
| 300 |               6.957 |                7.394 |
| 400 |              11.843 |               10.927 |
| 500 |              16.371 |               15.801 |
| 600 |              22.308 |               21.588 |
| 700 |              29.488 |               29.099 |
| 800 |              37.888 |               37.726 |


With added shuffle of the list:
|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  50 |               0.075 |                0.063 |
| 100 |               0.141 |                0.137 |
| 200 |               0.303 |                0.291 |
| 300 |               0.523 |                0.513 |
| 400 |               0.708 |                0.674 |
| 500 |               0.883 |                0.869 |
| 600 |               1.052 |                1.046 |
| 700 |               1.256 |                1.245 |
| 800 |               1.484 |                1.461 |

It seems like choosing a random pivot is always slightly faster, no matter the other varibles.

With the already sorted list, the algorithm is comparable to n^2 run time(for both fixed pivot and random pivot). When I graph the data, it follows the n^2 curve almost exactly. This makes sense since the already sorted list is our worst case run time, and quicksort has an n^2 worst case run time.

With the not sorted list, the algorithm is comparable to nlog(n) run time (for both fixed pivot and random pivot). When I graph the data, it follows this line almost exactly, although it looked more like n run time at first. This makes sense since the average case run time is more like nlog(n) for quicksort.


The run time greatly decreases when we shuffle the list vs the already sorted list. This is because with quicksort the worst case senario is that our list is already sorted. This is because we will have unbalanced arrays, aka the greater than the pivot partition of the list will be empty and we'll just be iterating through the list.


- **1c.**

Already sorted lists:
|   n |   sorted |   qsort-random-pivot |
|-----|----------|----------------------|
|  50 |    0.001 |                0.200 |
| 100 |    0.001 |                0.828 |
| 200 |    0.002 |                3.546 |
| 300 |    0.004 |                7.891 |
| 400 |    0.004 |               12.272 |
| 500 |    0.005 |               17.310 |
| 600 |    0.004 |               23.047 |
| 700 |    0.006 |               30.905 |
| 800 |    0.006 |               39.687 |



With added shuffle of the list:
|   n |   sorted |   qsort-random-pivot |
|-----|----------|----------------------|
|  50 |    0.004 |                0.090 |
| 100 |    0.008 |                0.172 |
| 200 |    0.017 |                0.374 |
| 300 |    0.025 |                0.570 |
| 400 |    0.036 |                1.008 |
| 500 |    0.047 |                1.072 |
| 600 |    0.056 |                1.272 |
| 700 |    0.066 |                1.512 |
| 800 |    0.078 |                1.798 |

The built in sorted function is much, much faster. Quicksort performs more poorly with the already sorted list, but Timsort performs better when the list is already sorted. Overall, it seems Timsort outperforms Quicksort and especially excels when a list is already sorted.