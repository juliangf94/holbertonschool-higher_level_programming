#include "binary_trees.h"

/**
* binary_tree_nodes - counts the nodes with at least 1 child in a tree
* @tree: pointer to the root node of the tree to count
* Return: amount of nodes that respect the case, 0 if null
*/

size_t binary_tree_nodes(const binary_tree_t *tree)
{
	size_t count = 0, cl, cr;

	if (tree == NULL)
		return (0);

	if (tree->left != NULL || tree->right != NULL)
		count = count + 1;

	cl = binary_tree_nodes(tree->left);
	cr = binary_tree_nodes(tree->right);

	count = count + cl + cr;
	return (count);
}
