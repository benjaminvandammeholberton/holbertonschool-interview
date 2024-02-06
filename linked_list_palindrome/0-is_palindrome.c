#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palyndrome
 *
 * @head: pointer to pointer on the head of the singly linked list
 *
 * Return: 1 if it's a palyndrom, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int length = 0;
	listint_t *front, *end;
	listint_t *temp = *head;
	int i = 0;
	int j;

	if (!*head)
		return (1);
	while (temp != NULL)
	{
		length += 1;
		temp = temp->next;
	}
	while (i != length / 2)
	{
		front = end = *head;
		for (j = 0; j < i; j++)
			front = front->next;
		for (j = 0; j < length - (i + 1); j++)
			end = end->next;
		if (front->n != end->n)
			return (0);
		i++;
	}
	return (1);
}
