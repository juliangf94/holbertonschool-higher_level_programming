#include "binary_trees.h"

/**
* binary_tree_uncle - finds the uncle of a node
* @node: pointer to the node to find the uncle
* Return: pointer to the uncle node, NULL if node is NULL or no uncle
*/

binary_tree_t *binary_tree_uncle(binary_tree_t *node)
{
	binary_tree_t *parent, *grandparent;

	if (node == NULL)
		return (NULL);

	parent = node->parent;
	if (parent == NULL)
		return (NULL);

	grandparent = parent->parent;
	if (grandparent == NULL)
		return (NULL);

	if (parent == grandparent->left)
		return (grandparent->right);

	if (parent == grandparent->right)
		return (grandparent->left);

	return (NULL);
}
