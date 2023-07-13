class Cat:
    num_legs = 4
    owner_name = "Lalisa Manobal"

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def print_info(self):
        print(f"Cat name is {self.name.upper()} and its color is {self.color.lower()}")
    
    @classmethod
    def get_num_legs(cls):
        return cls.num_legs
    
    @staticmethod
    def get_owner_name():
        return Cat.owner_name


if __name__ == '__main__':
    leo = Cat('Leo', 'brown')
    luca = Cat('Lily', 'white')
    leo.print_info()
    luca.print_info()
    print(f'The number of legs of all cats is {Cat.get_num_legs()}')
    print(f'The owner of these cats is {Cat.get_owner_name()}')