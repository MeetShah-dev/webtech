import pytest

from rest_framework.test import APIClient
from pytest_factoryboy import register

from .factories import (
    BlogFactory, 
    DraftFactory, 
    FileFactory, 
    UserFactory, 
    RoleFactory, 
    CategoryFactory, 
    MagazineFactory
)

register(RoleFactory)
register(UserFactory)
register(MagazineFactory)
register(CategoryFactory)
register(BlogFactory)
register(DraftFactory)
register(FileFactory)


@pytest.fixture
def api_client():
    return APIClient


# to run test run the command: "pytest -s"