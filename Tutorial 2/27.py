def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
nums = list(map(int, input("Enter numbers: ").split()))
sort_list(nums)
print(nums)
