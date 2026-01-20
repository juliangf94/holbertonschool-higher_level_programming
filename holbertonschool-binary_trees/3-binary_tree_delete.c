#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_delete - Deletes an entire binary tree
 * @tree: a pointer to the root node of the tree to delete
 *
 * This function performs a post-order traversal (Left -> Right -> Root)
 * to ensure that all child nodes are freed before the parent node.
 */
void binary_tree_delete(binary_tree_t *tree)
{
	if (tree == NULL)
		return;
	binary_tree_delete(tree->left);
	binary_tree_delete(tree->right);
	free(tree);
}
