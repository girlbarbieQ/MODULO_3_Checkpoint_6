class Usuario:
    def _init_(self, username, password):
        self.username = username
        self.password = password


usuario1 = Usuario("Barbara", "1234")


print(usuario1.username)
print(usuario1.password)