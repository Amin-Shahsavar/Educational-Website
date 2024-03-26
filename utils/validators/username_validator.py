from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.+-]+\Z"
    message = _(
        "یک نام کاربری معتبر وارد کنید که شامل حروف و اعداد و علامت های ./+/-/_ باشد."
    )
    flags = 0
