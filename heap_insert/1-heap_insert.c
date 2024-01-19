#include "binary_trees.h"
#include <stdlib.h>

/**
 * heapify - Restore the max heap property by swapping with parent nodes.
 *
 * @new_node: Pointer to the newly inserted node.
 *
 * Return: Pointer to the final position of the inserted node.
 */
heap_t *heapify(heap_t *new_node)
{
    heap_t *parent;
    int temp;

    parent = new_node->parent;
    while (parent != NULL && new_node->n > parent->n)
    {
        temp = parent->n;
        parent->n = new_node->n;
        new_node->n = temp;

        new_node = parent;
        parent = new_node->parent;
    }
    return (new_node);
}

/**
 * heap_insert - Insert a value into a Max Binary Heap.
 *
 * @root: Double pointer to the root node of the heap.
 * @value: The value to be inserted.
 *
 * Return: Pointer to the created node, or NULL on failure.
 */
heap_t *heap_insert(heap_t **root, int value)
{
    heap_t *new_node, *current;

    new_node = binary_tree_node(NULL, value);
    if (new_node == NULL)
        return (NULL);

    if (*root == NULL)
    {
        *root = new_node;
        return (new_node);
    }

    current = *root;
    while (current->left != NULL && current->right != NULL)
    {
        if (value <= current->n)
            current = current->left;
        else
            current = current->right;
    }

    if (current->left == NULL)
        current->left = new_node;
    else
        current->right = new_node;

    new_node->parent = current;

    return (heapify(new_node));
}
