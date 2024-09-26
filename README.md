# 3TierWebApp

Backend: Python (Flask)
Frontend: React (Axios)
Database: (MySQL)


## To run the application (backend)

Start the backend so the API is working correctly. Make sure there is a connection to your local database.

~ cd backend

--------------------------

~ python3 app.py

--------------------------

View database items on http://localhost:5000/api/items

--------------------------

## To run the application (frontend)

Start the backend so the API is working correctly. Make sure there is a connection to your local database.

~ cd frontend

--------------------------

~ npm start

--------------------------

View web interface at http://localhost:3000/

--------------------------

## To make sure the API is working without having to use Postman, use cUrl for testing the requests easy, for example:

curl -X DELETE http://localhost:5000/api/items/1
{
  "message": "Item removed successfully!"
}


