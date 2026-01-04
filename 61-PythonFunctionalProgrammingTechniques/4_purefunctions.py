def bubble_sort(data: list[int]) -> list[int]:
    sorted_data = data.copy()  # copy the data to ensure immutability
    n = len(sorted_data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                swapped = True
        if not swapped:
            break
    return sorted_data


def quick_sort(data: list[int]) -> list[int]:
    match data:
        case []:
            return []
        case [x]: 
            return [x] # Instead of returning data, return a new list with the single element
        case _:
            pivot = data[-1]
            greater = [item for item in data[:-1] if item > pivot]
            lesser = [item for item in data[:-1] if item <= pivot]
            return quick_sort(lesser) + [pivot] + quick_sort(greater)


def do_operations(data: list[int]) -> list[int]:
    transformed_data = [item * 2 + 10 for item in data]
    return bubble_sort(transformed_data)

# Same input, same output, no side effects - Use copies of data to avoid mutation
# Print statements removed to avoid side effects
def main() -> None:
    data = [1, 5, 3, 4, 2]

    print(f"Data before sorting: {data}")
    result = do_operations(data)
    print(f"Result after sorting: {result}")


if __name__ == "__main__":
    main()