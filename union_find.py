
class UnionFind:
    def __init__(self, num_members):
        self.arr = list(range(num_members))

    def union(self, left, right):
        lparent = self.find(left)
        rparent = self.find(right)

        self.arr[lparent] = rparent

    def find(self, member):
        path = [member]

        cur = member
        while cur != self.arr[cur]:
            cur = self.arr[cur]
            path.append(cur)

        for member in path:
            self.arr[member] = cur

        return cur


test_uf = UnionFind(10)
test_uf.union(1, 9)
test_uf.union(2, 4)
test_uf.union(3, 7)
assert(test_uf.find(3) == 7)
assert(test_uf.find(2) == 4)
assert(test_uf.find(1) == 9)
test_uf.union(3, 2)
assert(test_uf.find(2) == 4)
assert(test_uf.find(3) == 4)
assert(test_uf.find(4) == 4)
