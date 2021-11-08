import pytest
from main01 import get_word_count


@pytest.mark.parametrize("sentence, expected", [("우리는 파이썬을 즐겨요", 3)])
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected


# 위 방식으로도 되고 아래 방식으로 하나하나도 됨. 위 : 위치 기반 인자


def test_get_word_count():
    assert get_word_count("우리는 파이썬을 즐겨요") == 3
