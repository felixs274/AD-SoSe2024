// In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Felix Scholzen, Daniel Heisig entstanden

#include <iostream>
//AVL-Baum nach dem Einfügen: 1 2 3 4 5 6 8 9 10 11 12 13 14 15 16 
//AVL-Baum nach dem Löschen: 1 2 9 10 11 13 16 

using namespace std;

struct AVLNode {
    int key;
    AVLNode* left;
    AVLNode* right;
    int height;
};

int height(AVLNode* node) {
    if (node == nullptr)
        return 0;
    return node->height;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

AVLNode* newNode(int key) {
    AVLNode* node = new AVLNode();
    node->key = key;
    node->left = nullptr;
    node->right = nullptr;
    node->height = 1;
    return node;
}

AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;

    // Rotation durchführen
    x->right = y;
    y->left = T2;

    // Höhen aktualisieren
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    return x;
}

AVLNode* leftRotate(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* T2 = y->left;

    // Rotation durchführen
    y->left = x;
    x->right = T2;

    // Höhen aktualisieren
    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

int getBalance(AVLNode* node) {
    if (node == nullptr)
        return 0;
    return height(node->left) - height(node->right);
}

AVLNode* insert(AVLNode* node, int key) {
    // Normales BST-Einfügen
    if (node == nullptr)
        return newNode(key);

    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else // Duplikate sind nicht erlaubt
        return node;

    // Höhe des aktuellen Knotens aktualisieren
    node->height = 1 + max(height(node->left), height(node->right));

    // Balance-Faktor erhalten
    int balance = getBalance(node);

    // Unausgeglichene Knoten behandeln

    // Links-Links Fall
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    // Rechts-Rechts Fall
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    // Links-Rechts Fall
    if (balance > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Rechts-Links Fall
    if (balance < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    // Ausgeglichener Baum
    return node;
}

AVLNode* minValueNode(AVLNode* node) {
    AVLNode* current = node;
    while (current->left != nullptr)
        current = current->left;
    return current;
}

AVLNode* deleteNode(AVLNode* root, int key) {
    // BST-Löschvorgang
    if (root == nullptr)
        return root;

    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        // Knoten mit einem oder keinem Kind
        if ((root->left == nullptr) || (root->right == nullptr)) {
            AVLNode* temp = root->left ? root->left : root->right;

            // Kein Kind Fall
            if (temp == nullptr) {
                temp = root;
                root = nullptr;
            } else // Ein Kind Fall
                *root = *temp;
            delete temp;
        } else {
            // Knoten mit zwei Kindern: Den Inorder-Nachfolger finden (kleinster im rechten Teilbaum)
            AVLNode* temp = minValueNode(root->right);

            // Inorder-Nachfolger kopieren
            root->key = temp->key;

            // Den Inorder-Nachfolger im rechten Teilbaum löschen
            root->right = deleteNode(root->right, temp->key);
        }
    }

    // Wenn der Baum nur einen Knoten hatte
    if (root == nullptr)
        return root;

    // Die Höhe des aktuellen Knotens aktualisieren
    root->height = 1 + max(height(root->left), height(root->right));

    // Balance-Faktor des Knotens abrufen
    int balance = getBalance(root);

    // Unausgeglichene Knoten behandeln

    // Links-Links Fall
    if (balance > 1 && getBalance(root->left) >= 0)
        return rightRotate(root);

    // Links-Rechts Fall
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }

    // Rechts-Rechts Fall
    if (balance < -1 && getBalance(root->right) <= 0)
        return leftRotate(root);

    // Rechts-Links Fall
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}

// AVL-Baum in Inorder durchlaufen
void inorder(AVLNode* root) {
    if (root != nullptr) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
    }
}

// Hauptfunktion
int main() {
    AVLNode* root = nullptr;

    // Werte in genannter Reihenfolge einfügen
    int insertValues[] = {5, 6, 9, 12, 13, 3, 8, 10, 11, 16, 15, 14, 4, 2, 1};
    int n = sizeof(insertValues) / sizeof(insertValues[0]);

    for (int i = 0; i < n; i++) {
        root = insert(root, insertValues[i]);
    }

    // AVL-Baum nach dem Einfügen ausgeben
    cout << "AVL-Baum nach dem Einfügen: ";
    inorder(root);
    cout << endl;

    // Werte in genannter Reihenfolge entfernen
    int deleteValues[] = {12, 8, 5, 4, 3, 6, 15, 14};
    n = sizeof(deleteValues) / sizeof(deleteValues[0]);

    for (int i = 0; i < n; i++) {
        root = deleteNode(root, deleteValues[i]);
    }

    // AVL-Baum nach dem Löschen ausgeben
    cout << "AVL-Baum nach dem Löschen: ";
    inorder(root);
    cout << endl;

    return 0;
}
