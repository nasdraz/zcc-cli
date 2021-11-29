

import zendesk_api as api
import ui


def view_ticket():
    ticket_id = input('\nPlease enter ticket id: ')

    ticket = api.get_ticket(ticket_id)
    if 'error_code' not in ticket:
        ui.show_ticket(ticket)
    else:
        ui.show_error(ticket['error_code'])


def list_tickets():
    pages = api.get_ticket_pages()

    if 'error_code' not in pages:
        ui.show_page(pages[0])
        print('--- Page {}/{} ---'.format(1, len(pages)))
        while True:
            if len(pages) > 2:
                ui.show_list_options()
            else:
                break

            usr_in = input('Awaiting input: ')
            if usr_in == 'quit':
                end()
            elif usr_in == 'back':
                break
            elif usr_in.isnumeric():
                if 0 < int(usr_in) <= len(pages):
                    page_index = int(usr_in) - 1
                    ui.show_page(pages[page_index])
                    print('--- Page {}/{} ---'.format(page_index + 1, len(pages)))
                else:
                    print('Such page does not exist')
            else:
                print('Input is invalid')

    else:
        ui.show_error(pages['error_code'])


def menu_loop():

    while True:
        ui.show_menu_options()
        i = input('Awaiting Input: ')
        if i == 'list':
            list_tickets()
        elif i == 'ticket':
            view_ticket()
        elif i == 'quit':
            end()
        else:
            print('Input invalid')


def start():
    print("         ---------TICKET VIEWER---------")
    menu_loop()


def end():
    print('Program End.')
    exit()


if __name__ == '__main__':
    start()
