import requests


API_URL = "http://127.0.0.1:5000"


def test_addition():
    test_data = {"num1": 1, "num2": 2}
    expected_result = test_data["num1"] + test_data["num2"]
    response = requests.post(f"{API_URL}/addition", json=test_data)
    assert response.status_code == 200
    assert response.json()["result"] == expected_result


def test_subtraction():
    test_data = {"num1": 1, "num2": 2}
    expected_result = test_data["num1"] - test_data["num2"]
    response = requests.post(f"{API_URL}/subtraction", json=test_data)
    assert response.status_code == 200
    assert response.json()["result"] == expected_result


def test_multiplication():
    test_data = {"num1": 1, "num2": 2}
    expected_result = test_data["num1"] * test_data["num2"]
    response = requests.post(f"{API_URL}/multiplication", json=test_data)
    assert response.status_code == 200
    assert response.json()["result"] == expected_result
