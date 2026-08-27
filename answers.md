# CMPS 2200 Recitation 01
## Answers

**Name:**__Nahema Dumonteil__
**Name:**_________________________


Place all written answers from `recitation-01.md` here for easier grading.

- **4) (1 pts)** Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 
Linear: if it is at the end of the list or not in the list at all
Binary:All the way to the right or the left of the remaining search space, or not in the list at all
- **5) (1 pts)** Describe the best case input value of `key` for `linear_search`? for `binary_search`? 
Linear: at the beginning
Binary: the middle of the initial list
- **6) Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- **7) Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.
- **8) (1 pts)** Call `print_results(compare_search())` and paste the results here:

|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.001 |    0.002 |
|      100 |    0.002 |    0.001 |
|     1000 |    0.018 |    0.002 |
|    10000 |    0.178 |    0.002 |
|   100000 |    1.738 |    0.003 |
|  1000000 |   18.497 |    0.042 |
| 10000000 |  173.244 |    0.030 |

- **9) (1 pts)** Do the theoretical running times match your empirical results?
yes. linear search increases linearly while binary search increases at a much slower rate which matches with a logarithmic growth. 

- **10a) (1 pts)** What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? 
O(k*n)
Since a single worst case linear search of a list of n elements is O(n), then repeating it k times scales linearly O(k*n)

- **10b) (1 pts)** For binary search? 
If the list is already sorted, then it would be O(k*logn) because a single worst case is O(logn) then k times would scale it. 

- **10c) (1 pts)** For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? You may assume that your sorting algorithm runs in $O(n \lg n)$ time.

We solve the inequality nlogn + klogn < kn
and we get k>(nlogn)/(n-logn) so once k is greater than that fraction, it pays off. 