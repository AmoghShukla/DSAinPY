'''
Question : 56. 
Title : Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Level : Medium

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    lower: int = intervals[0][0]
    upper: int = intervals[0][1]

    Result: list[list[int]] = []

    pointer: int = 1

    while pointer <= intervals.lenght():
        if pointer == len(intervals):
            Result.append([Lower_limit, Upper_limit])  
            break      
        if intervals[pointer][0] <= Upper_limit and intervals[pointer][1] >= Upper_limit:
            Upper_limit = intervals[pointer][1]
        elif intervals[pointer][0] > Upper_limit and intervals[pointer][1] > Upper_limit:
            Result.append([Lower_limit, Upper_limit])
            Lower_limit = intervals[pointer][0]
            Upper_limit = intervals[pointer][1]
        else:
            pass
        pointer += 1
    return Result


intervals = [[4,7],[1,4]]
print(merge(intervals))