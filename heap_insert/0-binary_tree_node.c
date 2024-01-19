#include "binary_trees.h"
#include <stdlib.h>

/**
 * *binary_tree_node - Create a new binary tree node
 *
 * @parent: pointer to the parent node of the new node created
 * @value: the integer value to be store to the new node
 *
 * Return: A pointer to the newly created binary tree node, or
 * NULL if memory allocation fails.
 */
heap_t *binary_tree_node(heap_t *parent, int value)
{
	heap_t *new_node;

	new_node = malloc(sizeof(heap_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->parent = parent;
	new_node->n = value;
	new_node->left = NULL;
	new_node->right = NULL;
	return (new_node);
}
