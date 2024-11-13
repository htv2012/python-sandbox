import pytest

RANKS = "Ace 2 3 4 5 6 7 8 9 10 Jack Queen King".split()
FACES = "Heart Diamond Club Spade".split()


@pytest.fixture(params=FACES)
def face(request):
    return request.param


@pytest.fixture(params=RANKS)
def rank(request):
    return request.param


def test_card(rank, face):
    pass
