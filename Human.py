# metaclass
class HumanMeta(type):
    def __call__(cls, *args, **kwargs):
        print('Called:', args, kwargs)
        return type.__call__(cls, *args, **kwargs)


class Human(metaclass=HumanMeta):
    """Descripes human behavior.

     Keyword arguments:
     age: int
         human age
     name: str
         human name
     height: float
         human height
     weight: float
         human weight
     job: str
         human job
     sex: str
         human sex
     hair_color: str
         human hair_color
     """
    # 7 attribute
    age: int
    name: str
    height: float
    weight: float
    job: str
    sex: str
    hair_color: str

    # getters setters
    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_height(self):
        return self.__height

    def set_height(self, height: float):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight: float):
        self.__weight = weight

    def get_job(self):
        return self.__job

    def set_job(self, job: str):
        self.__job = job

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex: str):
        self.__sex = sex

    def get_hair_color(self):
        return self.__hair_color

    def set_hair_color(self, hair_color: str):
        self.__hair_color = hair_color

    # 5 methods
    def __init__(self, age, name, height, weight, job, sex, hair_color):
        self.__age = age
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__job = job
        self.__sex = sex
        self.__hair_color = hair_color

    def __str__(self):
        return f"Human information:{self.__age}, {self.__name}, {self.__height}, {self.__weight}," \
               f" {self.__job}, {self.__sex}, {self.__hair_color}"

    # my methods
    def say_hi(self):
        print(f"{self.__name}, say Hi)")

    def say_common_information(self):
        print(f"My name is {self.__name}, I am {self.__age} years old. My job is {self.__job}")

    def walking(self):
        print(f"{self.__name} is walking")

    def my_drink_decorator(func):
        def wrapper(self):
            print(f"{self.__name}, bought drink")
            func(self)
            print(f"{self.__name}, utilized bottle")

        return wrapper

    @my_drink_decorator
    def drink(self):
        print(f"{self.__name}, is drinking")


