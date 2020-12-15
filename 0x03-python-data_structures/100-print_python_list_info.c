#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about a Python list
 * @list: pointer of Python object
 * Returns: void
 */


void print_python_list_info(PyObject *list)
{
	int length;
	int i;
	PyObject *list2;

	length = PyList_Size(list);
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)list)->allocated);
	for (i = 0; i < length; i++)
	{
		list2 = PyList_GetItem(list, i);
		printf("Element %d: %s\n", i, Py_TYPE(list2)->tp_name);
	}
}
