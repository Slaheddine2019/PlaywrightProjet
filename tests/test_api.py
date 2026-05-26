import pytest

import requests
from playwright.sync_api import Playwright, expect


@pytest.mark.skip(
    reason="Ce test est un exemple de test d'API, il n'est pas lié à l'application web testée"
)
def test_api_getttt(playwright):
    response = playwright.request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert (
        data["title"]
        == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    )
