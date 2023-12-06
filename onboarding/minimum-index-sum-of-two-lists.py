class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic_t = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dic_t[list1[i]] = i+j
        arr=[]
        for i,j in dic_t.items():
            if j == min(dic_t.values()):
                arr.append(i)
        return arr