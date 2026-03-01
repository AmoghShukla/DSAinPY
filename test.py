def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    Lower_limit = intervals[0][0]
    Upper_limit = intervals[0][1]
    Output : list[list[int]] = []
    pointer = 1
    while pointer <= len(intervals):
        if pointer == len(intervals):
            Output.append([Lower_limit, Upper_limit])  
            break      
        if intervals[pointer][0] <= Upper_limit and intervals[pointer][1] >= Upper_limit:
            Upper_limit = intervals[pointer][1]
        elif intervals[pointer][0] > Upper_limit and intervals[pointer][1] > Upper_limit:
            Output.append([Lower_limit, Upper_limit])
            Lower_limit = intervals[pointer][0]
            Upper_limit = intervals[pointer][1]
        else:
            pass
        pointer += 1
    return Output

intervals = [[4, 7],[1, 4]]
print(merge(intervals))
