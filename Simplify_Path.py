class Solution:
    def simplifyPath(self, path: str) -> str:
      
        paths = path.split('/')
        stack = []
      
        for path in paths:
            if path != "" and path != ".." and path !=".":
                stack.append(path)
            if path == ".." and len(stack) > 0:
                stack.pop()
        print(stack)
        return "/"+"/".join(st)

