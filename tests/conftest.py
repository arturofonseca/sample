"""Conftest holding configuration and fixtures for use across the test suite."""

from pathlib import Path
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import pytest


# Assumes this file lives in grp_.../test/
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def pytest_sessionstart(session: pytest.Session) -> None:
    """Prepare the session."""


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Clean up after the session finishes."""


def get_patch_prefix(test_file: str) -> str:
    """Generate the patch prefix for mocking based on the test file's path.

    Args:
        test_file (str): The test file's path (should always be `__file__`).

    Returns:
        str: The generated patch prefix for mocking (e.g., `my_pkg.src.score.score.{}`).

    Examples:
        ```
        from my_pkg.test.conftest import get_patch_prefix

        PATCH_PREFIX = get_patch_prefix(__file__)


        @patch(PATCH_PREFIX.format("SomeClass"))
        def test_my_func(mock_some_class): ...
        ```
    """
    path = Path(test_file).relative_to(ROOT_DIR)
    stem = path.stem.removeprefix("test_").removesuffix("test")
    path = path.with_name(stem).with_suffix("")
    return ".".join([path.parts[0], "src", *path.parts[2:], "{}"])
