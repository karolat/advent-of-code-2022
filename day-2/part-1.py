player_1_moves_dict = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}

player_2_moves_dict = {
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
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

def determine_winner(player_1_move, player_2_move):
  if player_1_move == player_2_move:
    return 'draw'
  elif player_1_move == 'rock' and player_2_move == 'scissors':
    return 'win'
  elif player_1_move == 'rock' and player_2_move == 'paper':
    return 'loss'
  elif player_1_move == 'paper' and player_2_move == 'rock':
    return 'win'
  elif player_1_move == 'paper' and player_2_move == 'scissors':
    return 'loss'
  elif player_1_move == 'scissors' and player_2_move == 'paper':
    return 'win'
  elif player_1_move == 'scissors' and player_2_move == 'rock':
    return 'loss'

def calculate_score(outcome, move):
  score = 0
  score += outcome_scores[outcome]
  score += move_score[move]
  return score

def load_moves():
  player_1_moves = []
  player_2_moves = []
  with open('moves.txt', 'r') as moves_file:
    for line in moves_file:
      player_1_move, player_2_move = line.replace('\n', '').split(' ')
      player_1_moves.append(player_1_move)
      player_2_moves.append(player_2_move)
  return player_1_moves, player_2_moves

def main():
  # Part 1
  player_1_moves, player_2_moves = load_moves()
  player_2_score = 0
  for player_1_move, player_2_move in zip(player_1_moves, player_2_moves):
    player_1_move = player_1_moves_dict[player_1_move]
    player_2_move = player_2_moves_dict[player_2_move]
    outcome = determine_winner(player_2_move, player_1_move)
    player_2_score += calculate_score(outcome, player_2_move)
  print('Part 1, Player 2 score: {}'.format(player_2_score))

if __name__ == '__main__':
  main()