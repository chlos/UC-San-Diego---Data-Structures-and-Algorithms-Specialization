# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.update(dst_parent, src_parent)
        else:
            self.update(src_parent, dst_parent)

        return True

    def update(self, child, new_parent):
        # attach smaller-rank tree to a bigger one
        self.parents[child] = new_parent

        # update rank
        if self.ranks[child] == self.ranks[new_parent]:
            self.ranks[new_parent] += 1

        # update row counts
        self.row_counts[new_parent] += self.row_counts[child]
        self.row_counts[child] = 0

        # update max cout
        self.max_row_count = max(self.max_row_count, self.row_counts[new_parent])

    def get_parent(self, table):
        # find parent and compress path
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for _ in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()