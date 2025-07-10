from src.date_time import time_remake


def test_time_remake():
    assert time_remake(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
    assert time_remake([]) == []