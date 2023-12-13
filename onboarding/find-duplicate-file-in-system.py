class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content_map = {} 

        for path in paths:
            tokens = path.split()
            directory = tokens[0]
            files = tokens[1:]

            for file in files:
                file_tokens = file.split('(')
                file_name = file_tokens[0]
                file_content = file_tokens[1][:-1] 

                full_path = directory + '/' + file_name

                if file_content in content_map:
                    content_map[file_content].append(full_path)
                else:
                    content_map[file_content] = [full_path]

      
        result = [group for group in content_map.values() if len(group) > 1]

        return result



            