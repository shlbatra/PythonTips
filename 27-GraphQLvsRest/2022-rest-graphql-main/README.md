# GraphQL vs REST: What's The Difference And When To Use Which?

GraphQL vs REST: they're both popular approaches to developing backend services. In this video I show you what the difference is between REST and GraphQL, how to build a basic API using either of these approaches and when to choose one over the other.

- Rest Interface 
    - Representational State Transfer
    - Take action on resource , you send http request, body of request contains desired new state and server reply with actual state after handling request
    - resource orienred
    - RPC (Remote Procedural Calls) -> action oriented -> call remote fn that performs certain task & get result back. Ex, set block title and get response as ok instead of block title
    - Issues
        - Make sure yourself Rest interface following standard Ex. Swagger open AI standard
        - getting author seperate request -> coordinate several request in front end to get the data you need and waiting for these requests to complete
        - doesnt enforce distinction structure of data in database and structure of data that you receive/send via API -> send data directly from db - security issues ex. send user email
        - not control how much data get back from request
- graphql
    - use single end pt and query language to interact with server
    - views data as graph structure where objects connected by relationships forming graph
    - query lang specify what data you want and which part of graph structure you want to retrieve
    - so get blog and asscoiated author in single request
    - define interface with graphql backend via schema & specify what data looks like
    - can only do things that is specified in graph schema
    - Use library ariadne to setup graphsql, also graphene and strawberry
    - 2 ways interact with GraphQL service
        - Posting query (retrieving data) - GET
        - do mutation (change) - PUT/POST/DELETE
    - Write queries in playground when start graphql server
    - http://127.0.0.1:5000/graphql
    - Ex. -> get all blogs with id, title and content
        query {
            blogs {
                id
                title
                content
            }
        }
    - Lot more control over data you need and reduces amt of data that server needs to send back - speed up app
    - Allow for mutations as well
    - Get things in 1 request Ex.
        query {
            blogs {
                id
                author {
                    id 
                    name
                }
            }
        }
    - Issues
        - Send request to server complex - define mutation / query to make 
        - suffers from n+1 problem,get authors from blog, seperate request for each author -> local caching mechanism 
        - query lang pretty verbose -> specify mutation, variable names multiple places
        - not everything standardized
- When to use ?
    - Rest simple to use - smaller apps and public apps, Only expose data that you want to make public (layered architecture- translate data from db to public forum)
    - Graphql -> complex apps that are tightly integrated and need specific data - front end eay to manage.