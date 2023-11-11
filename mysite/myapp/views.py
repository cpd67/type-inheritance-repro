from django.shortcuts import render
from strawberry.django.views import GraphQLView
from strawberry.type import get_object_definition

from .types import SomeModelType, SomeOtherModelType, AnotherModelType


class CustomGraphqlView(GraphQLView):
    """
    Custom gql view to demonstrate type inheritance issue.
    """

    def dispatch(self, request, *args, **kwargs):
        # Grab the object definitions for each object type
        some_model_type_def = get_object_definition(SomeModelType, strict=True)
        some_other_model_type_def = get_object_definition(SomeOtherModelType, strict=True)
        another_model_type_def = get_object_definition(AnotherModelType, strict=True)

        # Print out the fields & their types
        print("SomeModelType object definition fields:")
        print("-------------------")
        for f in some_model_type_def.fields:
            print(f.python_name, type(f))
        print()

        print("SomeOtherModelType object definition fields:")
        print("-------------------")
        for f in some_other_model_type_def.fields:
            print(f.python_name, type(f))
        print()

        print("AnotherModelType object definition fields:")
        print("-------------------")
        for f in another_model_type_def.fields:
            print(f.python_name, type(f))
        print()

        return super().dispatch(request, *args, **kwargs)