class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)

        buckets = [[] for _ in range(n+1)]

        for char, freq in counts.items():
            buckets[freq].append(char)
        
        res = []
        for freq in range(n, 0, -1):
            for char in buckets[freq]:
                res.append(char * freq)
        
        return "".join(res)
