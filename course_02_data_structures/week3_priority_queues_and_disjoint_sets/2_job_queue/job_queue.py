# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker():
    def __init__(self, id, next_free_time):
        self.id = id
        self.next_free_time = next_free_time

    def __lt__(self, other):
        if self.next_free_time == other.next_free_time:
            return self.id < other.id
        else:
            return self.next_free_time < other.next_free_time

    def __repr__(self):
        return f'({self.id}, {self.next_free_time})'


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    result = []

    queue = []
    for w in range(n_workers):
        heapq.heappush(queue, Worker(w, 0))

    for job in jobs:
        next_worker = heapq.heappop(queue)
        result.append(AssignedJob(next_worker.id, next_worker.next_free_time))
        next_worker.next_free_time += job
        heapq.heappush(queue, next_worker)

    return result


def test():
    n_workers = 2
    jobs = [1, 2, 3, 4, 5]
    print(f'test: {n_workers} {jobs}')
    assigned_jobs_naive = assign_jobs_naive(n_workers, jobs)
    assigned_jobs= assign_jobs(n_workers, jobs)
    print(f'naive: {assigned_jobs_naive}')
    print(f'heapq: {assigned_jobs}')
    assert assigned_jobs == assigned_jobs_naive

    print('OK')


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
    # test()