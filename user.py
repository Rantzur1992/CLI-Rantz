class User:
    def __init__(self, username, password, auth_token = None):
        self.username = username
        self.password = password
        self.auth_token = auth_token

    def create_new_user(self, name, email, password, admin, profile_updatable,
                        disable_ui_access, internal_password_disabled, groups,
                        watch_manager, policy_manager):
        pass