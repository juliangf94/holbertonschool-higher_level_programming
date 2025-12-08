#include "binary_trees.h"
#include <stdlib.h>

/**
* binary_tree_insert_left - inserts a node as the left-child of another node
* @parent: pointer to the parent tree
* @value: integer, value of the new node
* Return: pointer to the created node, NULL if failure or if parent is NULL
*/

binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node, *temp;

	if (parent == NULL)
		return (NULL);

	new_node = malloc(sizeof(binary_tree_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = value;
	new_node->right = NULL;
	new_node->parent = parent;
	new_node->left = NULL;

	if (parent->left != NULL)
	{
		temp = parent->left;
		new_node->left = temp;
		temp->parent = new_node;
	}

	parent->left = new_node;
	return (new_node);
}
