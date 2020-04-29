#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function that inserts a number into a sorted singly linked ls
 * @head: head of the list
 * @number: number to be added
 *
 * Return: the address of the new node, NULL on failure
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *low;

	if (*head == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = NULL;
	new->n = number;
	low = *head;
	if (low->n >= number)
	{
		new->next = *head;
		*head = new;
		return(new);
	}
	while (low->next != NULL)
	{
		if (low->next->n >= number)
		{
			new->next = low->next;
			low->next = new;
			return (new);
		}
		low = low->next;
	}
	return (NULL);
}
