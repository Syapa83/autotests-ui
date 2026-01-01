import pytest

@pytest.mark.slow
def test_heavy_calculation():
    pass

@pytest.mark.integration
def test_integration_with_external_api():
    pass

@pytest.mark.smoke
def test_quick_check():
    pass