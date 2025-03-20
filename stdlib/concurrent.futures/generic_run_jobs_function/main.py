# https://stackoverflow.com/q/79520670/459745
import random
import time
from concurrent.futures import ThreadPoolExecutor

from loguru import logger


def some_function(job_in: dict) -> dict:
    logger.debug(f"Start job {job_in=}")
    # Simulate time it takes to finish job
    time.sleep(random.randint(1, 4))

    job_out = {**job_in, "status": "done"}
    logger.debug(f"Finish job {job_out=}")
    return job_out


def run_jobs(job, args, threads=None):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        output = executor.map(job, args)
    return output


def main():
    logger.info("start")
    args_list = [{"job_id": i} for i in range(7)]
    for result in run_jobs(some_function, args_list, threads=4):
        logger.info(result)
    logger.info("end")


if __name__ == "__main__":
    main()
