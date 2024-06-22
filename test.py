def find_unique(nums):
    start = 0
    end = len(nums) - 1  # Corrected end index
    
    # Check if the array is rotated
    if nums[start] > nums[end]:  # Check if the array is rotated
        boolvalue = True
    else:
        boolvalue = False

    # Binary search loop to find the unique element
    while start <= end:
        mid = start + (end - start) // 2  # Calculate mid index
        
        # Check if mid is the unique element
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        
        # Determine the direction to search
        if boolvalue:
            if nums[mid] > nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[mid] > nums[mid + 1]:
                end = mid - 1
            else:
                start = mid + 1
    
    return None  # If no unique element is found

# Example usage:
nums = [6, 7, 8, 1, 1, 2, 3, 4, 4, 5, 5]
print(find_unique(nums))
