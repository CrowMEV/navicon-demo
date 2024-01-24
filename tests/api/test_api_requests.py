import requests

import app.api_requests as app


# class MockResponse:
#     @staticmethod
#     def json():
#         return {"mock_key": "mock_response"}


# def test_get_json(monkeypatch):
#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr(requests, "get", mock_get)

#     result = app.get_json("https://fakeurl")
    # assert result["mock_key"] == "mock_response"


def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
