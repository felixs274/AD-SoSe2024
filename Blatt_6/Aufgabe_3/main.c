// ###########################################################################
// # In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner #
// ###########################################################################


#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct Node {
    int value;
    struct Node *next;
} Node;


Node* createRingList(int size) {
    Node *head = NULL, *current = NULL;
    for (int i = 1; i <= size; i++) {
        Node* newNode = malloc(sizeof(Node));
        newNode->value = i;
        if (head == NULL) {
            head = newNode;
        } else {
            current->next = newNode;
        }
        current = newNode;
    }
    current->next = head;  
    return head;
}


int removeNode(Node** head, int index) {
    if (*head == NULL) return -1; 
    Node *current = *head, *prev = NULL;
    if (index == 0) { 
        if ((*head)->next == *head) { 
            int value = (*head)->value;
            free(*head);
            *head = NULL;
            return value;
        } else {
            while (current->next != *head) { 
                current = current->next;
            }
            current->next = (*head)->next;
            int value = (*head)->value;
            free(*head);
            *head = current->next;
            return value;
        }
    }
    for (int i = 0; i < index; i++) {
        prev = current;
        current = current->next;
    }
    prev->next = current->next;
    int removedValue = current->value;
    free(current);
    return removedValue;
}


int main() {
    int size = 49;
    Node* head = createRingList(size);

    srand(time(NULL));
    printf("Gezogene Lottozahlen:\n");
    for (int i = 0; i < 6; i++) {
        int step = rand() % size;
        int number = removeNode(&head, step);
        printf("%d ", number);
        size--;
    }
    printf("\n");

    return 0;
}