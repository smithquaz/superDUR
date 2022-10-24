def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2  # Finding the mid of the array
        left = unsorted_array[:mid]  # Dividing the array elements
        right = unsorted_array[mid:]  # into 2 halves

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1


# Code to print the list
def print_list(array1):
    for i in range(len(array1)):
        print(array1[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    
    total = 0
    
    for j in range(1, 21):
    
        array1 = [70, 50, 30, 10, 20, 40, 60, 23, 124, 33, 1544, 344, 112, 644, 11, 721, 51, 20, 40, 24, 48, 62]
        array2 = []

        import random

        # create random array of size 100
        for i in range(100):
            array2.append(random.randint(0, 2000))
        
        # print initial array
        # print("Given array1 is", end="\n")
        # print_list(array1)
        
        from timeit import default_timer as timer

        start = timer()

        # calls merge sort
        merge_sort(array1)
        merge_sort(array2)

        # print sorted array
        # print("Sorted array1 is: ", end="\n")
        # print_list(array1)

        end = timer()

        # print time taken
        output = "{:.10f}".format(float(end - start))
        print(f'* test {j}: {output}')
        total += float(output)

    print(f'* Average: {"{:.10f}".format(float(total / 20))}')