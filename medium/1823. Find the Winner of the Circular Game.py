class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        friends = [x + 1 for x in range(n)]
        start_pos = 0

        while len(friends) > 1:
            start_pos = (start_pos + k - 1) % len(friends)
            friends.pop(start_pos)

        return friends[0]
