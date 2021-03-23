trie = {}
    i = 0
    for index, q in queries:
        x, m = q
        while i < len(nums) and nums[i] <= m:
            num = nums[i]
            cur = trie
            for j in range(31, -1, -1):
                cur_bit = (num >> j) & 1
                cur.setdefault(cur_bit, {})
                cur = cur[cur_bit]
            i += 1