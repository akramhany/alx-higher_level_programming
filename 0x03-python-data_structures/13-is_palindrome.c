#include "lists.h"

/**
 * is_palindrome - takes a linked list and check if it is palindrome or not
 * @head: pointer to the head pointer of the list.
 * Return: 1 if its palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int isPal = is_pal_rec(&ptr, ptr);

	return (isPal);
}


/**
 * is_pal_rec - a function that determines if a list is pal using recursion.
 * @forwardPtr: address of the pointer to the head of the list.
 * @backwardPtr: pointer to the head of the list.
 * Return: 1 if the list is pal, 0 if not
 */
int is_pal_rec(listint_t **forwardPtr, listint_t *backwardPtr)
{
	int isPal = 0;

	if (!backwardPtr)
		return (1);

	isPal = is_pal_rec(forwardPtr, backwardPtr->next);

	if (isPal == 1)
	{
		if ((*forwardPtr)->n == backwardPtr->n)
		{
			(*forwardPtr) = (*forwardPtr)->next;
			return (1);
		}
		return (0);
	}

	return (0);
}
