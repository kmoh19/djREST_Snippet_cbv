from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
#     
#     def create(self, validated_data):
#         #creaate and return anew 'Snippet' instance, given the validated data
#         return Snippet.objects.create(**validated_data)
#     
#     
#     def update(self,instance,validated_data):
#         #Update and return an existing snippet instance, given the validated data
#         
#         instance.title = validated_data.get('title',instance.title)
#         instance.code =validated_data.get('code',instance.code)
#         instance.linenos =validated_data.get('code',instance.linenos)
#         instance.language =validated_data.get('code',instance.language)
#         instance.style =validated_data.get('code',instance.style)
#         instance.save()
#         return instance
################## OR less verbose ###########

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner =serializers.ReadOnlyField(source='ownwer.username')
    
    #Notice that we've also added a new 'highlight' field. This field is of the same type as the url field, except that it points to the
    #'snippet-highlight' url pattern, instead of the 'snippet-detail' url pattern.Because we've included format suffixed URLs such as '.json', we also need to 
    #indicate on the highlight field that any format suffixed hyperlinks it returns should use the '.html' suffix.
    
    
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    
    class Meta:
        model = Snippet
        fields =('id','title','code','linenos','language','style','owner','url','highlight')
       
    def create(self, validated_data):
        #create and return anew 'Snippet' instance, given the validated data
        return Snippet.objects.create(**validated_data)
    
    
    def update(self,instance,validated_data):
        #Update and return an existing snippet instance, given the validated data
        
        instance.title = validated_data.get('title',instance.title)
        instance.code =validated_data.get('code',instance.code)
        instance.linenos =validated_data.get('code',instance.linenos)
        instance.language =validated_data.get('code',instance.language)
        instance.style =validated_data.get('code',instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    
    class Meta:
        model = User
        fields= ('url','id','username','snippets')#Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.
        
        
    
    