class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(int)
        winners = set()
        loosers = set()
    
        for win, loss in matches:
            hash_map[loss] += 1
            if win not in hash_map:
                winners.add(win)
            
            if loss in winners:
                    winners.remove(loss)
            
            if hash_map[loss] == 1:
                loosers.add(loss)
            else:
                if loss in loosers:
                    loosers.remove(loss)
        
        winner = sorted(list(winners))
        loser = sorted(list(loosers))
         
        return [winner, loser] 