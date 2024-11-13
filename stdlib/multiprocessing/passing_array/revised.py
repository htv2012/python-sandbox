from multiprocessing import Queue, JoinableQueue, Process
from toolbox import logger


def calc_manager(myData, start, end):
    logger.info("CalcManager started")
    # Initialize the multiprocessing queue so we can get the values
    # returned to us
    tasks = JoinableQueue()
    results = Queue()

    # Add tasks
    for i in range(start, end):
        tasks.put(myData[i])

    # Create processes to do work
    nprocs = 3
    for i in range(nprocs):
        logger.info("starting processes")
        p = Process(target=worker, args=(tasks, results))
        p.daemon = True
        p.start()

    # Wait for tasks completion, i.e. tasks queue is empty
    try:
        tasks.join()
    except KeyboardInterrupt:
        logger.info("Cancel tasks")

    # Print out the results
    print("RESULTS")
    while not results.empty():
        result = results.get()
        print(result)

    logger.info("CalManager ended")


def worker(tasks, results):
    while True:
        try:
            task = tasks.get()  # one row of input
            task["done"] = True  # simular work being done
            results.put(task)  # Save the result to the output queue
        finally:
            # JoinableQueue: for every get(), we need a task_done()
            tasks.task_done()


def main():
    """ Entry """
    logger.info("Main started")
    data = []
    for i in range(5):
        data.append({str(i): i})

    calc_manager(data, start=0, end=5)
    logger.info("Main ended")


if __name__ == "__main__":
    main()
