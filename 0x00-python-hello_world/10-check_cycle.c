#include "lists.h"

/**
 * check_cycle - checks if the linked list has a cycle
 * @list: linked list
 * Return: 1 if cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (!list)
		return (0);

	while (list && temp && temp->next)
	{
		temp = temp->next->next;
		list = list->next;
		if (list == temp)
			return (1);
	}
	return (0);
}
