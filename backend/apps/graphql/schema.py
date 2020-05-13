import graphene
import backend.apps.graphql.example.schema as schema_example

# Query for getting the data from the server.
class Query(schema_example.Query, graphene.ObjectType):
    pass

# Create schema
schema = graphene.Schema(query=Query)