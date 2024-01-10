#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

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
    listint_t *current;
    listint_t *new;

    current = *head;

    if (number == NULL)
        return NULL;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    if (*head == NULL)
    {
        new->next = NULL;
        *head = new;
    }
    else
    {
        while (number > current->next->n || current->next == NULL)
            current = current->next;
        new->next = current->next;
        current->next = new;
    }
    return (new);
}
