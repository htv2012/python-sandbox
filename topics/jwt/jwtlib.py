#!/usr/bin/env python3
import base64
import collections
import json

JwtParts = collections.namedtuple("JwtParts", ["header", "payload", "signature"])


def base64_pad(unpadded: bytes):
    padded = unpadded + b"=" * (4 - len(unpadded) % 4)
    return padded


def decode_jwt(data: bytes):
    raw_header, raw_payload, raw_signature = data.split(b".")

    raw_header = base64_pad(raw_header)
    raw_header = base64.urlsafe_b64decode(raw_header)
    header = json.loads(raw_header)

    raw_payload = base64_pad(raw_payload)
    raw_payload = base64.urlsafe_b64decode(raw_payload)
    payload = json.loads(raw_payload)

    raw_signature = base64_pad(raw_signature)
    signature = base64.urlsafe_b64decode(raw_signature)

    return JwtParts(header, payload, signature)
