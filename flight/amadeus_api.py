# your_app/amadeus_api.py

import requests
import time
from django.conf import settings

# Optional: in-memory token cache (simple, not for prod scale)
_cached_token = None
_cached_token_expiry = 0

def get_access_token():
    global _cached_token, _cached_token_expiry

    # Return cached token if still valid
    if _cached_token and time.time() < _cached_token_expiry:
        return _cached_token

    response = requests.post(
        "https://test.api.amadeus.com/v1/security/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": settings.AMADEUS_API_KEY,
            "client_secret": settings.AMADEUS_API_SECRET,
        }
    )
    data = response.json()
    _cached_token = data['access_token']
    _cached_token_expiry = time.time() + data['expires_in'] - 60  # buffer

    return _cached_token


def search_flights(origin, destination, departure_date, adults=1):
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": adults,
        "nonStop":'false',
        "currencyCode": "INR"
    }

    response = requests.get(
        "https://test.api.amadeus.com/v2/shopping/flight-offers",
        headers=headers,
        params=params
    )

    return response.json() if response.status_code == 200 else None
