- Source Link
    - https://www.nylas.com/blog/use-python-requests-module-rest-apis/

- Python Request library
- Application Programming Interface (API) is a web service that grants access to specific data and methods that other applications can access – and sometimes edit – via standard HTTP protocols, 
- REpresentational State Transfer (REST) consists of a set of guidelines designed to simplify client / server communication.
- Request -> When you want to interact with data via a REST API, this is called a request
    - Endpoint -> The URL that delineates what data you are interacting with. Endpoint URL is tied to a specific resource within an API.
    - Method -> Specifies how you’re interacting with the resource located at the provided endpoint. 
        - GET – Retrieve data
        - PUT – Replace data
        - POST – Create data
        - DELETE – Delete data
    - Data -> If you’re using a method that involves changing data in a REST API, you’ll need to include a data payload with the request that includes all data that will be created or modified.
    - Headers -> Contain any metadata that needs to be included with the request, such as authentication tokens, the content type that should be returned, and any caching policies.
- Response -> Contains response header and response data. The response header consists of useful metadata about the response, while the response data returns what you actually requested.
- Ex. curl -X GET "http://api.open-notify.org/astros.json"
- Request Data with GET (Python)
    response = requests.get("http://api.open-notify.org/astros.json")
The response object contains all the data sent from the server in response to your GET request, including headers and the data payload. We get content by following -
                response.content() # Return the raw bytes of the data payload
                response.text() # Return a string representation of the data payload
                response.json() # This method is convenient when the API returns JSON
- How to Use Query Parameters 
Queries can be used to filter the data that an API returns, and these are added as query parameters that are appended to the endpoint URL. This is handled via the params argument, which accepts a dictionary object
    query = {'lat':'45', 'lon':'180'}
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    print(response.json())
- How to Create and Modify Data With POST and PUT -> add data argument to pass assosciated data
    # Create a new resource
    response = requests.post('https://httpbin.org/post', data = {'key':'value'})
    # Update an existing resource
    requests.put('https://httpbin.org/put', data = {'key':'value'})
- To get metadata for your requests ->
    response.headers
    print(response.headers["date"]) 
- How to Authenticate to a REST API
    - The simplest way is to pass your username and password to the appropriate endpoint as HTTP Basic Auth
    - Ex. requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))
    - A more secure method is to get an access token that acts as an equivalent to a username/password combination. Ex. OAuth
    - Ex.   my_headers = {'Authorization' : 'Bearer {access_token}'}
            response = requests.get('http://httpbin.org/headers', headers=my_headers)
    - Other ways to authenticate -> digest, Kerberos, NTLM, and AuthBase. 
- Use Sessions to Manage Access Tokens 
    - Session objects persist parameters that are needed for making multiple requests within a single session, like access tokens. 
    - Ex.   session = requests.Session()
            session.headers.update({'Authorization': 'Bearer {access_token}'})
            response = session.get('https://httpbin.org/headers')
- The Basics of HTTP Status Codes
    - 1xx Informational – Indicates that a request has been received and that the client should continue to make the requests for the data payload. You likely won’t need to worry about these status codes while working with Python Requests.
    - 2xx Successful – Indicates that a requested action has been received, understood, and accepted. You can use these codes to verify the existence of data before attempting to act on it.
    - 3xx Redirection – Indicates that the client must make an additional action to complete the request like accessing the resource via a proxy or a different endpoint. You may need to make additional requests, or modify your requests to deal with these codes.
    - 4xx Client Error – Indicates problems with the client, such as a lack of authorization, forbidden access, disallowed methods, or attempts to access nonexistent resources. This usually indicates configuration errors on the client application.
    - 5xx Server Error – Indicates problems with the server that provides the API. There are a large variety of server errors and they often require the API provider to resolve.
- How to Check for HTTP Errors With Python Requests
    - Status_code attribute that can be used to check for any errors the API might have reported
- How to Handle HTTP Errors With Python Requests
    -   response = requests.get("http://api.open-notify.org/astros.json")
        if (response.status_code == 200):
            print("The request was a success!")
            # Code here will only run if the request is successful
        elif (response.status_code == 404:
            print("Result not found!")
            # Code here will react to failed requests

    -   Another Examples ->   
            try:
                response = requests.get('http://api.open-notify.org/astros.json')
                response.raise_for_status()      # raise an exception for all error codes (4xx and 5xx)
                # Additional code will only run if the request is successful
            except requests.exceptions.HTTPError as error:
                print(error)
                # This code will run if there is a 404 error.
- TooManyRedirects
    - Something that is often indicated by 3xx HTTP status codes is the requirement to redirect to a different location for the resource you’re requesting -> infinite redirect loop
    - Ex.
        try:
            response = requests.get('http://api.open-notify.org/astros.json')
            response.raise_for_status()
            # Code here will only run if the request is successful
        except requests.exceptions.TooManyRedirects as error:
            print(error)
    - Ex. set max redirects 
    response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)
    - Ex. disable redirecting directly
    response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)
- ConnectionError
    - Connection errors can occur for many different reasons, including a DNS failure, refused connection, internet connectivity issues or latency somewhere in the network.
    Ex.
    try:
        response = requests.get('http://api.open-notify.org/astros.json') 
        # Code here will only run if the request is successful
    except requests.ConnectionError as error:
        print(error)
- Timeout
    - Ex.
    Timeout errors occur when you’re able to connect to the API server, but it doesn’t complete the request within the allotted amount of time. 
    try:
        response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
        # Code here will only run if the request is successful
    except requests.Timeout as error:
        print(error)
- Robust API Calls
    - Ex. 
        try:
        response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
        response.raise_for_status()
        # Code here will only run if the request is successful
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
