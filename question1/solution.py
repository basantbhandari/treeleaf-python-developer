def merge_count_split_inv(left, right):
    i = j = count = 0
    merged = []
    len_left = len(left)

    while i < len_left and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len_left - i  # All remaining elements in left[] are greater than right[j]
            j += 1

        # Early exit if count exceeds 1,000,000,000
        if count > 1000000000:
            return count, []

    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return count, merged


def sort_and_count(arr):
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr) // 2
    left_count, left_sorted = sort_and_count(arr[:mid])
    right_count, right_sorted = sort_and_count(arr[mid:])

    split_count, sorted_arr = merge_count_split_inv(left_sorted, right_sorted)

    total_count = left_count + right_count + split_count

    # Early exit if total count exceeds 1,000,000,000
    if total_count > 1000000000:
        return total_count, []

    return total_count, sorted_arr


def solution(A):
    inversion_count, _ = sort_and_count(A)

    if inversion_count > 1000000000:
        return -1
    else:
        return inversion_count


# Example Usage
A = [-1, 6, 3, 4, 7, 4]
print(solution(A))  # Output: 4
