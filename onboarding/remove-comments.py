class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment = False
        result = []
        stg = ""

        for line in source: 
            i = 0
            while i < len(line):
                if line[i:i+2] == "//" and not comment:
                    break

                elif line[i:i+2] == "/*" : 
                    if not comment:
                        comment = True
                        i += 1

                elif line[i:i+2] == "*/" and comment:
                    comment = False
                    i += 1

                elif not comment:
                    stg += line[i]

                i += 1

            if not comment and  stg:
                result.append(stg)
                stg = ""
                
        return result


               



        