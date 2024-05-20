MAX = 5

def depth_first_search(adj, visited, start):
    stack = []
    print(start, end=" ")

    visited[start] = 1
    stack.append(start)

    while stack:
        start = stack[-1]
        found = False
        for i in range(MAX):
            if adj[start][i] and visited[i] == 0:
                stack.append(i)
                print(i, end=" ")
                visited[i] = 1
                found = True
                break
        if not found:
            stack.pop()

adj = [[0] * MAX for _ in range(MAX)]
visited = [0] * MAX

print("Enter the adjacency matrix:")
for i in range(MAX):
    adj[i] = list(map(int, input().split()))

print("DFS Traversal:", end=" ")
depth_first_search(adj, visited, 0)
print()
