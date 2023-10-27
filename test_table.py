import pytest
from parse_table import data, ProgrammingLanguage


@pytest.mark.parametrize("popularity_threshold", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_popularity_threshold(popularity_threshold):
    errors = []
    for language in data:
        if language.popularity < popularity_threshold:
            error_message = f"{language.name} (Frontend: {language.frontend}|Backend: {language.backend}) has {language.popularity:,} unique visitors per month. (Expected more than {popularity_threshold:,})"
            errors.append(error_message)
    assert not errors, "\n".join(errors)