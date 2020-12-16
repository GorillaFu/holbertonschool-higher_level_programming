#include "lists.h"

/**
 * flip - flips linked list
 * @h: linked list
 * Return: reversed list
 */
listint_t *flip(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*h)
	{
		next = (*h)->next;
		(*h)->next = prev;
		prev = *h;
		*h = next;
	}
	*h = prev;
	return (*h);
}

/**
 * is_palindrome - reverses linked list
 * @h: Linked list
 * Return: reversed list
 */
int is_palindrome(listint_t **head)
{
	listint_t *list1 = *head;
	listint_t *list2 = *head;
	listint_t *temp = NULL;

	if (!*head)
		return (1);
	while (list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;
	}
	if (list2)
		list1 = list1->next;
	list2 = *head;
	temp = flip(&list1);
	while (list1)
	{
		if (list2->n != list1->n)
		{
			flip(&temp);
			return (0);
		}
		list2 = list2->next;
		list1 = list1->next;
	}
	flip(&temp);
	return (1);
}
