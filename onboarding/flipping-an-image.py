class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        result = [[0] * n for _ in range(n)]

        for row in range(n):
            reversed_row = image[row][::-1]
            for col in range(n):
                if reversed_row[col] == 0:
                    result[row][col] = 1
                else:
                    result[row][col] = 0

                

        return result


            

        
            
       
                
                    
