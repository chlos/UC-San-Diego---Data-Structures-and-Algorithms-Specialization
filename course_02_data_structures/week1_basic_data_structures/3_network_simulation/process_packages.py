# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

DROP = True
NOT_DROP = False


class Buffer:
    def __init__(self, size):
        self.size = size
        self.buffer = deque()

    def process(self, request):
        # buffer is empty: server is ready to serve the request
        if not self.buffer:
            self.buffer.append(request.arrived_at + request.time_to_process)
            return Response(NOT_DROP, request.arrived_at)

        # buffer cleanup: rm oldest (served) reqs
        while self.buffer and self.buffer[0] <= request.arrived_at:
            self.buffer.popleft()

        # buffer is full: drop the req
        if len(self.buffer) >= self.size:
            return Response(DROP, -1)

        # put req to the buffer
        if not self.buffer:
            self.buffer.append(request.arrived_at + request.time_to_process)
            return Response(NOT_DROP, request.arrived_at)
        else:
            server_ready_time = self.buffer[-1]
            self.buffer.append(server_ready_time + request.time_to_process)
            return Response(NOT_DROP, server_ready_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
