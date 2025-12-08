#include "binary_trees.h"
#include <stdlib.h>

/**
* binary_tree_node - creates a new node
* @parent: pointer to the parent node
* @value: integer value stocked in the node
* Return: pointer to the new node if success, NULL if failure
*/
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node;

	new_node = malloc(sizeof(binary_tree_t));
	if (new_node == NULL)
	    return (NULL);
  new_node->parent = parent;
	new_node->n = value;
	new_node->left = NULL;
	new_node->right = NULL;
	return (new_node);
}