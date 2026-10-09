#Example 1
#Input: 
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]



class Solution:
    def findRestaurant(self, list1, list2):
        min_sum = float("inf")
        result = []

        for x in list1:
            if x in list2:
                index_sum = list1.index(x) + list2.index(x)

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [x]
                elif index_sum == min_sum:
                    result.append(x)

        return result
    
    
    
#Example 2
#Input:
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
 
class Solution:
    def findRestaurant(self, list1, list2):
        min_sum = float("inf")
        result = []

        for x in list1:
            if x in list2:
                index_list1 = list1.index(x)
                index_list2 = list2.index(x)
                index_sum = index_list1 + index_list2

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [x]
                elif index_sum == min_sum:
                    result.append(x)

        return result

#Example 3
#Input: 
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

class Solution:
    def findRestaurant(self, list1, list2):
        min_sum = float("inf")
        result = []

        for x in list1:
            if x in list2:
                index_list1 = list1.index(x)
                index_list2 = list2.index(x)
                index_sum = index_list1 + index_list2

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [x]
                elif index_sum == min_sum:
                    result.append(x)
        return result