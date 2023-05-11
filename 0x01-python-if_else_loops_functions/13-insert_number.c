#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node) {
        return NULL;
    }
    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= new_node->n) {
        new_node->next = *head;
        *head = new_node;
    }
    else {
        listint_t *current = *head;
        while (current->next != NULL && current->next->n < new_node->n) {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}
