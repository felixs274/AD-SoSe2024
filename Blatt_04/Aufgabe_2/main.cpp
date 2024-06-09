
/*In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner entstanden.*/

#include <iostream>
#include <vector>
#include <chrono>
#include <ctime>
#include <random>

void bubbleSort(std::vector<int>& a) {
    int n = a.size();
    for (int i = 0; i < n; i++) {
        for (int j = n - 2; j >= i; j--){
            if (a[j] > a[j+1]) {
                std::swap(a[j], a[j + 1]);
            }
        }
    }
}

void preparePartition(std::vector<int>& a, int f, int l, int &p) {
// Pivot-Element
    int pivot = a[f];
    p = f - 1;
    for (int i = f; i <= l; i++) {
        if (a[i] <= pivot) {
            p++;
            std::swap(a[i], a[p]);
        }
        // Pivot an die richtige Stelle
        std::swap(a[f], a[p]);
    }
}
void quickSort(std::vector<int>& a, int f, int l) {
    int part;
    if (f < l) {
        preparePartition(a, f, l,part);
        quickSort(a, f, part - 1);
        quickSort(a, part + 1, l);
    }
}

void merge(std::vector<int>& a, int f, int l, int m) {
    int i, n = l - f + 1;
    int a1f = f, a1l = m - 1;
    int a2f = m, a2l = l;
    std::vector<int> anew(n);

    for (i = 0;i < n; i++) {
        if (a1f <= a1l) {
            if (a2f <= a2l){
                if(a[a1f] <= a[a2f]) anew[i] = a[a1f++];
                else anew[i] = a[a2f++];
            } else anew[i] = a[a1f++];
        } else anew[i] = a[a2f++];
    }
    for (i = 0; i < n; i++) a[f + i] = anew[i];
}

void mergeSort(std::vector<int>& a, int f, int l) {
    if(f < l){
        int m = (f + l + 1) / 2;
        mergeSort(a, f, m - 1);
        mergeSort(a, m, l);
        merge(a, f, l, m);
    }
}


int main() {
    int n = 7000000;       // Anzahl der zufälligen Zahlen für Merge / Quick Sort
    int j = 90000;          // Anzahl der zufälligen Zahlen für Bubble Sort

    std::vector<int> numbers_bubble(j);
    std::vector<int> numbers(n);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 10000);
    for (int i = 0; i < n; ++i) {
        if(i < j) {
            numbers_bubble[i] = dis(gen);
        }
        numbers[i] = dis(gen);
    }

    std::cout << "Start Bubble Sort: ";
    auto start_bubble = std::chrono::system_clock::now();
    std::time_t current_time = std::chrono::system_clock::to_time_t(start_bubble);
    std::cout << std::ctime(&current_time);
    bubbleSort(numbers_bubble);
    auto end_bubble = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(end_bubble);
    std::chrono::duration<double> bubble_time = end_bubble - start_bubble;
    double bubble_elements_per_minute = n * (60/bubble_time.count());
    std::cout << "Finish Bubble Sort: " <<  std::ctime(&current_time) << std::endl;

    std::cout << "Start Quick Sort: ";
    auto start_quick = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(start_quick);
    std::cout << std::ctime(&current_time);
    quickSort(numbers, 0, n - 1);
    auto end_quick = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(end_quick);
    std::chrono::duration<double> quick_time = end_quick - start_quick;
    double quick_elements_per_minute = n * (60/quick_time.count());
    std::cout << "Finish Quick Sort: " << std::ctime(&current_time) << std::endl;

    std::cout << "Start Merge Sort: ";
    auto start_merge = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(start_merge);
    std::cout << std::ctime(&current_time);
    mergeSort(numbers, 0, n - 1);
    auto end_merge = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(end_merge);
    std::chrono::duration<double> merge_time = end_merge - start_merge;
    double merge_elements_per_minute = n * (60/merge_time.count());
    std::cout << "Finish Merge Sort: " << std::ctime(&current_time) << std::endl;

    std::cout << "###########################################" << std::endl;
    std::cout << "Bubble Sort: " << int(bubble_elements_per_minute) << " Elemente / Minute\n";
    std::cout << "Quick Sort:  " <<  int(quick_elements_per_minute) << " Elemente / Minute\n";
    std::cout << "Merge Sort:  " <<  int(merge_elements_per_minute) << " Elemente / Minute\n";
    /*
     * Nur für kleine n sinnvoll: Bubble Sort: 6.29216e+06 Elemente / Minute
     * Quick Sort: 6.93809e+06 Elemente / Minute
     * Merge Sort: 4.0627e+07 Elemente / Minute
     */

    return 0;
}
