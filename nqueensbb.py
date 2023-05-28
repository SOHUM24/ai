def solveNQueens(n):
    col = set()  
    posDiag = set() 
    negDiag = set()  
    res = []
    board = [["."] * n for i in range(n)]

   
    def heuristic(r):
        non_attacking = n - len(col)  # Number of columns available for queens
        non_attacking -= len(posDiag.intersection(range(r + 1, n + r + 1)))  # Number of positive diagonals available
        non_attacking -= len(negDiag.intersection(range(r - n, r)))  # Number of negative diagonals available
        return non_attacking

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        columns = sorted(range(n), key=lambda c: heuristic(r + 1))

        for c in columns:
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

solutions = solveNQueens(4)

for solution in solutions:
    for row in solution:
        print(" ".join(row))
    print()