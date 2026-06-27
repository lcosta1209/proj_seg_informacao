class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "object-src 'none'; "
            "frame-ancestors 'none'"
        )
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
        response['Pragma'] = 'no-cache'
        return response