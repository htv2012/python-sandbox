# http://pymotw.com/2/multiprocessing/communication.html

import multiprocessing
import time
import random


class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print("%s: Exiting" % proc_name)
                self.task_queue.task_done()
                break
            print("%s: %s" % (proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return


class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        self.task_time = random.randint(1, 20)
        time.sleep(self.task_time)  # pretend to take some time to do the work
        return "Task #{} - {:2} seconds - result: {}".format(
            self.a, self.task_time, 2 * self.a
        )

    def __str__(self):
        return "Task #{}".format(self.a)


if __name__ == "__main__":
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count()
    print("Creating %d consumers" % num_consumers)
    consumers = [Consumer(tasks, results) for i in range(num_consumers)]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print("Result:", result)
        num_jobs -= 1
