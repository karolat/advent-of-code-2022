player_1_moves_dict = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}

required_outcome_dict = {
  'X': 'loss',
  'Y': 'draw',
  'Z': 'win'
}

outcome_scores = {
  'win': 6,
  'draw': 3,
  'loss': 0
}

move_score = {
  'rock': 1,
  'paper': 2,
  'scissors': 3
}

def determine_move(player_1_move, outcome):
  if outcome == 'win':
    if player_1_move == 'rock':
      return 'paper'
    elif player_1_move == 'paper':
      return 'scissors'
    elif player_1_move == 'scissors':
      return 'rock'
  elif outcome == 'draw':
    return player_1_move
  elif outcome == 'loss':
    if player_1_move == 'rock':
      return 'scissors'
    elif player_1_move == 'paper':
      return 'rock'
    elif player_1_move == 'scissors':
      return 'paper'

def calculate_score(outcome, move):
  score = 0
  score += outcome_scores[outcome]
  score += move_score[move]
  return score

def load_moves():
  player_1_moves = []
  outcomes = []
  with open('moves.txt', 'r') as moves_file:
    for line in moves_file:
      player_1_move, player_2_move = line.split(' ')
      player_1_moves.append(player_1_moves_dict[player_1_move.replace('\n', '')])
      outcomes.append(required_outcome_dict[player_2_move.replace('\n', '')])
  return player_1_moves, outcomes

def main():
  # Part 2
  player_1_moves, outcomes = load_moves()
  player_2_score = 0
  for player_1_move, outcome in zip(player_1_moves, outcomes):
    player_2_move = determine_move(player_1_move, outcome)
    player_2_score += calculate_score(outcome, player_2_move)
  print(f'Part 2, Player 2 score: {player_2_score}')

if __name__ == '__main__':
  main()