#include "lists.h"

/**
 * insert_node - inserts a node in a sorted singly linked list
 * @head: the address of the head pointer.
 * @number: the value that the node will hold.
 * Return: pointer to the created node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *ptr = NULL;

	if (head == NULL)
		return (NULL);


	node = malloc(sizeof(listint_t));
	node->n = number;

	if (node == NULL)
		return (NULL);

	if ((*head) == NULL || (*head)->n >= number)
	{
		node->next = *head;
		(*head) = node;
		return (node);
	}

	ptr = *head;

	while (ptr->next != NULL && ptr->next->n < number)
		ptr = ptr->next;

	node->next = ptr->next;
	ptr->next = node;

	return (node);
}
