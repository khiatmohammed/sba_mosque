Nearest Mosque Locator API 🕌
A fast and accurate API for finding the nearest mosque in Sidi Bel Abbes, Algeria.
Description 📝
The Nearest Mosque Locator API is a RESTful API built using the powerful FastAPI framework and Python. It provides a simple and efficient way for developers to integrate mosque location data for the city of Sidi Bel Abbes into their applications. 🛠️
By leveraging a SQLite database that stores the latitude, longitude, and name of mosques in Sidi Bel Abbes, the API utilizes the Haversine formula to calculate the distance between the user's coordinates and the nearest mosque, ensuring accurate results. 🧭
Features 🌟

Sidi Bel Abbes Mosque Lookup: Users can submit their coordinates and receive the name of the closest mosque in Sidi Bel Abbes. 🔍
SQLite Database: The API uses a SQLite database to store and manage the mosque data for the city, providing a reliable and efficient data source. 💾
Haversine Formula: The use of the Haversine formula guarantees the accuracy of the distance calculations, delivering precise results. 📏
CORS Support: The API is configured to support Cross-Origin Resource Sharing (CORS), allowing it to be accessed from various domains. 🌐

Tech Stack 🛠️

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 🚀
Python: A versatile and powerful programming language, providing the foundation for the API 🐍
SQLite: A lightweight and efficient database management system, used to store the mosque data 💻
Pydantic: A data validation library, ensuring the integrity of user input 👌

Deployment 🚀
The Nearest Mosque Locator API is currently hosted on Render, a cloud platform that provides a seamless deployment and hosting experience. 🌐
You can access the API at the following URL:
Copyhttps://nearest-mosque-locator-api.onrender.com
Usage 🤖
To use the Nearest Mosque Locator API, you can send a POST request to the root endpoint (/) with the user's latitude and longitude coordinates in JSON format:
jsonCopy{
  "lat": 35.1788686,
  "lon": -0.6326298
}
The API will respond with the name of the nearest mosque in Sidi Bel Abbes:
jsonCopy{
  "nearest_mosque": "مسجد الشهداء"
}
Future Enhancements 🚀
We plan to expand the database to include mosques from other cities, providing a more comprehensive solution for users. Additionally, we're exploring the integration of advanced features such as routing and directions, as well as user feedback and contribution capabilities.
