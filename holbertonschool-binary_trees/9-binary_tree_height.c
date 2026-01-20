#include "binary_trees.h"

/**
* binary_tree_height - measures the height of a binary tree
* @tree: pointer to the root node of the tree to measure
* Return: height of the tree, 0 if tree is NULL
*/

size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t hl, hr;

	if (tree == NULL)
		return (0);

	if (tree->left == NULL && tree->right == NULL)
		return (0);

	hl = binary_tree_height(tree->left);
	hr = binary_tree_height(tree->right);

	if (hl > hr)
		return (hl + 1);

	return (hr + 1);
}
