import pytest


@pytest.mark.parametrize(
    "language, lang_id",
    [
        ("en", 1),
        pytest.param("fr", 2, marks=pytest.mark.unlicensed),
        ("qwer", 3),
    ],
)
def test_lang(language, lang_id):
    pass
