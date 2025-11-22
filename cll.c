#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the circular linked list
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
    newNode->next = NULL; // Will be set later to make it circular
    return newNode;
}

/**
 * @brief Joins two circular linked lists into a single circular list.
 * * @param head1 The head of the first circular linked list.
 * @param head2 The head of the second circular linked list.
 * @return Node* The head of the new, combined circular linked list (head1).
 */
Node* joinCircularLists(Node* head1, Node* head2) {
    // If one list is empty, return the other one.
    if (head1 == NULL) {
        return head2;
    }
    if (head2 == NULL) {
        return head1;
    }

    // 1. Find the last node of the first list.
    // The last node is the one whose 'next' pointer points back to head1.
    Node* tail1 = head1;
    while (tail1->next != head1) {
        tail1 = tail1->next;
    }

    // 2. Find the last node of the second list.
    // The last node is the one whose 'next' pointer points back to head2.
    Node* tail2 = head2;
    while (tail2->next != head2) {
        tail2 = tail2->next;
    }

    // --- The Joining Logic ---

    // 3. Last node of List 1 (tail1) points to the head of List 2 (head2).
    // This breaks the circularity of List 1.
    tail1->next = head2;

    // 4. Last node of List 2 (tail2) points to the head of the new combined list (head1).
    // This completes the circularity of the combined list.
    tail2->next = head1;

    // Return the head of the combined list
    return head1;
}

/**
 * @brief Prints the elements of a circular linked list starting from the head.
 * * @param head The head of the circular linked list.
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

    // Print the final link back to the head to show it's circular
    printf("... (back to %d)\n", head->data);
}

// Function to free the memory of the circular list
void freeCircularList(Node* head) {
    if (head == NULL) {
        return;
    }

    Node* current = head->next;
    Node* temp;

    // Traverse and free all nodes until we are back at the head
    while (current != head) {
        temp = current;
        current = current->next;
        free(temp);
    }
    // Finally, free the head node
    free(head);
}


// --- Main Driver Program ---
int main() {

    // 1. Create First Circular List (List 1: 10 -> 20 -> 30 -> 10)
    printf("Creating List 1...\n");
    Node* head1 = createNode(10);
    Node* second1 = createNode(20);
    Node* third1 = createNode(30);

    head1->next = second1;
    second1->next = third1;
    third1->next = head1; // Make it circular

    printf("List 1: ");
    displayCircularList(head1);

    // 2. Create Second Circular List (List 2: 40 -> 50 -> 40)
    printf("\nCreating List 2...\n");
    Node* head2 = createNode(40);
    Node* second2 = createNode(50);

    head2->next = second2;
    second2->next = head2; // Make it circular

    printf("List 2: ");
    displayCircularList(head2);

    // 3. Join the two lists
    printf("\nJoining List 1 and List 2...\n");
    Node* combinedHead = joinCircularLists(head1, head2);

    // 4. Display the joined list
    printf("Combined List: ");
    displayCircularList(combinedHead);

    // 5. Cleanup
    freeCircularList(combinedHead);

    return 0;
}
