#include "lists.h"
#include <stdlib.h>

/**
 * listint_t *insert_node - inserts a number
 * into a sorted singly linked list
 * @head: points to the head of the list
 * @number: number to insert
 * Return: the adress of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp, *new;

    tmp = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;

    if (*head == NULL)
    {
        *head = new;
        return (new);
    }

    while (tmp->next && tmp->next->n < number)
        tmp = tmp->next;
    if (tmp != *head)
    {
        new->next = tmp->next;
        tmp->next = new;
    }
    else
    {
        new->next = tmp;
        *head = new;
    }
    return (new);
}
