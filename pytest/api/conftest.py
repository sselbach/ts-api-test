import pytest

def pytest_configure():
    pytest.api_base_url = "https://app.trustsource.io/api/v1"