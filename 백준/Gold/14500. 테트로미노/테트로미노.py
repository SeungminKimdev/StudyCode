import sys
input = sys.stdin.readline

def main():
    n, m = map(int,input().split())
    paper = {}
    for i in range(n):
        paper[i] = list(map(int,input().split()))
    tetris=[[(0,0),(0,1),(0,2),(0,3)],\
        [(0,0),(1,0),(2,0),(3,0)],\
        [(0,0),(1,0),(0,1),(1,1)],\
        [(0,0),(1,0),(2,0),(2,1)],\
        [(0,1),(1,1),(2,1),(2,0)],\
        [(0,0),(0,1),(1,1),(2,1)],\
        [(0,0),(0,1),(1,0),(2,0)],\
        [(0,0),(1,0),(1,1),(1,2)],\
        [(0,2),(1,1),(1,2),(1,0)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,1),(1,1),(1,0),(2,0)],\
        [(1,0),(1,1),(0,1),(0,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,1),(1,0),(1,1),(1,2)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,1),(1,1),(1,0),(2,1)]]
    answer = 0
    for i in range(n):
        for j in range(m):
            for t in tetris:
                try:
                    tempSum = paper[i+t[0][0]][j+t[0][1]]+paper[i+t[1][0]][j+t[1][1]]+paper[i+t[2][0]][j+t[2][1]]+paper[i+t[3][0]][j+t[3][1]]
                    answer = max(answer,tempSum)
                except:
                    continue
    print(answer)
    return

if __name__ == '__main__':
    main()