class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
       
        diagonal = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
               diagonal[i+j].append(mat[i][j])

        print(diagonal)
        
        flag = 0
        ans = []

        for key in diagonal.keys():
            if flag % 2 == 1: 
                ans += diagonal[key]
            else: 
                ans += diagonal[key][::-1]
            flag += 1

        return ans

            
                
            
        





    





                    
