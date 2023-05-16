# test/integration/test_app_redis.py

import pytest

from redis import RedisError


@pytest.mark.timeout(1.5)
def test_should_update_redis(redis_client, http_client):
    # Given
    try:
        redis_client.set("page_views", 4)
    except RedisError as e:
        assert False

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 200
    assert response.text == "This page has been seen 5 times."
    assert redis_client.get("page_views") == b"5"
