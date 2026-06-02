import requests
import pytest

# common data
BASE_URL = "https://restful-booker.herokuapp.com"

BOOKING = {
    "firstname": "Anna",
    "lastname": "Ivanova",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-05"},
    "additionalneeds": "Breakfast",
}


# preparation - fixtures
@pytest.fixture
def token():
    resp = requests.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    return resp.json()["token"]

# create booking befire tests
@pytest.fixture
def created_booking(token):                 
    resp = requests.post(f"{BASE_URL}/booking", json=BOOKING)
    booking_id = resp.json()["bookingid"]
    yield booking_id                        
    requests.delete(f"{BASE_URL}/booking/{booking_id}",   # clean up 
                    headers={"Cookie": f"token={token}"})


# tests

# create booking
def test_create_booking():
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING)  
    assert response.status_code == 200                             
    body = response.json()                                          
    assert "bookingid" in body
    assert body["booking"]["firstname"] == "Anna"


# read booking using created_booking fixture
def test_get_booking(created_booking):
    response = requests.get(f"{BASE_URL}/booking/{created_booking}") 
    assert response.status_code == 200                                
    assert response.json()["lastname"] == "Ivanova"  


# update booking
def test_update_booking(token, created_booking):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}",
    }
    updated = {**BOOKING, "firstname": "Updated"}
    response = requests.put(
        f"{BASE_URL}/booking/{created_booking}",
        json=updated,
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["firstname"] == "Updated"


# delete booking
def test_delete_booking(token, created_booking):
    headers = {"Cookie": f"token={token}"}
    response = requests.delete(
        f"{BASE_URL}/booking/{created_booking}",
        headers=headers,
    )
    assert response.status_code == 201


# negative test cases


#  nonexistent booking
def test_get_nonexistent_booking():
    response = requests.get(f"{BASE_URL}/booking/99999999")
    assert response.status_code == 404


# update without token
def test_update_without_token(created_booking):
    response = requests.put(
        f"{BASE_URL}/booking/{created_booking}",
        json=BOOKING,
    )
    assert response.status_code == 403

