import base64
import json

import requests

baseUrl = "https://zccerewhon.zendesk.com"
tickets_path = "/api/v2/tickets.json?page[size]=25"
tickets_url = "https://zccerewhon.zendesk.com/api/v2/tickets.json?page[size]=25"
ticket_url = "https://zccerewhon.zendesk.com/api/v2/tickets/"
users_url = 'https://zccerewhon.zendesk.com/api/v2/users/'

secret = json.load(open('./config.json'))
auth = secret['username'] + '/token:' + secret['api-token']
encoded_auth = str(base64.b64encode(auth.encode("utf-8")), "utf-8")

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic ' + encoded_auth}

user_cache = {}


def get_ticket_pages():
    try:
        pages = []

        url = tickets_url
        while url:
            req = requests.get(url=url, headers=headers)

            if req.status_code == 200:
                pages.append(req.json()['tickets'])

                if req.json()['meta']['has_more']:
                    url = req.json()['links']['next']
                else:
                    url = None
            else:
                return {'error_code': req.status_code}

        return pages
    except requests.ConnectionError:
        return {'error_code': 0}


def get_user_name(user_id):
    if user_id in user_cache:
        return user_cache[user_id]
    else:
        try:
            req = requests.get(url=users_url + str(user_id), headers=headers)

            if req.status_code == 200:
                user_cache[user_id] = req.json()['user']['name']
                return req.json()['user']['name']
            else:
                return str(user_id)

        except requests.ConnectionError:
            return str(user_id)


def get_ticket(ticket_id):
    try:
        req = requests.get(url=ticket_url + str(ticket_id), headers=headers)

        if req.status_code == 200:
            return req.json()['ticket']
        else:
            return {'error_code': req.status_code}

    except requests.ConnectionError:
        return {'error_code': 0}
