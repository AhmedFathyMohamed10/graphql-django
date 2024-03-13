import graphene
from graphene_django import DjangoObjectType
from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

schema = graphene.Schema(query=Query)
