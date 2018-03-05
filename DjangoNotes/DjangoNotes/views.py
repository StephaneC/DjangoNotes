from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'users': reverse('users:users-list', request=request, format=format),
       'notes': reverse('notes:notes', request=request, format=format),
})