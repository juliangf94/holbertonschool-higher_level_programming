#include "binary_trees.h"

/**
 * binary_tree_sibling - finds the sibling of a node
 * @node: pointer to the node to find the sibling
 *
 * Return: pointer to the sibling node, or NULL if none
 */
binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{
	binary_tree_t *parent;

	if (node == NULL)
		return (NULL);

	parent = node->parent;
	if (parent == NULL)
		return (NULL);

	if (node == parent->left)
		return (parent->right);

	if (node == parent->right)
		return (parent->left);

	return (NULL);
}
