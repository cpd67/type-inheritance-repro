import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from myapp.types import SomeModelType, SomeOtherModelType, AnotherModelType


@strawberry.type
class Query:
    some_model_type_list: list[SomeModelType] = strawberry_django.field()
    some_other_model_type: SomeOtherModelType = strawberry_django.field()
    another_model_type: AnotherModelType = strawberry_django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
