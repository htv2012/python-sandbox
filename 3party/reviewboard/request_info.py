#!/usr/bin/env python
"""
Display a review request info for a review id

Reference:
https://www.reviewboard.org/docs/manual/2.0/webapi/2.0/resources/review-request/
"""

from rbtools.api.client import RBClient
import argparse


info = """
Review ID: {review.id} -- {review.summary}
------------------------------------------------------------------------
Description:
{review.description}
------------------------------------------------------------------------

Status: {review.status}
Branch: {review.branch}
Bugs:   {bugs}
People: {people}
"""


def list2str(seq):
    return ', '.join(seq)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('review_id', type=int)
    options = parser.parse_args()

    client = RBClient('http://reviewboard/')
    root = client.get_root()

    review = root.get_review_request(review_request_id=options.review_id)
    people = list2str(r.title for r in review.target_people)
    bugs = list2str(review.bugs_closed)

    print(info.format(**locals()))
