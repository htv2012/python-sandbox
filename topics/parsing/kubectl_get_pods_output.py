#!/usr/bin/env python
"""
Parses the output of the kubectl get pods
"""
import collections
import pprint


kubectl_get_pods_output = """
NAME                               READY   STATUS    RESTARTS   AGE

virt-controller-57fc9c5cdc-5gqsj   1/1     Running   0          8h

virt-controller-57fc9c5cdc-cbk78   1/1     Running   1          8h

virt-api-57f89ff5b4-v4z2f          1/1     Running   0          8h

virt-handler-p4r9x                 1/1     Running   0          8h
""".strip()


def parse_kubectl_get_pods_output(text):
    lines = [line for line in text.strip().splitlines()]
    non_empty_lines = (line.split() for line in lines if line)

    # Create the namedtuple to contain a row
    keys = [key.lower() for key in next(non_empty_lines)]
    PodInfo = collections.namedtuple("PodInfo", keys)

    pods = [
        PodInfo(*values)
        for values in non_empty_lines
    ]

    for pod in pods:
        print(pod)


parse_kubectl_get_pods_output(kubectl_get_pods_output)
