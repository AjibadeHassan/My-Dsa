class Solution:
    def pathExistenceQueries(self, nodeTot_: int, nums_: list[int], maxDiff_: int, queries_: list[list[int]]) -> list[int]:
        kMax2Exp = 18
        
        # Associate values with original indices to track them after sorting
        nodes = [(val, idx) for idx, val in enumerate(nums_)]
        nodes.sort()  # Sorts primarily by value
        
        # Map original index to its new position in the sorted array
        posSorted = [0] * nodeTot_
        for j, (val, idx) in enumerate(nodes):
            posSorted[idx] = j
            
        # Determine the farthest reachable node moving right via valid steps
        reach = [-1] * nodeTot_
        reach[nodeTot_ - 1] = nodeTot_ - 1
        for j in range(nodeTot_ - 2, -1, -1):
            if nodes[j + 1][0] - nodes[j][0] <= maxDiff_:
                reach[j] = reach[j + 1]
            else:
                reach[j] = j
                
        # Precompute the maximum 1-step jump for each node
        gJumps = [[0] * kMax2Exp for _ in range(nodeTot_)]
        left = 0
        for right in range(nodeTot_):
            while nodes[right][0] - nodes[left][0] > maxDiff_:
                gJumps[left][0] = right - 1
                left += 1
        while left < nodeTot_:
            gJumps[left][0] = nodeTot_ - 1
            left += 1
            
        # Build the sparse table for jump distances of powers of 2
        for k in range(1, kMax2Exp):
            for j in range(nodeTot_ - 1, -1, -1):
                gJumps[j][k] = gJumps[gJumps[j][k - 1]][k - 1]
                
        ans = []
        for query_ in queries_:
            # Translate original query indices into the sorted domain
            leftIdx = posSorted[query_[0]]
            rightIdx = posSorted[query_[1]]
            
            # Always traverse left to right in the sorted array
            if leftIdx > rightIdx:
                leftIdx, rightIdx = rightIdx, leftIdx
                
            if leftIdx == rightIdx:
                ans.append(0)
                continue
                
            # Target is unreachable from the starting node
            if reach[leftIdx] < rightIdx:
                ans.append(-1)
                continue
                
            # Find minimum jumps to reach or exceed target using binary lifting
            jmp = 0
            for k in range(kMax2Exp - 1, -1, -1):
                # If taking 2^k jumps keeps us strictly before the target, take it
                if gJumps[leftIdx][k] < rightIdx:
                    leftIdx = gJumps[leftIdx][k]
                    jmp |= (1 << k)
                    
            # Because we already confirmed reachability using the `reach` array, we know
            # exactly 1 more jump will securely land on or past 'rightIdx'.
            ans.append(jmp + 1)
            
        return ans
