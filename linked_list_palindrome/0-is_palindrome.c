#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int is_palindrome(listint_t **head)
{
	int length = 0;
	int *array;
	int i = 0;
	int j;
	listint_t *temp = *head;

	if (!*head)
	{
		return (1);
	}
	while (temp != NULL)
	{
		length += 1;
		temp = temp->next;
	}
	array = (int *)malloc(length * sizeof(int));
	if (!array)
		return 0;
	while (*head != NULL)
	{
		array[i] = (*head)->n;
		*head = (*head)->next;
		i++;
	}
	j = length - 1;
	for (i = 0; i < length - 1 / 2; i++)
	{
		if (array[i] != array[j])
			return (0);
		j--;
	}
	return 1;
}
