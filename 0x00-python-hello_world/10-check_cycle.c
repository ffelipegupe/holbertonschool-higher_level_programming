#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: list to check
 *
 * Return: 0, if the is no cycle; 1, if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	listint_t *back = list;
	listint_t *forth = list->next;

	if (list == NULL)
		return (0);
	while (back && forth && forth->next)
	{
		if (back == forth)
			return (1);
		forth = (forth->next)->next;
		back = back->next;
	}
	return (0);
}
