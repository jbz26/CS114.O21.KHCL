import sys

def count_stars(image):
    rows, cols = len(image), len(image[0])
    visited = [[False] * cols for _ in range(rows)]
    star_count = 0

    def dfs(i, j):
        nonlocal visited
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or image[i][j] == '#':
          #print("out " ,i,j)  
          return


        visited[i][j] = True

        # Duyệt các điểm xung quanh (trái, phải, trên, dưới)
        if j > 0:
          dfs(i, j - 1)
        if j < cols - 1:
            dfs(i, j + 1)
        if i > 0:
            dfs(i - 1, j)
        if i < rows - 1:
            dfs(i + 1, j)

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and image[i][j] == '-':
                star_count += 1
                #print(i,j)
                dfs(i, j)

    return star_count

# Đọc input
test_cases = 1
while True:
  try:
    m, n = map(int, input().split())
   
    # do something with line
    image = [input().strip() for _ in range(m)]
    # Gọi hàm đếm số ngôi sao và in kết quả
    result = count_stars(image)
    print(f"Case {test_cases}: {result}")
    test_cases+=1
  except EOFError:
    break