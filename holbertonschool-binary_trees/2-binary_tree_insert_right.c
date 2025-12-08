#include "binary_trees.h"
#include <stdlib.h>

/**
* binary_tree_insert_right - inserts a node as the right-child of another node
* @parent: pointer to the parent tree
* @value: integer, value of the new node
* Return: pointer to the created node, NULL if failure or if parent is NULL
*/

binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node, *temp;

	if (parent == NULL)
		return (NULL);

	new_node = malloc(sizeof(binary_tree_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = value;
	new_node->left = NULL;
	new_node->parent = parent;
	new_node->right = NULL;

	if (parent->right != NULL)
	{
		temp = parent->right;
		new_node->right = temp;
		temp->parent = new_node;
	}

	parent->right = new_node;
	return (new_node);
}
