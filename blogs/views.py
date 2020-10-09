from rest_framework import viewsets
from blogs.models import BlogModel
from blogs.serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class BlogViewset(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

    ## Supports /blogs/cool_blogs/ url pattern
    @action(detail=False, methods=['get'])
    def cool_blogs(self, request, pk=None):
        # Apply some business logic to get list of cool blog posts
        blogs = BlogModel.objects.filter(pk=2)
        sr = BlogSerializer(blogs, many=True)
        return Response({'data': sr.data})



