# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
        else:
            self.name = None

    def __repr__(self):
        if self.name is not None:
            return f'"{self.type}: {self.number} {self.name}"'
        else:
            return f'"{self.type}: {self.number}"'


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            # otherwise, just add it
            else:
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)

    return result


def main():
    write_responses(process_queries(read_queries()))


def test():
    queries_list = [
        'add 911 police',
        'add 76213 Mom',
        'add 17239 Bob',
        'find 76213',
        'find 910',
        'find 911',
        'del 910',
        'del 911',
        'find 911',
        'find 76213',
        'add 76213 daddy',
        'find 76213',
    ]

    queries = [Query(q_str.split()) for q_str in queries_list]
    print(queries)
    result_naive = process_queries_naive(queries)
    print(result_naive)

    queries = [Query(q_str.split()) for q_str in queries_list]
    print(queries)
    result = process_queries(queries)
    print(result)

    assert result_naive == result
    print('OK')


if __name__ == '__main__':
    # test()
    main()