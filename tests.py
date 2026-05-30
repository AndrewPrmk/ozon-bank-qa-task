import pytest
from main import get_highest_hero, get_height_in_cm

#позитивный тест
@pytest.mark.parametrize("gender, has_work, expected_name, expected_height_in_cm", [
    ("Female", True, "Giganta", 6250),
    ("Male", False, "Ymir", 30480),
    ("Male", True, "Utgard-Loki", 1520),
    ("Female", False, "Ardina", 193)
])
def test_positive(gender, has_work, expected_name, expected_height_in_cm):
    result = get_highest_hero(gender, has_work)
    if expected_name is None:
        assert result is None
    else:
        assert result is not None
        assert result["name"] == expected_name
        assert get_height_in_cm(result) == expected_height_in_cm

#негативный тест
@pytest.mark.parametrize("gender, has_work", [
    ("sadb", True),
    (None, True),
    ("", True),
    ("Female", None)
])
def test_no_found_person(gender, has_work):
    result = get_highest_hero(gender, has_work)
    assert result is None

#проверка фильтра по полу
def test_filter_gender():
    result = get_highest_hero("Male", True)
    assert result is not None
    assert result["appearance"]["gender"] == "Male"

#проверка фильтра по работе
def test_filter_work():
    result = get_highest_hero("Male", True)
    assert result is not None
    assert result["work"]["occupation"] != ""

#проверка работоспособности функции get_height_in_cm
def test_get_height_in_cm():
    #рост в метрах
    result1 = {"appearance": {"height": ["200", "61.0 meters"]}}
    assert get_height_in_cm(result1) == 6100

    #рост в сантиметрах
    result2 = {"appearance": {"height": ["6'8", "203 cm"]}}
    assert get_height_in_cm(result2) == 203

    #отсутствие поля height
    result3 = {"appearance": {}}
    assert get_height_in_cm(result3) == 0

    #рост с десятичной точкой в метрах
    result4 = {"appearance": {"height": ["200   ", "304.8 meters"]}}
    assert get_height_in_cm(result4) == 30480






