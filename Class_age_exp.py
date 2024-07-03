age = 18  # Поле возраста
experience = 1  # Поле рабочего стажа


class enrollee:
    def __init__(self, age_c, experience_c):
        self.age = age_c
        self.experience = experience_c

    def selection(self):
        if self.age >= 18 and self.experience >= 2:
            print("Вы на рассмотрении")
        else:
            print("Вам отказано в силу возраста или отсуствия необходимо стажа")


Mary = enrollee(age, experience)
Mary.selection()
