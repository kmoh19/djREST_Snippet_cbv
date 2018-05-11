# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics
# 
# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class =SnippetSerializer
#     
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     
#     def post(self,request,*args,**kwargs):
#         
#         return self.create(request,*args,**kwargs)
#     
#     # The base class provides the core functionality, and the mixin classes provide the .list() and .create() actions.
#     # We're then explicitly binding the get and post methods to the appropriate actions.
#  
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView): 
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     
#     def put(self, request,*args,**kwargs):
#         return self.update(request, *args, **kwargs) 
#     
#     def delete(self, request,*args,**kwargs):
#         return self.destroy(request, *args, **kwargs)   

# 
# ########### ALTERNATIVELY ###########  ALTERNATIVELY ##################################################

## we can go one step further. REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    queryset =Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Snippet.objects.all()
    serializer_class =SnippetSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerializer
    
    
    
