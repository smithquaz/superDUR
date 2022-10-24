/*************************************************
 * Testing the time complexity of merge sort in c
 * Function mergeSort calls merge recursively
 ************************************************/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// function prototypes
void merge(int arr[], int l, int m, int r);
void mergeSort(int arr[], int l, int r);
void printArray(int A[], int size);

int main(void){
    
    double total = 0;
    
    // repeat for 20 times (20 tests)
    for (int j = 1 ; j <= 20 ; j++){

        // define array to be sorted
        int arr1[] = {70, 50, 30, 10, 20, 40, 60, 23, 124, 33, 1544, 344, 112, 644, 11, 721, 51, 20, 40, 24, 48, 62}; 
        int arr1_size = sizeof(arr1)/sizeof(arr1[0]);

        // define random array
        int arr2[100] = {};
        int arr2_size = sizeof(arr2)/sizeof(int);

        // Initialization, should only be called once.
        srand(time(NULL));
        
        for (int i = 0 ; i < 100 ; i++){

            // Returns a pseudo-random integer between 0 and RAND_MAX.
            int r = rand() % 2000;
            arr2[i] = r;

        }

        // print initial array
        // printf("initial: ");
        // printArray(arr1, arr1_size);
        
        clock_t start, end;
        double cpu_time_used;
        
        start = clock();
        
        // algorithm to be tested
        mergeSort(arr1, 0, arr1_size - 1);
        mergeSort(arr2, 0, arr2_size - 1);

        end = clock();

        cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

        // print sorted array
        // printf("final: ");
        // printArray(arr1, arr1_size);

        // print time taken
        printf("* test %d: %.10f\n", j, cpu_time_used);
        total += cpu_time_used;

    }

    printf("* Average: %.10f\n", total / 20);

}


void merge(int arr[], int l, int m, int r){

    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
  
    /* create temp arrays */
    int L[n1], R[n2]; 
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copy the remaining elements of L[], if there 
       are any */
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    /* Copy the remaining elements of R[], if there 
       are any */
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  

/* l is for left index and r is the right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r){

    if (l < r) 
    { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        int m = l+(r-l)/2; 
  
        // Sort first and second halves 
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 


void printArray(int A[], int size){

    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 

} 