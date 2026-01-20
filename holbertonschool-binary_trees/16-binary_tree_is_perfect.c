#include "binary_trees.h"

/**
 * get_depth - Calculates the depth of the leftmost leaf in the tree.
 * The depth of the root node is 0.
 *
 * @tree: A pointer to the root node.
 * Return: The depth of the leftmost leaf.
 */
static int get_depth(const binary_tree_t *tree)
{
	int depth = 0;

	while (tree && tree->left)
	{
		depth++;
		tree = tree->left;
	}
	return (depth);
}

/**
 * is_perfect_recursive_helper - Recursively checks if the tree is perfect.
 * It ensures the tree is full and all leaves are at the expected depth.
 *
 * @tree: A pointer to the current node.
 * @depth: The expected depth (level) of all leaves
 * (calculated from the leftmost leaf).
 * @level: The current level of the node, starting at 0 for the root.
 * Return: 1 if the node and its subtree are perfect, 0 otherwise.
 */
static int is_perfect_recursive_helper(const binary_tree_t *tree,
		int depth, int level)
{
	if (tree->left == NULL && tree->right == NULL)
		return (depth == level);
	if (tree->left == NULL || tree->right == NULL)
	{
		return (0);
	}
	return (is_perfect_recursive_helper(tree->left, depth, level + 1)
			&& is_perfect_recursive_helper(tree->right, depth, level + 1));
}

/**
 * binary_tree_is_perfect - Checks if a binary tree is perfect.
 *
 * @tree: A pointer to the root node of the tree to check.
 * Return: 1 if the tree is perfect, 0 otherwise (including if tree is NULL).
 */
int binary_tree_is_perfect(const binary_tree_t *tree)
{
	int depth;

	if (tree == NULL)
		return (0);
	depth = get_depth(tree);
	return (is_perfect_recursive_helper(tree, depth, 0));
}
