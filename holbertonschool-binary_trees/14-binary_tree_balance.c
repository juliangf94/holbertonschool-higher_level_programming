#include "binary_trees.h"

/**
 * height - measures the height of a binary tree
 * @tree: pointer to the root node
 *
 * Return: height of the tree
 */
static size_t height(const binary_tree_t *tree)
{
	size_t hl, hr;

	if (tree == NULL)
		return (0);

	hl = height(tree->left);
	hr = height(tree->right);

	if (hl > hr)
		return (hl + 1);

	return (hr + 1);
}

/**
 * binary_tree_balance - measures the balance factor of a binary tree
 * @tree: pointer to the root node
 *
 * Return: balance factor, 0 if tree is NULL
 */
int binary_tree_balance(const binary_tree_t *tree)
{
	if (tree == NULL)
		return (0);

	return ((int)height(tree->left) - (int)height(tree->right));
}
