class MultiDBAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from .router import MultiDBRouter

        setattr(MultiDBRouter, "request", request)
        if request.method == "POST":
            db = request.POST.get("database", "default")
            request.session["DB"] = db

        response = self.get_response(request)

        return response
