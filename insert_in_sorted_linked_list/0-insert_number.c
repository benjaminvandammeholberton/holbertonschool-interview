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
    listint_t *current, *new_node;
    current = *head;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = number;
    if (*head == NULL || number < current->n)
    {
        new_node->next = current;
        *head = new_node;
        return new_node;
    }
    else
    {
        while (current->next != NULL && number > current->next->n)
            current = current->next;

        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}
