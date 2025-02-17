from typing import Any, Dict, List, Mapping, Optional, Type

from pydantic import BaseModel, validator
from yarl import URL

from overhave.base_settings import BaseOverhavePrefix
from overhave.utils import make_url


class EmptyBrowseURLError(ValueError):
    """Exception for situation with empty ```browse_url``` while trying to ```get_link_url```."""


class OverhaveProjectSettings(BaseOverhavePrefix):
    """
    Entity project settings.

    You could specify your fixture content for specific pytest usage with your own plugins.
    It could give you pretty extended file with powerful possibilities.
    `fixture_context` will be formatted by `OverhaveProccessor` before test would be started.
    """

    # Fixture content in list format, which would be compiled into formatted string.
    fixture_content: List[str] = [
        "from pytest_bdd import scenarios",
        "from overhave import overhave_proxy_manager",
        "pytest_plugins = overhave_proxy_manager().plugin_resolver.get_plugins()",
        "scenarios('{feature_file_path}')",
    ]

    # Task tracker URL for browsing
    browse_url: Optional[URL]
    # Behaviour specification keyword for tasks attachment and linking
    links_keyword: Optional[str]

    # Templates are used for creation of test user and system specifications.
    # Keys for specification mapping are still the same - feature types.
    user_spec_template_mapping: Mapping[str, Type[BaseModel]] = {}

    @validator("browse_url", pre=True)
    def make_browse_url(cls, v: Optional[str]) -> Optional[URL]:
        return make_url(v)

    @validator("links_keyword")
    def validate_links_keyword(cls, v: Optional[str], values: Dict[str, Any]) -> Optional[str]:
        if isinstance(v, str) and values.get("browse_url") is None:
            raise ValueError("Browse URL should be specified in case of links keyword usage!")
        return v

    def get_link_url(self, link: str) -> str:
        if isinstance(self.browse_url, URL):
            return (self.browse_url / link).human_repr()
        raise EmptyBrowseURLError("Browse URL is None, so could not create link URL!")


class OverhaveTestSettings(BaseOverhavePrefix):
    """Settings for PytestRunner, which runs scenario tests with specified addoptions."""

    default_pytest_addoptions: str = "--disable-warnings"
    extra_pytest_addoptions: Optional[str]

    workers: Optional[int]  # Number of xdist workers, `None` by default
