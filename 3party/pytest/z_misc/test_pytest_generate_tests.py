"""Generate test parameters with pytest_generate_tests()"""

RANKS = "Ace 2 3 4".split()  # Shorten for brevity
FACES = "Heart Diamond".split()  # Shorten for brevity


def pytest_generate_tests(metafunc):
    if "rank" in metafunc.fixturenames:
        metafunc.parametrize("rank", RANKS)

    if "face" in metafunc.fixturenames:
        metafunc.parametrize("face", FACES)


def test_face(face):
    assert face in ["Heart", "Diamond", "Club", "Spade"]


def test_rank(rank):
    pass


def test_face_and_rank(face, rank):
    """Test the product of face x rank."""
    pass
