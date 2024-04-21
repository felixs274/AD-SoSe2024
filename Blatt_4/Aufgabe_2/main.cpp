#include <iostream>
#include <vector>
#include <chrono>
#include <ctime>
#include <random>

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; ++i) {
        for (int j = 0; j < n-i-1; ++j) {
            if (arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
            }
        }
    }
}

void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j <= high - 1; ++j) {
            if (arr[j] < pivot) {
                ++i;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        int pi = i + 1;

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void merge(std::vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    std::vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; ++i) {
        L[i] = arr[l + i];
    }
    for (int j = 0; j < n2; ++j) {
        R[j] = arr[m + 1 + j];
    }

    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            ++i;
        } else {
            arr[k] = R[j];
            ++j;
        }
        ++k;
    }

    while (i < n1) {
        arr[k] = L[i];
        ++i;
        ++k;
    }

    while (j < n2) {
        arr[k] = R[j];
        ++j;
        ++k;
    }
}

void mergeSort(std::vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int n = 20000000;       // Anzahl der zufälligen Zahlen für Merge / Quick Sort
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
    double bubble_rate = n / bubble_time.count();
    double bubble_elements_per_minute = bubble_rate * 60;
    std::cout << "Finish Bubble Sort: " <<  std::ctime(&current_time) << std::endl;

    std::cout << "Start Quick Sort: ";
    auto start_quick = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(start_quick);
    std::cout << std::ctime(&current_time);
    quickSort(numbers, 0, n - 1);
    auto end_quick = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(end_quick);
    std::chrono::duration<double> quick_time = end_quick - start_quick;
    double quick_rate = n / quick_time.count();
    double quick_elements_per_minute = quick_rate * 60;
    std::cout << "Finish Quick Sort: " << std::ctime(&current_time) << std::endl;

    std::cout << "Start Merge Sort: ";
    auto start_merge = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(start_merge);
    std::cout << std::ctime(&current_time);
    mergeSort(numbers, 0, n - 1);
    auto end_merge = std::chrono::system_clock::now();
    current_time = std::chrono::system_clock::to_time_t(end_merge);
    std::chrono::duration<double> merge_time = end_merge - start_merge;
    double merge_rate = n / merge_time.count();
    double merge_elements_per_minute = merge_rate * 60;
    std::cout << "Finish Merge Sort: " << std::ctime(&current_time) << std::endl;

    std::cout << "###########################################" << std::endl;
    std::cout << "Bubble Sort: " << bubble_elements_per_minute << " Elemente / Minute\n";
    std::cout << "Quick Sort: " << quick_elements_per_minute << " Elemente / Minute\n";
    std::cout << "Merge Sort: " << merge_elements_per_minute << " Elemente / Minute\n";

    return 0;
}
