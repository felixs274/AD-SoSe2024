#include <stdio.h>
#include <stdlib.h>
#include <time.h>


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
    clock_t start = clock();
    qsort(items, n, sizeof(Item), compare);
    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity <= 0) break;
        double amount = items[i].weight < capacity ? items[i].weight : capacity;
        totalValue += amount * (items[i].value / items[i].weight);
        capacity -= amount;
    }
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Laufzeit (Anteilig): %.6f Sekunden\n", time_spent);
    return totalValue;
}


int ganzzahlig(Item items[], int n, int capacity) {
    clock_t start = clock();
    int **dp = malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = malloc((capacity + 1) * sizeof(int));
    }

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
    int result = dp[n][capacity];

    for (int i = 0; i <= n; i++) {
        free(dp[i]);
    }
    free(dp);

    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Laufzeit (Ganzzahlig): %.6f Sekunden\n", time_spent);

    return result;
}


Item* generateItems(int n) {
    Item* items = malloc(n * sizeof(Item));
    if (items == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        items[i].value = (rand() % 200) + 1;
        items[i].weight = (rand() % 50) + 1;
    }
    return items;
}


int main() {
    int n_items = 100000;
    int capacity = 5000;

    Item* items = generateItems(n_items);
    
    double max_value_anteilig = anteilig(items, n_items, capacity);
    printf("Maximaler Wert im Rucksack (Anteilig): %.2f\n", max_value_anteilig);

    int max_value_ganzzahlig = ganzzahlig(items, n_items, capacity);
    printf("Maximaler Wert im Rucksack (Ganzzahlig): %d\n", max_value_ganzzahlig);

    free(items);
    return 0;
}


/*

---=== LAUFZEITEN ===---

Anteilig: 
O(n log n), da qsort 

Ganzzahlig:
O(n * W), wegen der (n+1) * (W+1) Tabelle



---=== VARIANTE 2 SCHLECHTER AUF DAUER ===---

Output fuer:
    int n_items = 100000;
    int capacity = 5000;


Laufzeit (Anteilig): 0.014742 Sekunden
Maximaler Wert im Rucksack (Anteilig): 428775.00

Laufzeit (Ganzzahlig): 2.483765 Sekunden
Maximaler Wert im Rucksack (Ganzzahlig): 428775

*/