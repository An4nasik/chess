from pprint import pprint


def res(size, row, board, results):
    if row == size:
        results.append(board.copy())
        return
    for col in range(size):
        if check_the_place(row, col, board):
            board[row] = col
            res(size, row + 1, board, results)
            board[row] = -1


def check_the_place(row, col, board):
    for i in range(row):
        if board[i] == col or (board[i] - i == col - row) or (board[i] + i == col + row):
            return False
    return True



def find_all_res(size):
    results = []
    board = [-1] * size
    res(size, 0, board, results)
    return results


ans = find_all_res(8)
z = []
for x in ans:
    c = list([lambda y: 7 - y for y in x])
    if x not in z and x[::-1] not in z and c not in z:
        z.append(x)
for a in z:
    desk = [["_"] * 8 for x in range(8)]
    for i in range(8):
        desk[i][a[i]] = "Q"
    print(a)
    pprint(desk)
print(len(z))