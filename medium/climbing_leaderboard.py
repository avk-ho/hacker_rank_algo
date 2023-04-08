# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def climbing_leaderboard(ranked, player):
    def update_ranked(ranked, new_score):
        ranked.append(new_score)
        updated_ranked = list(set(ranked))
        updated_ranked.sort(reverse=True)

        return updated_ranked

    player_ranks = []
    for score in player:
        updated_ranked = update_ranked(ranked, score)
        player_ranks.append(updated_ranked.index(score) + 1)
        # print(player, ranked, updated_ranked)

    return player_ranks


def climbing_leaderboard2(ranked, player):
    player_ranks = []
    for score in player:
        new_rank = 1
        idx = 0
        prev_rank = ranked[idx]
        while idx < len(ranked) and score < ranked[idx]:
            if ranked[idx] < prev_rank:
                new_rank += 1

            prev_rank = ranked[idx]
            idx += 1

        if score < prev_rank:
            new_rank += 1

        ranked.insert(idx, score)
        player_ranks.append(new_rank)
        # print(ranked)

    return player_ranks


test1 = [[100, 90, 90, 80], [70, 80, 105]]  # 4 3 1
test2 = [[100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]]  # 6 4 2 1
print(climbing_leaderboard(*test1), climbing_leaderboard(*test2))
print(climbing_leaderboard2(*test1), climbing_leaderboard2(*test2))

# [100, 90, 90, 80]
# idx 0, curr 100 prev 100, nr 1,
# idx 1, curr 90, prev 100, nr 2,
# idx 2, curr 90, prev 90, nr2
# idx 3, curr 80, prev 90, nr3
# idx 4, prev 80, nr4