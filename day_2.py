from re import A


plan = None
with open('input-2.txt','r') as file:
    plan = file.readlines()

def get_points(adversary,mine):
    translate = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors', 
        'X': 'rock', 
        'Y': 'paper', 
        'Z': 'scissors', 
    }
    points = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
    }
    adversary = translate.get(adversary)
    mine = translate.get(mine)
    if adversary == mine :
        #draw
        return 3 + points.get(mine)
    elif adversary == 'rock' and mine == 'paper':
        #win
        return 6 + points.get(mine)
    elif adversary == 'scissors' and mine == 'rock':
        #win
        return 6 + points.get(mine)
    elif adversary == 'paper' and mine == 'scissors':
        #win
        return 6 + points.get(mine)
    else:
         return points.get(mine)
    
def compute_plan(plan):
    total_points = 0
    for game in plan:
        game_list = game.split()
        adversary = game_list[0]
        mine = game_list[1]
        points = get_points_2(adversary,mine)
        total_points += points
    return total_points

plan_ex = [
'A Y',
'B X',
'C Z',
]


def get_points_2(adversary,target):
    translate = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors', 
        'X': 'lose', 
        'Y': 'draw', 
        'Z': 'win', 
    }
    points = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
    }
    win = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock',
    }
    lose = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    }
    adversary = translate.get(adversary)
    target = translate.get(target)
    if target == 'draw':
        return 3 + points.get(adversary)
    elif target == 'win':
        #win
        winner_move = win.get(adversary)
        return 6 + points.get(winner_move)
    elif target == 'lose':
        loser_move = lose.get(adversary)
        return points.get(loser_move)
    
print(compute_plan(plan))