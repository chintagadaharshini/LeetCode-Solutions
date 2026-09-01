from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter cell
        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)

        # No litter to collect
        if total_litter == 0:
            return 0

        all_collected = (1 << total_litter) - 1

        # BFS state:
        # (row, col, mask, remaining_energy, moves)
        queue = deque()

        sr, sc = start
        queue.append((sr, sc, 0, energy, 0))

        # visited[(r, c, mask)] = maximum energy
        # with which we have reached this state.
        visited = {}

        visited[(sr, sc, 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need one energy to make this move
                if curr_energy == 0:
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    litter_index = litter[(nr, nc)]
                    new_mask |= (1 << litter_index)

                # Reset energy on R
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                new_moves = moves + 1

                # Have we collected everything?
                if new_mask == all_collected:
                    return new_moves

                state = (nr, nc, new_mask)

                # If we have already reached this state with
                # equal or greater energy, this path is useless.
                if state in visited and visited[state] >= new_energy:
                    continue

                visited[state] = new_energy

                queue.append(
                    (nr, nc, new_mask, new_energy, new_moves)
                )

        return -1