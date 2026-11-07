
import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = []
        busy = []
        
        # Store (weight, index) of all servers
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
        
        ans = []
        time = 0

        for j, task in enumerate(tasks):

            # Actual time cannot be earlier than task arrival
            time = max(time, j)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is free, move to the next finish time
            if not available:
                time = busy[0][0]

                # Release ALL servers finishing at this time
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the server with minimum weight and index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Assign the task and calculate finishing time
            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return ans
