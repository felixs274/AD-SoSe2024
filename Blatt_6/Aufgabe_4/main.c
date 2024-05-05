// ###########################################################################
// # In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner #
// ###########################################################################


#include <stdio.h>
#include <stdlib.h>


typedef struct {
    double value;
    double weight;
} Item;


int compare(const void* a, const void* b) {
    double r1 = ((Item*)a)->value / ((Item*)a)->weight;
    double r2 = ((Item*)b)->value / ((Item*)b)->weight;
    return (r1 < r2) - (r1 > r2);
}


int max(int a, int b) {
    return a > b ? a : b;
}


double anteilig(Item items[], int n, double capacity) {
    qsort(items, n, sizeof(Item), compare);
    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity <= 0) break;
        double amount = items[i].weight < capacity ? items[i].weight : capacity;
        totalValue += amount * (items[i].value / items[i].weight);
        capacity -= amount;
    }
    return totalValue;
}


int ganzzahlig(Item items[], int n, int capacity) {
    int dp[n+1][capacity+1];
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (items[i-1].weight <= w)
                dp[i][w] = max(dp[i-1][w], items[i-1].value + dp[i-1][w-(int)items[i-1].weight]);
            else
                dp[i][w] = dp[i-1][w];
        }
    }
    return dp[n][capacity];
}


int main() {
    Item items[] = {{60.0, 10.0}, {100.0, 20.0}, {120.0, 30.0}};
    int n_items = sizeof(items) / sizeof(items[0]);
    int capacity = 50;

    double max_value_anteilig = anteilig(items, n_items, capacity);
    printf("Maximaler Wert im Rucksack (Anteilig): %.2f\n", max_value_anteilig);

    int max_value_ganzzahlig = ganzzahlig(items, n_items, capacity);
    printf("Maximaler Wert im Rucksack (Ganzzahlig): %d\n", max_value_ganzzahlig);

    return 0;
}
