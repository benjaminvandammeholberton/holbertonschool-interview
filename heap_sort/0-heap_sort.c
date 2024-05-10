#include "sort.h"

/**
 * swap - Swaps two values
 * using the Heap sort algorithm
 *
 * @a: First value
 * @b: Second value
 *
 * Return: Nothing
 */
void swap(int *a, int *b)
{
	int tmp = *a;

	*a = *b;
	*b = tmp;
}

/**
 * heapify - Builds a heap from the element to be sorted
 *
 * @array: The array from which to build the heap
 * @n: The size of the array
 * @i: The index of the root node
 * @size: The size of the original array
*/
void heapify(int *array, int n, int i, size_t size)
{
	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < n && array[left] > array[largest])
		largest = left;

	if (right < n && array[right] > array[largest])
		largest = right;

	if (largest != i)
	{
		swap(&array[i], &array[largest]);
		print_array(array, size);
		heapify(array, n, largest, size);
	}
}

/**
 * heap_sort - Sorts an array of integers in  ascending order
 * using the Heap sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 *
 * Return: Nothing
 */
void heap_sort(int *array, size_t size)
{
	int i;

	for (i = size / 2 - 1; i >= 0; i--)
		heapify(array, size, i, size);

	for (i = size - 1; i > 0; i--)
	{
		swap(&array[0], &array[i]);
		print_array(array, size);
		heapify(array, i, 0, size);
	}
}
