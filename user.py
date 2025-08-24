class User:
    name = "Liliya"
    last_name = "Khudich"
    age = 44
    image = "some image"

    def hello(self):
        print("Hello World!")

    def goodbye(self):
        return f"{self.name} {self.last_name} goodbye!"
