---
description: Discover how to properly setup API token and credentials
icon: rocket-launch
---

# Get started

To use the younium API each request will need to be authenticated using a JWT access token. This guide describes how to generate the necessary credentials and how to acquire the JWT token to enable using the younium APIs. If you need to authenticate with a legacy user, using username and password a guide can be found [here](https://developer.younium.com/get-started-legacy#U8eBS) but this method is obsolete and will be deprecated.

It’s recommended to authenticate to the API using the client credentials generated from the API Token. If you cannot log on into Younium using SSO/MFA with your user, you will need to be migrated to the new authentication platform. Please contact your Younium customer success manager.

Regardless of the authentication method, a user is required and any user with sufficient permissions for your use case can be used. However, it’s recommended when developing automated solutions and integrations to have a dedicated API user set up.

### Generating an API token and client credentials <a href="#generating-an-api-token-and-client-credentials" id="generating-an-api-token-and-client-credentials"></a>

1. Open the user profile menu in the top right of the screen by clicking your name, select “Privacy & Security”.

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252F0mXZe15FktelxqHPGil1%252FPrivacy\_security.png%3Falt%3Dmedia%26token%3Df73aa508-7dd2-4e3c-adf6-d3112b16bb77\&width=768\&dpr=4\&quality=100\&sign=455f570e\&sv=1)

1. Select “Personal Tokens” in the panel to the left and click “Generate Token”.

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252FOL87CpqCW0Ry1OqYTTNW%252Fpersonal%2520token.png%3Falt%3Dmedia%26token%3D1668f7cf-4866-4fff-ade3-5e725b5c2440\&width=768\&dpr=4\&quality=100\&sign=27ac7cc9\&sv=1)

1. Write a relevant description Click “Create”

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252FYDOohhCa7dHadeulQYwj%252Fapi%2520token.png%3Falt%3Dmedia%26token%3D90bc2c98-d4cb-4feb-aec3-a842d1c3d02e\&width=768\&dpr=4\&quality=100\&sign=ef76adb0\&sv=1)

1. The Client and ID and Secret key is now generated and be visible. Make sure to copy the values now since they will never be visible again. These credentials will be used to generating the access JWT token

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252FfXHKaqA8o7bEJ3l5Uk5u%252FCredentials%2520%281%29.png%3Falt%3Dmedia%26token%3Dc0361a08-2e62-4130-926a-81c2cbeabc61\&width=768\&dpr=4\&quality=100\&sign=a51723c7\&sv=1)

### Generating A JWT token <a href="#generating-a-jwt-token" id="generating-a-jwt-token"></a>

The jwt access token is acquired via a POST request to the /auth/token endpoint with the provided header and body.

Sandbox: [api.sandbox.younium.com/auth/token](https://developer.younium.com/get-started)

Production: [api.younium.com/auth/token](https://developer.younium.com/get-started)

#### Request header <a href="#request-header" id="request-header"></a>

Copy

```
Content-Type: application/json
```

#### Request body <a href="#request-body" id="request-body"></a>

Copy

```
{ 
    "clientId": [Client ID], 
    "secret": [Secret key] 
}
```

If all credentials are valid the request will return the following response containing the `accessToken` which will be used to authenticate to the API.

Copy

```
{
    "expires": "Thu, 21 Mar 2024 11:12:01 GMT",
    "expiresIn": 86400,
    "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cC...",
    "refreshToken": "4baf4774-5ef9-4983-a8d8-f4fdae7f7000"
}
```

The access token is valid for 24 hours after which a new token will need to be acquired.

If the the credentials provided are not valid or other errors occur a response with code 400 or 401 will be returned with an error message describing the error:

Copy

```
error: [Error message]
```

#### Example request in Postman <a href="#example-request-in-postman" id="example-request-in-postman"></a>

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252FJWX7k6lxuvOUcSpkFvii%252Fauth%2520example%2520postman.png%3Falt%3Dmedia%26token%3D299bb43e-a2c7-4ea4-82ea-9007ecc08a2f\&width=768\&dpr=4\&quality=100\&sign=db7f98ab\&sv=1)

### Making Authenticated calls to the Younium API <a href="#making-authenticated-calls-to-the-younium-api" id="making-authenticated-calls-to-the-younium-api"></a>

The access token received from a successful authentication will then be used to make authenticated calls to the Younium API.

All requests to the Younium API should have the following HTTP Headers:

Copy

```
Authorization: Bearer [JWT token]
Content-Type: application/json
api-version : [version] (optional but recommended)
legal-entity: [legal entity id or Name]
```

#### Specifying legal entity <a href="#specifying-legal-entity" id="specifying-legal-entity"></a>

Specifying the `legal-entity` header allow you to read and write to the desired legal entity and will be required to specify if your tenant have multiple legal entities. If the provided legal entity cannot be found under the tenant a 403 Forbidden response will be returned.

Example request to GET /accounts with all headers in postman

![](https://younium.gitbook.io/\~gitbook/image?url=https%3A%2F%2F940708998-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FMV73ftGLs1NaypiZYzZB%252Fuploads%252FSRCVCcbvE2RWZj6kmXmb%252Fexample%2520request.png%3Falt%3Dmedia%26token%3D2b296404-fdce-4aa3-bef3-330db119e323\&width=768\&dpr=4\&quality=100\&sign=bb06555e\&sv=1)

#### Versions <a href="#versions" id="versions"></a>

The header api-version may be set to specify which version of the api to be called. By default version 2.1 will be called.

[**Read more about different versions**](https://developer.younium.com/developer-resources#jJK1f)

#### Common errors related to authentication <a href="#common-errors-related-to-authentication" id="common-errors-related-to-authentication"></a>

In most cases an error message indicates why an error is thrown but a message is absent or unclear the below cases can give a general idea of the issue.

* 401 Unauthorized response: Generally indicates an expired, missing or incorrect access token.
* 403 Forbidden response: Indicates that the request is authorized but the action is forbidden. This may occur if:
  * legal entity provided in the header is empty, invalid or incorrect
  * If the user is missing permission to access a resource. This can be solved bu changing the permissions in the UI
  * Issue with accessing connected integrations or services.
