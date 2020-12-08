rank = int(input())
rank_arr = list(map(int,input().split()))

player = int(input())
player_arr = list(map(int,input().split()))

def climbingLeaderboard(ranked, player): 
    scores = sorted(list(set(ranked)), reverse=True)
    player_ranks = []
    for score in player:
        while scores and score >= scores[-1]:
            scores.pop()
        player_ranks.append(len(scores) + 1)

    return player_ranks
res = climbingLeaderboard(rank_arr,player_arr)
print(res)
