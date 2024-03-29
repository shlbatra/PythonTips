from typing import Any

from ariadne import ObjectType
from data import (Author, Blog, BlogPayload, all_blogs, get_author, get_blog,
                  update_blog)
from graphql import GraphQLResolveInfo

from schema.types import mutation, query

#create connection here -> blogs with author
BLOG_TYPEDEF = """
    type Blog {
        id: ID!
        title: String!
        content: String!
        author: Author!
    }

    input BlogPayload {
        title: String
        content: String
    }

    type Mutation {
        update_blog(id: ID!, payload: BlogPayload!): Blog!
    }
"""
#attach resolver to blog object
blog_query = ObjectType("Blog")

#define queries in MAIN_TYPEDEF
@query.field("blogs")
def resolve_blogs(_, info: GraphQLResolveInfo) -> list[Blog]:
    return all_blogs()


@query.field("blog")
def resolve_blog(_, info: GraphQLResolveInfo, id: str) -> Blog:
    return get_blog(int(id))


@mutation.field("update_blog")
def resolve_update_blog(
    _, info: GraphQLResolveInfo, id: str, payload: BlogPayload
) -> Blog:
    return update_blog(int(id), payload)

#attach blog query to author using resolve
@blog_query.field("author")
def resolve_blog_author(blog: dict[str, Any], info: GraphQLResolveInfo) -> Author:
    print(blog)
    return get_author(blog["author_id"])
