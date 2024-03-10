def shift_edges_clockwise(matrix):
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
      if(top%2==0 or left%2==0):
        if(top==bottom):
          prev = matrix[bottom][right]
          for i in range(left, right + 1):
            matrix[top][i], prev = prev, matrix[top][i]
          break 
        else:
          if(left==right):
            prev = matrix[bottom][right]
            for i in range(top, bottom + 1):
              matrix[i][right], prev = prev, matrix[i][right]
            break;
          prev = matrix[top+1][left]
        # Dịch chuyển phần tử từ trên cùng sang phải
        for i in range(left, right + 1):
            matrix[top][i], prev = prev, matrix[top][i]

        top += 1

        # Dịch chuyển phần tử từ phải sang dưới
        for i in range(top, bottom + 1):
            matrix[i][right], prev = prev, matrix[i][right]

        right -= 1

        # Dịch chuyển phần tử từ dưới lên trái
        for i in range(right, left - 1, -1):
            matrix[bottom][i], prev = prev, matrix[bottom][i]

        bottom -= 1

        # Dịch chuyển phần tử từ trái lên trên
        for i in range(bottom, top - 1, -1):
            matrix[i][left], prev = prev, matrix[i][left]
        left += 1
      else:
        if(top==bottom):
          prev = matrix[top][left]
          for i in range(right, left-1,-1):
            matrix[top][i], prev = prev, matrix[top][i]
          break 
        else:
          if(left==right):
            prev = matrix[top][left]
            for i in range(bottom, top - 1, -1):
              matrix[i][right], prev = prev, matrix[i][right]
            break
          else:
            prev = matrix[top+1][right]


        # Dịch chuyển phần tử từ trên cùng sang phải
        for i in range(right, left-1,-1):
            matrix[top][i], prev = prev, matrix[top][i]

        top += 1

        # Dịch chuyển phần tử từ phải sang dưới
        for i in range(top, bottom + 1):
            matrix[i][left], prev = prev, matrix[i][left]

        left+= 1

        for i in range(left, right+1):
          matrix[bottom][i], prev = prev, matrix[bottom][i]

        bottom -= 1

        # Dịch chuyển phần tử từ trái lên trên
        for i in range(bottom, top - 1, -1):
            matrix[i][right], prev = prev, matrix[i][right]

        right -= 1
        # Dịch chuyển phần tử từ dưới lên trái
       
# Đọc input
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

# Thực hiện dịch chuyển
shift_edges_clockwise(matrix)

# Xuất mảng sau khi dịch chuyển
for row in matrix:
    print(*row)