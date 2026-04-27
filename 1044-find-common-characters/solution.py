class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [0] * 26
        for char in words[0]:
            min_freq[ord(char) - ord('a')] += 1
        
        for i in range(1, len(words)):
            curr_freq = [0] * 26
            for char in words[i]:
                curr_freq[ord(char) - ord('a')] += 1
            
            for j in range(26):
                min_freq[j] = min(min_freq[j], curr_freq[j])
        
        res = []
        for i in range(26):
            for _ in range(min_freq[i]):
                res.append(chr(i + ord('a')))
        
        return res

        
