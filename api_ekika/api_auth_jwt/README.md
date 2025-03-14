# JWT Authentication

This module serves as a fundamental component within the API Framework. To implement JWT-based authentication in your API configuration system, it is essential to integrate this module. Note that this module is not intended to function independently; it relies on the API Framework Base (api_framework_base) to seamlessly operate alongside other API authentication mechanisms.

## Overview

JWT (JSON Web Token) authentication provides a robust and stateless way to secure API endpoints. It ensures that only authorized users can access API resources by requiring the client to include a token in the request headers.

## How It Works

When making a request to an API endpoint secured with JWT authentication, clients must include a Authorization header with the JWT token. This token is issued by the API provider during login or authentication and must be sent with each subsequent request to access protected resources.

**Headers**

|Key|Value|
|:-------:|:----------------:|
|Authorization|Bearer Your-JWT-Token|

## Configuring JWT Authentication

**Specify the authentication type as JWT for using JSON Web Tokens (JWT).**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-1.png" class="img-fluid" alt="API-JWT-Auth-Setting-1"/>

**The Authentication Configuration tab is visible when the API is in the OPEN/PUBLISHED state.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-2.png" class="img-fluid" alt="API-JWT-Auth-Setting-2"/>

**Select a JWT algorithm from the list of available options.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-3.png" class="img-fluid" alt="API-JWT-Auth-Setting-3"/>

**Provide the JWT token's expiration time in hours.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-7.png" class="img-fluid" alt="API-JWT-Auth-Setting-7"/>

**Use the "UPDATE JWT KEYS" button to create or refresh JWT keys according to the chosen algorithm.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-4.png" class="img-fluid" alt="API-JWT-Auth-Setting-4"/>

**As shown in the image below, JWT keys are generated according to the chosen algorithm when the "UPDATE JWT KEYS" button is clicked.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-5.png" class="img-fluid" alt="API-JWT-Auth-Setting-5"/>

**As shown in the image below, JWT keys are generated according to the chosen algorithm when the "UPDATE JWT KEYS" button is clicked.**
<img src="static/description/assets/api-jwt-images/API-JWT-Auth-Setting-6.png" class="img-fluid" alt="API-JWT-Auth-Setting-6"/>

## Login Using JWT

**Below Image Shows the jwt login request in postman**
<img src="static/description/assets/api-jwt-images/JWT-Login-Postman.png" class="img-fluid" alt="JWT-Login-Postman"/>

**Here's an example using Python:**
```python
import requests
import json

url = "http://localhost:8016/gql_jwt/api/jwt/auth/login"

payload = json.dumps({
  "login": "admin",
  "password": "admin"
})
headers = {
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

## Fetch Data Using JWT Authentication

**Below Image Shows the jwt fetch data request in postman**
<img src="static/description/assets/api-jwt-images/JWT-Fetch-Data-1.png" class="img-fluid" alt="JWT-Login-Postman"/>
<img src="static/description/assets/api-jwt-images/JWT-Fetch-Data-2.png" class="img-fluid" alt="JWT-Login-Postman"/>

**Here's an example using Python:**
```python
import requests
import json

url = "http://localhost:8016/gql_jwt"

payload = "{\"query\":\"query MyQuery {\\n    SaleOrder {\\n        id\\n        name\\n    }\\n}\",\"variables\":{}}"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsIm5hbWUiOiJNaXRjaGVsbCBBZG1pbiIsImV4cCI6MTczMDIyNzYwM30.wbcAM5Ps-qvPvLkW-IJX7iODHXQo1Ps6-14Hiq4FClE',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
