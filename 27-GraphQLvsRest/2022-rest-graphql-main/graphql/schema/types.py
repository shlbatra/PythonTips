from ariadne import MutationType, QueryType

#! -> raise error , basic queries defined below, define blog and author type here
MAIN_TYPEDEF = """
    type Query {
        blogs: [Blog]!
        blog(id: ID!): Blog!
        authors: [Author]!
        author(id: ID!): Author!
    }
    """

query = QueryType() #get
mutation = MutationType() #put/post/delete
