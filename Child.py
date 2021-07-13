from Human import Human


class Child(Human):
    def __init__(self, age, name, height, weight, job, sex, hair_color):
        if age < 16:
            job = "Unemployed"
        super(Child, self).__init__(age, name, height, weight, job, sex, hair_color)

    def set_job(self, job: str):
        if self.__age < 16:
            self.__job = "Unemployed"

    def walking(self):
        print(f"{self.get_name()}, cant walking))). Too small")

    def working(self):
        if self.get_job() == "Unemployed":
            print(f"I was born to flex, My human is working for me. Bu ga ga ga ga")





