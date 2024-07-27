class Solution(object):
    def assignTasks(self, servers, tasks):
        # Empty server heap (insert according to weight and index)
        emptyServers = []
        for j in range(len(servers)):
            heappush(emptyServers, (servers[j], j))

        # Occupied server heap (insert according to free time),
        # weight and index
        occupiedServers = []

        # List with final server assignments
        serverAssignment = []

        for i in range(len(tasks)):
            # First, check if any servers are becoming free:
            while occupiedServers and occupiedServers[0][0] <= i:
                currentEndTime, currentWeight, currentServer = heappop(occupiedServers)
                heappush(emptyServers, (currentWeight, currentServer))
            
            # If there are empty servers, assign task to server:
            if emptyServers:
                currentWeight, currentServer = heappop(emptyServers)
                serverAssignment.append(currentServer)
                heappush(occupiedServers, (i + tasks[i], currentWeight, currentServer))
            
            # Otherwise, find out when first server will become empty and assign task to it
            else:
                currentEndTime, currentWeight, currentServer = heappop(occupiedServers)
                serverAssignment.append(currentServer)
                heappush(occupiedServers, (currentEndTime + tasks[i], currentWeight, currentServer))

        return serverAssignment