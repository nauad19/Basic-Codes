#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the linked list
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// --- Conversion Function ---

/**
 * @brief Converts a circular linked list into a singly linked list.
 * The operation is done in-place.
 * @param head The head of the circular linked list.
 * @return Node* The head of the new singly linked list (same as the input head).
 */
Node* circularToSingly(Node* head) {
    // Check for an empty list
    if (head == NULL) {
        return NULL;
    }

    // 1. Find the last node (tail) of the circular list.
    // The tail is the node whose 'next' pointer points back to 'head'.
    Node* current = head;
    while (current->next != head) {
        current = current->next;
    }

    // 2. Perform the conversion.
    // Set the 'next' pointer of the tail node to NULL.
    // This breaks the circular link.
    current->next = NULL;

    // The head remains the same
    return head;
}

// --- Display Functions ---

/**
 * @brief Prints the elements of a circular linked list.
 */
void displayCircularList(Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* current = head;
    do {
        printf("%d -> ", current->data);
        current = current->next;
    } while (current != head);

    printf("... (back to %d)\n", head->data);
}

/**
 * @brief Prints the elements of a standard singly linked list.
 */
void displaySinglyList(Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// --- Main Driver Program ---
int main() {

    // 1. Create a Circular Linked List (10 -> 20 -> 30 -> 10)
    printf("--- Initial Circular List ---\n");
    Node* head = createNode(10);
    Node* second = createNode(20);
    Node* third = createNode(30);

    head->next = second;
    second->next = third;
    third->next = head; // Make it circular

    printf("Before Conversion: ");
    displayCircularList(head);

    // 2. Convert the Circular List to a Singly List
    printf("\n--- Converting List ---\n");
    Node* singlyHead = circularToSingly(head);

    // 3. Display the Singly Linked List
    printf("After Conversion: ");
    displaySinglyList(singlyHead);

    // 4. Cleanup (Only need to free the singly list now)
    Node* current = singlyHead;
    Node* temp;
    while(current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }

    return 0;
}
