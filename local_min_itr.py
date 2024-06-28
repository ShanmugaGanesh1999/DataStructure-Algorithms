def local_minimum(a) -> list:
    local_min_index, n = [], len(a)
    for i in range(0, n):
        if i == 0:
            if a[i] < a[i + 1]:
                local_min_index.append(i)
        elif i == n - 1:
            if a[i] < a[i - 1]:
                local_min_index.append(i)
        else:
            if a[i] < a[i + 1] and a[i] < a[i - 1]:
                local_min_index.append(i)
    return local_min_index


a = [6, 3, 4, 7, 9, 11]  # [1]
# a = [10, 5, 3, 2, 8, 9]  # [3]
# a = [5, 4, 3, 6, 7]  # [2]
# a = [1, 2, 3, 4, 5, 6]  # [0]
# a = [7, 6, 5, 4, 3, 2]  # [5]
# a = [8, 7, 6, 9, 10]  # [2]
# a = [4, 3, 2, 5, 6, 7]  # [2]
# a = [10, 5, 20, 15, 30, 25]  # [1, 3, 5]
# a = [1, 3, 2, 5, 4]  # [0, 2, 4]
# a = [10, 8, 6, 7, 5, 3, 4, 2]  # [2, 5, 7]

local_min_list = local_minimum(a)
print(
    f"local minimum => list: {local_min_list} & elements: {[a[i] for i in local_min_list]}"
)
