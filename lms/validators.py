import re
from rest_framework.serializers import ValidationError


class LinkCheckValidator:
    """Проверка на отсутствие ссылок на сторонние ресурсы, кроме https://youtube.com"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'(https?://(?!www\.youtube\.com)[\w.-]+(?:\.[\w.-]+)+(/[\w.-]*)*)')
        tmp_val = dict(value).get(self.field)
        if bool(reg.match(tmp_val)):
            raise ValidationError(f'Можно ссылки только с https://youtube.com!!!')
