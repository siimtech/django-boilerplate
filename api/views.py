import logging
from ninja import NinjaAPI
import warnings
from watchtower import WatchtowerWarning
from newproject.auth import JwtAuth
from django.contrib.auth.decorators import login_required

api = NinjaAPI()

logger = logging.getLogger('django_app')

jwt_auth_instance = JwtAuth()

@api.get("/hello", auth=jwt_auth_instance, response=dict)
def protected_endpoint(request):
    print(request.auth)
    return {"message": "Hello, world!"}

@api.get("/event-handler")
def hello4(request):
    try:
        logger.info("This might be too late in the application lifecycle.")
    except WatchtowerWarning as e:
        warnings.warn("Attempted to log after shutdown: " + str(e))

    logger.debug('Debug message after CloudWatch logging attempt')
    return {"message": "Hello world2"}