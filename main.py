from user import User
artifactory_url = "https://rantz.jfrog.io/artifactory"
selection_options = ["1", "2", "3", "4", "5", "6"]
import requests as req
from requests.auth import HTTPBasicAuth
import sys
import argparse as ap
user = None


def input_username():
    return input("Username: ")


def input_password():
    return input("Password: ")


def report_failure(res):
    error_message = res['errors'][0]['message']
    print(f"Request returned the following error: {error_message}")


def get_instance_id(username, password):
    url = f"{artifactory_url}/api/system/service_id"
    res = req.get(url=url, auth=HTTPBasicAuth(username, password))
    if res.status_code == 200:
        return res.text
    else:
        report_failure(res.json())

def connect_user(username, password):
    #  Taking the default values of the access token to keep it simple
    #  Setting the token as admin token for full access of requested endpoints
    create_access_token = f"{artifactory_url}/api/security/token"
    service_id = get_instance_id(username, password)
    data = {"username" : username,
            'scope' : f"{service_id}:admin api:*"}
    headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
    res = req.post(url=create_access_token, data=data, headers=headers, auth=HTTPBasicAuth(username,password))
    if res.status_code == 200:
        access_token = res.json()['access_token']
        return access_token
    else:
        report_failure(res.json())


def show_welcome():
    print("Welcome to Artifactory CLI!\n"
          "Please provide your username and password:\n")
    global user
    username = input_username()
    password = input_password()
    access_token = connect_user(username, password)
    user = User(username=username,password=password,auth_token=access_token)


def validate_selection(selection):
    return selection in selection_options

def pick_action(selection):
    cases = {
        "1": system_ping,
        "2": get_system_version,
        "3": create_user,
        "4": "Delete User",
        "5": "Get Storage Information",
        "6": exit_cli,
    }
    cases.get(selection)()

def system_ping():
    system_ping_url = f"{artifactory_url}/api/system/ping"
    res = req.get(url=system_ping_url)
    print(f"System ping returned: {res.text}")

def get_system_version():
    global user
    system_version_url = f"{artifactory_url}/api/system/version"
    res = req.get(url=system_version_url, auth=HTTPBasicAuth(user.username, user.auth_token))
    if res.status_code == 200:
        version  = res.json()["version"]
        print(f"System version: {version}")
    else:
        report_failure(res.json())

def create_user():
    pass

def exit_cli():
    sys.exit()

def show_menu():
    show_welcome()
    while True:
        selection = input("Please choose one of the following:\n"
              "1. System Ping\n"
              "2. System Version\n"
              "3. Create User\n"
              "4. Delete User\n"
              "5. Get Storage Information\n"
              "6. Exit\n")
        if not validate_selection(selection):
            print("Invalid selection.")
        else:
            pick_action(selection)


if __name__ == '__main__':
    show_menu()