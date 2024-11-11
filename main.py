# Copyright (c) 2024 Khiat Mohammed Abderrezzak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Khiat Mohammed Abderrezzak <khiat.dev@gmail.com>


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlite3 import connect
from math import (
    radians,
    sin,
    cos,
    atan2,
    sqrt,
)


app: FastAPI = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connect to the SQLite database
conn = connect('mosques.db')
c = conn.cursor()


# Fetch all the data from the 'mosques' table
c.execute("SELECT * FROM mosques")
data = c.fetchall()


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # Radius of the Earth in kilometers
    R: float = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad: float = radians(lat1)
    lon1_rad: float = radians(lon1)
    lat2_rad: float = radians(lat2)
    lon2_rad: float = radians(lon2)

    # Difference in coordinates
    dlon: float = lon2_rad - lon1_rad
    dlat: float = lat2_rad - lat1_rad

    # Haversine formula
    a: float = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c: float = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance: float = R * c

    return distance


class Coordinates(BaseModel):
    lat: float
    lon: float


@app.post("/")
def get_nearest_mosque(coords: Coordinates) -> dict:
    min_distance: float = float("inf")
    nearest_mosque: None = None

    for row in data:
        lat, lon, name = row
        distance: float = haversine_distance(coords.lat, coords.lon, lat, lon)
        if distance < min_distance:
            min_distance: float = distance
            nearest_mosque: str = mosque

    return {"nearest_mosque": nearest_mosque}
