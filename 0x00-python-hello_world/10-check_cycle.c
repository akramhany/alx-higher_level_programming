#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* check_cycle - checks if a singly linked list contains a cycle or not
* @list: the head of the list.
* Return: 0 if no, 1 if yes.
*/
int check_cycle(listint_t *list)
{
	listint_t *begin = list;
	listint_t *end = list;
	listint_t *ptr = NULL;

	if (!list)
		return (0);

	ptr = list;

	while (ptr != NULL)
	{
		if (checkVisited(begin, end, ptr) == 1)
		{
			return (1);
		}
		end = ptr;
		ptr = ptr->next;
	}

	return (0);
}

/**
 * checkVisited - takes the start and end and check if the node was visited
 * @begin: the start node.
 * @end: the end node.
 * @target: the node to search for.
 * Return: 1 if it was visited, 0 if not.
 */
int checkVisited(listint_t *begin, listint_t *end, listint_t *target)
{
	listint_t *ptr = begin;

	while (ptr != end)
	{
		if (ptr == target)
			return (1);
		ptr = ptr->next;
	}

	return (0);
}
