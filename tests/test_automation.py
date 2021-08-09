import pytest

from automation.automation import get_data, pull_phone_info, pull_email_info, write_to_file


def test_get_data_can_grab_from_file_system():
    actual = get_data("assets/potential-contacts.txt")
    assert actual


def test_pull_phone_info_can_grab_phone_numbers():
    example = "One world we cold public trip. Tonight stock two short financial million. Cost some animal great course next eye. danielletaylor@hotmail.com Less or information clear century guess somebody. Sister follow wide report land find.861-26-5898Especially can south wall need.+1-178-383-0937x54779He final hour painting nature people never rise. Home decide ever kind together dinner. danielletaylor@hotmail.com +1-178-383-0937x54779Thank appear test call in key set. Approach agree land him gas alone reach. Agent region book whose military traditional quite."
    actual = pull_phone_info(example)
    expected = [
        "+11783830937x54779",
        "861265898",
    ]
    assert actual == expected


def test_pull_email_info_can_grab_emails():
    example = "One world we cold public trip. Tonight stock two short financial million. Cost some animal great course next eye. danielletaylor@hotmail.com Less or information clear century guess somebody. Sister follow wide report land find.861-26-5898Especially can south wall need.+1-178-383-0937x54779He final hour painting nature people never rise. Home decide ever kind together dinner. danielletaylor@hotmail.com +1-178-383-0937x54779Thank appear test call in key set. Approach agree land him gas alone reach. Agent region book whose military traditional quite."
    actual = pull_email_info(example)
    expected = ["danielletaylor@hotmail.com"]
    assert actual == expected


def test_write_to_file_can_write_a_file():
    example = ["item1", "item2"]
    write_to_file(example, "assets/test_file.txt")
    assert get_data("assets/test_file.txt")
