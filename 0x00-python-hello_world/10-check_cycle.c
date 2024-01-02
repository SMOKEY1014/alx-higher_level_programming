#include "list.h"

/*
 * check_cycle - checks if theres a cycling linked list.
 * @list: list to check.
 *
 * return: 1 if the list has a cycle, o if not
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
		return (1);
	}
	return (0);
}
