
# N-queens, N-Rooks and N-Knights Problem
This program solves n-queens, n-rooks and n-knights standard problems using basic search algorithm</br>
**How to run the program:**

    python board.py <problem_type> <board_size> [blocker_size] [points]
Problem Type: Could be any one of nqueen, nrook, nknight
Board Size: The size of the board you want to solve the problem for
Blocker size: Number of places where it is not allowed to keep queen, rook or knight
points:  Blocking points represented by two number `<row> <col>`
Examples:
1. N-queens for board 8: 
`python board.py nqueen 8`

3. N-queen for board 8 with 1 row and 8 col as blocker:
 `python board.py nqueen 8 1 1 8`
