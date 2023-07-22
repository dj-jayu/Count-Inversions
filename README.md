# Count-Inversions
Implementation of an algorithm that counts the number of inversions in an array in O(n*log(n)) time, and O(n) space complexity.

It's a simple modification of merge sort.

When merging, we not only merge the two arrays in sorted order, but also count the inversions between them.

An inversion occurs when an element from the right array is chosen. The number of inversions is then the number of elements remaining in the left array (because they should have come before the right element).

The number list is read from a text file and passed to an array.
