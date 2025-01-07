def linear_search(arr, target):
    """
    Perform a linear search for the target in the given list.

    Parameters:
    arr (list): The list to search through.
    target (int/str): The element to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Taking input from the user
input_list = input("Enter the elements of the list separated by space: ").split()
target = input("Enter the element to search for: ")

# Perform linear search
result = linear_search(input_list, target)

# Display the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")