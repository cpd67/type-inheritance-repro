import strawberry
import strawberry_django
from strawberry.types.info import Info
from strawberry.scalars import ID
from strawberry_django.fields.field import StrawberryDjangoField

from . import models


class CustomStrawberryDjangoField(StrawberryDjangoField):
    pass


class OtherCustomStrawberryDjangoField(StrawberryDjangoField):
    pass


def custom_field(resolver=None, *args, **kwargs):
    """
    Custom decorator used to create a new CustomStrawberryDjangoField.

    Should work similarly to strawberr_django.field().
    """
    field = CustomStrawberryDjangoField(*args, **kwargs) 

    if resolver:
        return field(resolver)
    return field


def other_custom_field(resolver=None, *args, **kwargs):
    """
    Custom decorator used to create a new CustomStrawberryDjangoField.

    Should work similarly to strawberr_django.field().
    """
    field = OtherCustomStrawberryDjangoField(*args, **kwargs) 

    if resolver:
        return field(resolver)
    return field


@strawberry.type
class BaseType:
    field_1: str = CustomStrawberryDjangoField()
    field_2: str = CustomStrawberryDjangoField()
    field_3: str = strawberry_django.field()
    field_4: str = OtherCustomStrawberryDjangoField()

    @custom_field
    def field_5(self, info: Info) -> int:
        return 42

    @other_custom_field
    def field_6(self, info: Info) -> str:
        return "Test!"


@strawberry_django.type(models.SomeModel)
class SomeModelType(BaseType):
    field_7: str


@strawberry_django.type(models.SomeOtherModel)
class SomeOtherModelType(BaseType):
    field_8: int


@strawberry_django.type(models.AnotherModel)
class AnotherModelType(BaseType):
    field_9: bool
