// In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Felix Scholzen, Daniel Heisig entstanden

#include <iostream>
// Laufzeitkomplexität:
// Einfügen (iterativ oder rekursiv): Durchschnitt O(log n), im schlimmsten Fall O(n) (bei unbalancierten Bäumen)
// Suche (iterativ): Durchschnitt O(log n), im schlimmsten Fall O(n) (bei unbalancierten Bäumen)
// Löschen (rekursiv): Durchschnitt O(log n), im schlimmsten Fall O(n) (bei unbalancierten Bäumen)

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BST {
private:
    TreeNode* root;

    TreeNode* insertRec(TreeNode* root, int val) {
        if (root == nullptr)
            return new TreeNode(val);
        
        if (val < root->val)
            root->left = insertRec(root->left, val);
        else if (val > root->val)
            root->right = insertRec(root->right, val);
        
        return root;
    }

    TreeNode* minValueNode(TreeNode* node) {
        TreeNode* current = node;
        while (current && current->left != nullptr)
            current = current->left;
        return current;
    }

    TreeNode* deleteRec(TreeNode* root, int val) {
        if (root == nullptr)
            return root;

        if (val < root->val)
            root->left = deleteRec(root->left, val);
        else if (val > root->val)
            root->right = deleteRec(root->right, val);
        else {
            if (root->left == nullptr) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr) {
                TreeNode* temp = root->left;
                delete root;
                return temp;
            }

            TreeNode* temp = minValueNode(root->right);
            root->val = temp->val;
            root->right = deleteRec(root->right, temp->val);
        }
        return root;
    }

public:
    BST() : root(nullptr) {}

    void insert(int val) {
        root = insertRec(root, val);
    }

    bool search(int val) {
        TreeNode* current = root;
        while (current != nullptr) {
            if (val == current->val)
                return true;
            else if (val < current->val)
                current = current->left;
            else
                current = current->right;
        }
        return false;
    }

    void remove(int val) {
        root = deleteRec(root, val);
    }
};

int main() {
    BST tree;
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);

    std::cout << "Search 20: " << (tree.search(20) ? "Found" : "Not found") << std::endl;
    std::cout << "Search 90: " << (tree.search(90) ? "Found" : "Not found") << std::endl;

    tree.remove(20);
    std::cout << "Search 20 after deletion: " << (tree.search(20) ? "Found" : "Not found") << std::endl;

    return 0;
}
