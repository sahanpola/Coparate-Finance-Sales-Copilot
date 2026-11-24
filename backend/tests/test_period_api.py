from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_valid_period_returns_summary():
    response = client.post(
        "/api/v1/period/validate",
        json={
            "start_date": "2026-10-01",
            "end_date": "2026-10-31",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "start_date": "2026-10-01",
        "end_date": "2026-10-31",
        "inclusive_days": 31,
    }


def test_single_day_period_is_valid():
    response = client.post(
        "/api/v1/period/validate",
        json={
            "start_date": "2026-10-15",
            "end_date": "2026-10-15",
        },
    )

    assert response.status_code == 200
    assert response.json()["inclusive_days"] == 1


def test_start_date_after_end_date_returns_validation_error():
    response = client.post(
        "/api/v1/period/validate",
        json={
            "start_date": "2026-10-31",
            "end_date": "2026-10-01",
        },
    )

    assert response.status_code == 422

    data = response.json()

    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert data["error"]["message"] == "Request validation failed."


def test_invalid_date_format_returns_validation_error():
    response = client.post(
        "/api/v1/period/validate",
        json={
            "start_date": "not-a-date",
            "end_date": "2026-10-31",
        },
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_missing_required_field_returns_validation_error():
    response = client.post(
        "/api/v1/period/validate",
        json={
            "start_date": "2026-10-01",
        },
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_unknown_endpoint_returns_standard_error():
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404

    data = response.json()

    assert data["error"]["code"] == "HTTP_ERROR"
    assert data["error"]["message"] == "Not Found"