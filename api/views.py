import logging
from ninja import NinjaAPI
import warnings
from watchtower import WatchtowerWarning

api = NinjaAPI()

# Get a logger specific to this module
logger = logging.getLogger('django_app')

@api.get("/event-handler")
def hello4(request):
    try:
        logger.info("This might be too late in the application lifecycle.")
    except WatchtowerWarning as e:
        warnings.warn("Attempted to log after shutdown: " + str(e))

    logger.debug('Debug message after CloudWatch logging attempt')
    return {"message": "Hello world2"}