#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - Inserts a new node with a given number into a
 * sorted linked list.
 *
 * @head: A pointer to the head of the linked list.
 * @number: The value to be inserted into the linked list.
 *
 * Return: A pointer to the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current, *new;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return NULL;

    new->n = number;

    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
        return (new);
    }
    else if ((*head)->n > number)
    {
        new->next = *head;
        *head = new;
        return (new);
    }
    else
    {
        while (current->next != NULL && number > current->next->n)
            current = current->next;
        new->next = current->next;
        current->next = new;
    }
    return (new);
}
