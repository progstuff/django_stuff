from datetime import datetime


class UserLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.META.get('REQUEST_METHOD', '')
        query = request.get_full_path()
        time_lbl = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        with open('users_log.log', 'a') as log:
            log.write('; '.join([time_lbl, query, method]) + '\n')
        response = self.get_response(request)

        return response