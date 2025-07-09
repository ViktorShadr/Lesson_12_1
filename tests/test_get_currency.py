from unittest.mock import Mock, patch

import pytest

from src.get_currency import get_currency_rate


def test_get_currency_rate_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "Valute": {
            "USD": {
                "Value": 73.5
            }
        }
    }

    with patch('requests.get', return_value=mock_response):
        result = get_currency_rate("USD")
        assert result == {
            "currency_code": "USD",
            "rate": 73.5
        }


def test_get_currency_rate_no_currency():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "Valute": {
            "EUR": {
                "Value": 89.5
            }
        }
    }

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="No data for currency"):
            get_currency_rate("USD")


def test_get_currency_rate_failed_request():
    mock_response = Mock()
    mock_response.status_code = 500

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get currency rate"):
            get_currency_rate("USD")