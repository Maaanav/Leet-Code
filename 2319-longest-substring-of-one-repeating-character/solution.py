class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegmentTree(s)
        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, len(s) - 1, idx, char)
            ans.append(tree.get_max_len())

        return ans

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree = [None] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def _merge(self, left_node, right_node, mid_char_match: bool):
        left_max, left_pref, left_suff, left_size = left_node
        right_max, right_pref, right_suff, right_size = right_node

        parent_max = max(left_max, right_max)
        parent_pref = left_pref
        parent_suff = right_suff
        parent_size = left_size + right_size

        if mid_char_match:
            parent_max = max(parent_max, left_suff + right_pref)
            
            if left_pref == left_size:
                parent_pref = left_size + right_pref
                
            if right_suff == right_size:
                parent_suff = right_size + left_suff

        return (parent_max, parent_pref, parent_suff, parent_size)

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = (1, 1, 1, 1)
            return

        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        
        match = (self.s[mid] == self.s[mid + 1])
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1], match)

    def update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.s[idx] = char
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, char)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, char)

        match = (self.s[mid] == self.s[mid + 1])
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1], match)

    def get_max_len(self) -> int:
        return self.tree[1][0]
