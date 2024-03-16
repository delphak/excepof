def check_winner(board):
  """
  Checks if there is a winner in the given board.

  Args:
    board: A list of lists representing the game board.

  Returns:
    The winner, if there is one. Otherwise, returns None.
  """

  # Check rows for a winner.
  for row in board:
    if len(set(row)) == 1 and row[0] != 0:
      return row[0]

  # Check columns for a winner.
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != 0:
      return column[0]

  # Check diagonals for a winner.
  diagonal1 = [board[i][i] for i in range(len(board))]
  if len(set(diagonal1)) == 1 and diagonal1[0] != 0:
    return diagonal1[0]

  diagonal2 = [board[i][len(board) - i - 1] for i in range(len(board))]
  if len(set(diagonal2)) == 1 and diagonal2[0] != 0:
    return diagonal2[0]

  # No winner yet.
  return None
