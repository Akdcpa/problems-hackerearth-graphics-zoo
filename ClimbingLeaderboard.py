rank = int(input())
rank_arr = list(map(int,input().split()))

player = int(input())
player_arr = list(map(int,input().split()))

# rank_arr.sort(reverse=True)

# j = 1
# index = [j]
# for i in range(1,len(rank_arr)):
#     if(rank_arr[i]==rank_arr[i-1]):
#         index.append(j)
#     else:
#         index.append(j+1)
#         j = j+1
# res = []
# def findNearest(arr,key):
#     res = []
#     for i in range(len(arr)):
#         res.append(abs())


# for i in range(player):
#     ele = player_arr[i]
#     if(ele in rank_arr):
#         res.append(index[rank_arr.index(player_arr[i])])
#     else:
#         for j in range():
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
