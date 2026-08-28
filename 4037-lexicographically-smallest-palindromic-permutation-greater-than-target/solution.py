class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        counts = Counter(s)

        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""

        freq = {ch: cnt // 2 for ch, cnt in counts.items()}

        def build_palindrome(first_half: List[str]) -> str:
            left = "".join(first_half)
            right = left[::-1]
            return left + mid_char + right
        
        first_half = []
        curr_freq = freq.copy()
        matched_pos = 0

        while matched_pos < half_len:
            ch = target[matched_pos]
            if curr_freq.get(ch, 0) > 0:
                first_half.append(ch)
                curr_freq[ch] -= 1
                matched_pos += 1
            else:
                break
        
        if matched_pos == half_len:
            candidate = build_palindrome(first_half)
            if candidate > target:
                return candidate
        
        for pos in range(matched_pos, -1, -1):
            if pos < len(first_half):
                char_to_restore = first_half.pop()
                curr_freq[char_to_restore] = curr_freq.get(char_to_restore, 0) + 1
            
            target_char = target[pos]

            pivot_char = None
            for ch_code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if curr_freq.get(ch, 0) > 0:
                    pivot_char = ch
                    break

            if pivot_char:
                res_half = first_half + [pivot_char]
                curr_freq[pivot_char] -= 1

                for ch_code in range(ord('a'), ord('z') + 1):
                    ch = chr(ch_code)
                    if curr_freq.get(ch, 0) > 0:
                        res_half.extend([ch] * curr_freq[ch])

                return build_palindrome(res_half) 

        return ""
