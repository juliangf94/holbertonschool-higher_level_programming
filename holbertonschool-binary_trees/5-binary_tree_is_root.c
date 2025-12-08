#include "binary_trees.h"
#include <stdlib.h>

/**
* binary_tree_is_root - checks if a given node is a root
* (i.e, having no parents)
* @node: pointer to the node to check
* Return: 1 if the node is a root, 0 if not
*/

int binary_tree_is_root(const binary_tree_t *node)
{
	if (node == NULL)
		return (0);

	if (node->parent == NULL)
		return (1);

	return (0);
}
