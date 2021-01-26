# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count, debug=False):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.buckets = [[] for _ in range(self.bucket_count)]

        self.debug = debug
        self.debug_result = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        result = 'yes' if was_found else 'no'
        if self.debug:
            self.debug_result.append(result)
        else:
            print(result)

    def write_chain(self, chain):
        result = ' '.join(chain)
        if self.debug:
            self.debug_result.append(result)
        else:
            print(result)

    def get_debug_result(self):
        return self.debug_result

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        # print('=====', self.buckets)
        # print('=====', query.type)
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # print('check', query.ind)
            self.write_chain(reversed(self.buckets[query.ind]))

        else:
            hash_value = self._hash_func(query.s)
            # print('hash: ', hash_value)
            is_found = False
            for v in self.buckets[hash_value]:
                if v == query.s:
                    is_found = True
            # print('is_found: ', is_found)

            if query.type == 'find':
                self.write_search_result(is_found)

            elif query.type == 'add':
                if not is_found:
                    self.buckets[hash_value].append(query.s)
                    # print('append')

            else:
                if is_found:
                    self.buckets[hash_value].remove(query.s)

    def process_queries(self, queries=None):
        self.debug_result = []
        if queries is None:
            n = int(input())
            for _ in range(n):
                self.process_query(self.read_query())
        else:
            for query in queries:
                self.process_query(Query(query.split()))


def test():
    m = 5
    query_strings = [
        'add world',
        'add HellO',
        'check 4',
        'find World',
        'find world',
        'del world',
        'check 4',
        'del HellO',
        'add luck',
        'add GooD',
        'check 2',
        'del good',
    ]
    proc = QueryProcessor(m, debug=True)

    naive_result = ['HellO world', 'no', 'yes', 'HellO', 'GooD luck']
    print(f'naive: {naive_result}')

    proc.process_queries(query_strings)
    result = proc.get_debug_result()
    print(f' fast: {result}')

    assert naive_result == result
    print('OK')


def main():
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


if __name__ == '__main__':
    # test()
    main()