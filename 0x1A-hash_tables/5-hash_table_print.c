#include "hash_tables.h"

/**
 * hash_table_print - Print as a dictionary obj
 * @ht: Hash Table
 * Return: void
 */

void hash_table_print(const hash_table_t *ht)
{

	unsigned int i = 0;
	int count = 0;
	char dict[1024] = "";
	hash_node_t *temp;

	if (!ht)
		return;

	while (index < ht->size)
	{
		if (ht->array[i] != NULL)
		{
			temp = ht->array[i];
			while (temp != NULL)
			{
				if (count != 0)
					strcat(dict, ", ");
				strcat(dict, "'");
				strcat(dict, temp->key);
				strcat(dict, "': '");
				strcat(dict, temp->value);
				strcat(dict, "'");
				temp = temp->next;
				count++;
			}
		}
		i++;
	}
	printf("{%s}\n", dict);
}
