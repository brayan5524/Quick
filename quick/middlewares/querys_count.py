import time
from django.db import connection
import logging

logger = logging.getLogger(__name__)

class QueryCountMiddleware:
    """Middleware para contar queries y medir tiempo de respuesta"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        total_time = time.time() - start_time
        total_queries = len(connection.queries)

        logger.info(f"[{request.method}] {request.path} -> {total_queries} queries, {total_time:.4f} seg")
        
        # Agregar al response headers para debugging
        response["X-Total-Queries"] = str(total_queries)
        response["X-Response-Time"] = f"{total_time:.4f} sec"

        return response
