from typing import Optional, cast

import pytest
from _pytest.fixtures import FixtureRequest
from pytest_mock import MockFixture

from overhave import OverhaveFileSettings, OverhaveProjectSettings
from overhave.entities import FeatureExtractor, GitRepositoryInitializer, OverhaveScenarioCompilerSettings
from overhave.scenario import FileManager


@pytest.fixture(scope="session")
def test_compilation_settings() -> OverhaveScenarioCompilerSettings:
    return OverhaveScenarioCompilerSettings()


@pytest.fixture()
def test_file_settings(request: FixtureRequest) -> OverhaveFileSettings:
    if hasattr(request, "param"):
        return cast(OverhaveFileSettings, request.param)
    raise NotImplementedError


@pytest.fixture()
def mocked_file_manager(mocker: MockFixture) -> FileManager:
    return cast(FileManager, mocker.create_autospec(FileManager))


@pytest.fixture()
def mocked_git_initializer(mocker: MockFixture) -> GitRepositoryInitializer:
    return cast(GitRepositoryInitializer, mocker.create_autospec(GitRepositoryInitializer))


@pytest.fixture()
def test_browse_url(request: FixtureRequest) -> Optional[str]:
    if hasattr(request, "param"):
        return cast(Optional[str], request.param)
    raise NotImplementedError


@pytest.fixture()
def test_project_settings(test_browse_url: Optional[str]) -> OverhaveProjectSettings:
    return OverhaveProjectSettings(browse_url=test_browse_url)


@pytest.fixture()
def test_feature_extractor(request: FixtureRequest) -> FeatureExtractor:
    if hasattr(request, "param"):
        return cast(FeatureExtractor, request.param)
    raise NotImplementedError
