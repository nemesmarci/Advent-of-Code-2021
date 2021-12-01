def solve(window):
    with open('input.txt') as data:
        nums = list(map(int, data))

    return sum(sum(nums[i-window:i]) > sum(nums[i-window-1:i-1])
               for i in range(window, len(nums)))
