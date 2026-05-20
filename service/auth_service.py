class AuthService:
    def __init__(self):
        self.users = {"admin": "1234"}  # Exemple d'utilisateur

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False
