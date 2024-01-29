import os

import pytest
from yarl import URL

from app.settings import conf


@pytest.fixture(scope="session")
def pg_url():
    """
    Provides base PostgreSQL URL for creating temporary databases.
    """
    return URL(os.getenv("CI_STAFF_PG_URL", conf.dsn_url))
