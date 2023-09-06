#include "lists.h"
/**
 * new_intnode - create a new node
 * @number: the number in the new node
 * Return: a pointer to the new node
 * or NULL if failed
 */
listint_t *new_intnode(int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	return (new);
}

/**
 * insert_inplace - handle list with one node
 * @head: a pointer to the head of the list
 * @new: a pointer to the new node
 * Return: the address of the new node
 */
listint_t *insert_inplace(listint_t **head, listint_t *new)
{
	listint_t *current = *head;

	if (current->n > new->n)
	{
		*head = new;
		new->next = current;
	}
	else
	{
		current->next = new;
		new->next = NULL;
	}
	return (new);
}
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: a pointer to the head of the list
 * @number: the number to add
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *after_current;
	/* Check validation */
	if (head == NULL)
		return (NULL);
	new = new_intnode(number);
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	} /* Handle if list with one node */
	current = *head;
	if (current->next == NULL)
		return (insert_inplace(head, new));
	after_current = current->next;
	while (after_current->next != NULL)
	{
		if (after_current->n > number)
		{
			current->next = new;
			new->next = after_current;
			return (new);
		}
		current = current->next;
		after_current = after_current->next;
	} /* When get out of the loop means reached the end of it */
	if (after_current->n > number)
	{
		current->next = new;
		new->next = after_current;
	}
	else
	{
		after_current->next = new;
		new->next = NULL;
	}
	return (new);
}
