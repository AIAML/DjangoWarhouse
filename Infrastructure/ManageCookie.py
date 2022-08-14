from django.http import HttpResponse
import datetime
class Coookie:
    def set_cookie(response, key, value, days_expire=1):
        if days_expire is None:
            max_age = 1 * 4 * 60 * 60  # 4 hour
        else:
            max_age = days_expire * 4 * 60 * 60
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
            "%a, %d-%b-%Y %H:%M:%S GMT",)
        response.set_cookie(
            key,
            value,
            max_age=max_age,
            expires=expires,
        )

    def get_cookie(request,label):
        return request.COOKIES.get(label)

    def delete_cookie(request,label):
        response.delete_cookie(label)

    def check_session_cookie(request,lable):
        try:
            print(request.COOKIES.get(lable,'notset'))
            if request.COOKIES.get(lable,'notset') != 'notset':
                return 1
            else:
                return 0
        except Exception as ex:
                return 0