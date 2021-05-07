# pylint: skip-file

"""Unit tests for the parse module."""

from pyuntype_cli.utils.title import title


class TestUtils:

    """Test the method title()."""

    @staticmethod
    def test_samle_title() -> None:
        """It should pass."""

        title()
        assert 1 == 1
