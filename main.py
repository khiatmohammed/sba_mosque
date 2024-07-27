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
from math import (
    radians,
    sin,
    cos,
    atan2,
    sqrt,
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


data = {
    (35.1788686, -0.6326298): "مسجد الشهداء",
    (35.1826881, -0.6374805): "مسجد إبن تيمية",
    (35.190847, -0.6315822): "مسجد أبو بكر الصديق",
    (35.1862095, -0.6358696): "مسجد عمر إبن الخطاب",
    (35.1772747, -0.6439883): "مسجد أم القرى",
    (35.1847204, -0.627384): "مسجد زيد إبن ثابث",
    (35.1875141, -0.6441104): "مسجد الكوثر",
    (35.1883081, -0.6460257): "مسجد الفردوس",
    (35.1874647, -0.6480864): "مسجد عبد الله إبن جعفر",
    (35.1940436, -0.6424977): "مسجد الرحمة",
    (35.212354, -0.6223852): "مسجد معاذ إبن جبل",
    (35.2180705, -0.6250337): "مسجد مصعب إبن عمير",
    (35.2194171, -0.6203722): "مسجد خالد إبن الوليد",
    (35.189699, -0.6231855): "مسجد فاطمة الزهراء القديم",
    (35.1900167, -0.6217951): "مسجد فاطمة الزهراء الجديد",
    (35.192648, -0.6163665): "مسجد الأزهر",
    (35.1874129, -0.6180014): "مسجد القدس",
    (35.2154673, -0.6369028): "مسجد أيوب",
    (35.191535, -0.6478004): "مسجد الأرقم بن أبي الأرقم",
    (35.1990851, -0.62226): "مسجد سعيد إبن زيد",
    (35.2007623, -0.6092242): "مسجد حراء",
    (35.1994925, -0.6252481): "مسجد الفردوس",
    (35.2063697, -0.6306267): "مسجد الحسين إبن علي",
    (35.2140563, -0.6304541): "مسجد الشيخ بلكبير",
    (35.2226299, -0.6251698): "مسجد الصفا",
    (35.2194406, -0.6140649): "مسجد النور",
    (35.2095047, -0.6147143): "مسجد إبراهيم الخليل",
    (35.1955125, -0.6311609): "مسجد عقبة إبن نافع",
    (35.2070843, -0.63954): "مسجد زين العابدين",
    (35.1962632, -0.6299596): "مسجد المدرسة",
    (35.2003037, -0.6338808): "مسجد الصحابة",
    (35.2048942, -0.6174606): "مسجد بني عامر الأنصار",
    (35.2003713, -0.6297176): "مسجد الأمير عبد القادر",
    (35.192621, -0.6244031): "مسجد ورش",
    (35.2139578, -0.6104398): "مسجد حمزة إبن عبد المطلب",
    (35.2014661, -0.6452257): "مسجد معاوية إبن أبي سفيان",
    (35.2026544, -0.6366952): "مسجد زينب بنت خزيمة",
    (35.2075726, -0.6471669): "مسجد أحد",
    (35.2020495, -0.652137): "مسجد عبد الرحمن بن عوف",
    (35.220513, -0.6074836): "مسجد النعمان إبن البشير",
    (35.2029839, -0.6304513): "مسجد الإمام مالك",
    (35.2197836, -0.6366535): "مسجد منى",
    (35.2042309, -0.6095421): "مسجد الإمام البخاري",
    (35.1976895, -0.6168706): "مسجد الشيخ البشير الإبراهيمي",
    (35.1849917, -0.6064605): "مسجد عرفة",
}


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
def get_nearest_mosque(coords: Coordinates):
    min_distance = float("inf")
    nearest_mosque = None

    for (lat, lon), mosque in data.items():
        distance = haversine_distance(coords.lat, coords.lon, lat, lon)
        if distance < min_distance:
            min_distance = distance
            nearest_mosque = mosque

    return {"nearest_mosque": nearest_mosque}
