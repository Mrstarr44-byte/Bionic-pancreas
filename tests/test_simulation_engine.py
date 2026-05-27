import pytest
from app.simulation.engine import SimulationEngine


@pytest.mark.parametrize('bg, carbs, insulin, expected_status', [
    (120, 0, 0, 'normal'),          # Normal aralık içinde
    (65, 0, 0, 'hypoglycemia'),     # <70 -> hipoglisemi
    (190, 0, 0, 'hyperglycemia'),   # >180 -> hiperglisemi
    (70, 0, 0, 'normal'),           # Alt sınır
    (180, 0, 0, 'normal'),          # Üst sınır
])
def test_status_determination(bg, carbs, insulin, expected_status):
    result = SimulationEngine.calculate_new_bg(bg, carbs, insulin)
    assert result['status'] == expected_status


def test_carb_insulin_impact():
    # CARB_FACTOR=4, INSULIN_FACTOR=40 - sabit değerler engine içinde
    result = SimulationEngine.calculate_new_bg(100, carbs=5, insulin=1)
    # Yeni BG = 100 + 5*4 - 1*40 = 100 + 20 - 40 = 80
    assert result['new_bg'] == 80.0
    assert result['status'] == 'normal'


def test_rounding_and_limits():
    # Sonucun 1 ondalık basamağa yuvarlandığını kontrol et
    result = SimulationEngine.calculate_new_bg(99.456, carbs=0, insulin=0)
    assert result['new_bg'] == 99.5

    # Minimum sınır (20) altına düşerse min değeri almalı
    result_low = SimulationEngine.calculate_new_bg(10, carbs=0, insulin=5)
    assert result_low['new_bg'] == SimulationEngine.BG_MIN

    # Maksimum sınır (600) üstüne çıkarsa max değeri almalı
    result_high = SimulationEngine.calculate_new_bg(590, carbs=5, insulin=0)
    assert result_high['new_bg'] == SimulationEngine.BG_MAX
