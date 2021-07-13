from Human import Human
from BMI import BMI
from Child import Child


if __name__ == "__main__":
    human = Human(21, "Olex", 185, 88, "Programmer", "male", "blonde")
    print(human.say_hi())
    print(human.say_common_information())
    print(human.walking())
    print(human.drink())

    child = Child(1, "Vlad", 12, 30, "flex", "mail", "blonde")
    child.walking()
    child.working()

    #dataclass
    bmi = BMI(human)
    print(bmi.calculate_BMI())




