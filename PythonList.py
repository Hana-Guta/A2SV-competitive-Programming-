if __name__ == '__main__':
    N = int(input())  
    lst = []  

    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            position = int(command[1])
            element = int(command[2])
            lst.insert(position, element)
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            element = int(command[1])
            lst.remove(element)
        elif command[0] == 'append':
            element = int(command[1])
            lst.append(element)
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()
