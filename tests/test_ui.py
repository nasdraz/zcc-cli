import ui


ticket = {'id': 333, 'subject': 'test ticket 1', 'submitter_id': 111, 'created_at': '2021-11-28T22:55:29Z', 'status': 'open', 'description': 'test description'}
page = [{'id': 333, 'subject': 'test ticket 1', 'submitter_id': 111, 'created_at': '2021-11-28T22:55:29Z', 'status': 'open'},
        {'id': 444, 'subject': 'test ticket 2', 'submitter_id': 222, 'created_at': '2021-11-29T22:55:29Z', 'status': 'open'}]


def test_show_ticket(mocker, capsys):
    mocker.patch('zendesk_api.get_user_name', return_value='Ron Fricke')
    ui.show_ticket(ticket)
    captured = capsys.readouterr()
    assert captured.out == f'''
        ~~~ Ticket 333 is: OPEN ~~~
    Subject: test ticket 1
    Date Created: 2021-11-28    Submitter: Ron Fricke

test description\n'''


def test_show_page(mocker, capsys):
    mocker.patch('zendesk_api.get_user_name', return_value='Ron Fricke')
    ui.show_page(page)
    captured = capsys.readouterr()
    assert captured.out == '''
        ~~~ Listing Tickets ~~~
[id] || Subject || Submitter || Date Created || Status
---------------
[333] || test ticket 1 || Ron Fricke || 2021-11-28 || OPEN
---
[444] || test ticket 2 || Ron Fricke || 2021-11-29 || OPEN
---
'''


def test_show_menu_options(capsys):
    ui.show_menu_options()
    captured = capsys.readouterr()
    assert captured.out == ('\n'
                            '            ~~~ Main Menu ~~~\n'
                            '        Please enter:\n'
                            '            - \'list\' to view all tickets\n'
                            '            - \'ticket\' to view a single ticket\n'
                            '            - \'quit\' to exit program\n\n')


def test_show_list_options(capsys):
    ui.show_list_options()
    captured = capsys.readouterr()
    assert captured.out == ('\n'
                            '            ~~~ List Menu ~~~\n'
                            '        Please enter:\n'
                            '            - The number of the page you wish to view \n'
                            '            - \'back\' to go back to main menu \n'
                            '            - \'quit\' to exit program \n\n')


def test_show_error(capsys):
    ui.show_error(401)
    captured = capsys.readouterr()
    assert captured.out == 'Error: User could not be authenticated. Check credentials.\n'

    ui.show_error(403)
    captured = capsys.readouterr()
    assert captured.out == 'Error: User is not authorized to use API.\n'

    ui.show_error(404)
    captured = capsys.readouterr()
    assert captured.out == 'Error: Record not found.\n'

    ui.show_error(429)
    captured = capsys.readouterr()
    assert captured.out == 'Error: Usage limit has been exceeded.\n'

    ui.show_error(503)
    captured = capsys.readouterr()
    assert captured.out == 'Error: Request could not be handled.\n'

    ui.show_error(0)
    captured = capsys.readouterr()
    assert captured.out == 'Connection Error: Could not connect to the API.\n'

    ui.show_error(999)
    captured = capsys.readouterr()
    assert captured.out == f'Error: Code {999}.\n'
