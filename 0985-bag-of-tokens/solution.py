class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        curr_score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                curr_score += 1
                left += 1
                max_score = max(curr_score, max_score)
            elif curr_score > 0 and left < right:
                power += tokens[right]
                curr_score -= 1
                right -= 1
            else:
                break

        return max_score 
