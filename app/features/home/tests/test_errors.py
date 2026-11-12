"""Tests de páginas de error."""


def test_405_error_page(client):
    response = client.get("/auth/logout")
    assert response.status_code == 405
    html = response.get_data(as_text=True)
    assert "Esa dirección no admite este método." in html
    assert "Volver al inicio" in html
