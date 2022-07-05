import pytest

from fastapi import Depends

from app.db.mongodb import AsyncIOMotorClient, get_database


