from users.models import Token, User
from rest_framework import authentication
from rest_framework import exceptions

import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)


class CustumAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN') # get the token request header
        if not token: # no username passed in request headers
            return None # authentication did not succeed

        try:
            user = r.get('token_'+token)            
        except User.DoesNotExist:
            return None
            #raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        if user == None:
            return None
            #raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 

        u = json.loads(user)
        
        return (User(u['username'], u['urlPhoto'], u['pwd'], u['date']), None) # authentication successful