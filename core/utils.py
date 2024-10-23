from rest_framework.response import Response

def api_response(success=True, message="", data=None, errors=None, status_code=200):
    response_structure = {
        "status": "success" if success else "error",
        "message": message,
        "data": data if success else None,
        "errors": errors if not success else None,
    }
    return Response(response_structure, status=status_code)