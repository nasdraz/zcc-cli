import zendesk_api as api
import textwrap


def show_page(page):
    print('\n'
          '        ~~~ Listing Tickets ~~~\n'
          '[id] || Subject || Submitter || Date Created || Status\n'
          '---------------')
    for ticket in page:
        ticket_id, subject, name, date, status = ticket['id'], ticket['subject'], api.get_user_name(
            ticket['submitter_id']), ticket['created_at'][:10], ticket['status'].upper()

        print(f'[{ticket_id}] || {subject} || {name} || {date} || {status}\n'
              '---')


def show_ticket(ticket):
    ticket_id, subject, name, date, status = ticket['id'], ticket['subject'], api.get_user_name(
        ticket['submitter_id']), ticket['created_at'][:10], ticket['status'].upper()
    print(f'\n'
          f'        ~~~ Ticket {ticket_id} is: {status} ~~~\n'
          f'    Subject: {subject}\n'
          f'    Date Created: {date}    Submitter: {name}\n')
    print('\n'.join(textwrap.wrap(ticket['description'], 100, break_long_words=False, replace_whitespace=False)))


def show_menu_options():
    print('\n'
          '            ~~~ Main Menu ~~~\n'
          '        Please enter:\n'
          '            - \'list\' to view all tickets\n'
          '            - \'ticket\' to view a single ticket\n'
          '            - \'quit\' to exit program\n')


def show_list_options():
    print('\n'
          '            ~~~ List Menu ~~~\n'
          '        Please enter:\n'
          '            - The number of the page you wish to view \n'
          '            - \'back\' to go back to main menu \n'
          '            - \'quit\' to exit program \n')


def show_error(err_code):
    if err_code == 401:
        print('Error: User could not be authenticated. Check credentials.')
    elif err_code == 403:
        print('Error: User is not authorized to use API.')
    elif err_code == 404:
        print('Error: Record not found.')
    elif err_code == 429:
        print('Error: Usage limit has been exceeded.')
    elif err_code == 503:
        print('Error: Request could not be handled.')
    elif err_code == 0:
        print('Connection Error: Could not connect to the API.')
    else:
        print(f'Error: Code {err_code}.')
