class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Can i not just start on the right, tracking largest seen so far and moving left while adding the index ot the list

        result = []

        largest = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > largest:
                result.append(i)
                largest = heights[i]


        result.reverse()
        return result