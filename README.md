# 3TierWebApp

A simple TODO API.

Backend: Python (Flask)
Frontend: React (Axios)
Database: (MySQL)
API doc: Swagger
Cloud: Azure

## To run the application 

Start with pushing the images to your ACR.

- Backend image
- Frontend image
- MySQL image

After that setup a container app for each image.
A good idea is to setup the MySQL container first so the backend later can establish a connection to the container.
Make sure to have the right settings for each container:

- Backend container: port 5000, external ingress, no env variables when setting it up.
- Frontend container: port 3000, external ingress, no env variables when setting it up
- MySQL container: port 3306, external traffic over TCP. Set up relevant env variables. (check docker-compose)

When the MySQL container is set up make sure to access it via command line and log in as the user provided in the env variables.
Then use the database that you supplied in the env variables and create items table in that database.
For some reason (still working on that) the app.py dosent create the items table in the initialization of the database.

You can setup the containers with right env variables from the start, however the github workflows will provide them automaitcally when you push & pull requests. 

## Known bugs

- Bad backendURL can cause react to crash (whitescreen), therefore the backendurl is hardcoded.
- Not a bug but the app hasnt been tested with a persitent volume. If you shut down the mysql container you loose all the data.
- Some of the env variables are hardcoded and shouldnt be for example DATABASE_PASSWORD.
- app.py dosent create the items table even tough its supposed to.
- The branches are not merged properly. Each branch serve the purpose to try the app in different enviroments. For example, in docker, azure, with hardcoded env variables, with swagger integration, and locally.


### To make sure the API is working without having to use Postman, use cUrl for testing the requests easy, for example:

curl -X DELETE http://localhost:5000/api/items/1
{
  "message": "Item removed successfully!"
}


# CICD GITBOOKS

1. After a new build, the OpenAPI json gets downloaded from the live resource (via curl)
2. The new openAPI file is saved in docs folder with updated content
3. After the build workflow is complete and the openapi json is generated the openapi-gen workflow starts
4. The workflow generate swagger blocks based on the openapi file and gets saved in the apidocs.md
5. Gitbook sync the repo after a push and fetch the data from apidocs.md and display the updated json in gitbooks.