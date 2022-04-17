"""Программный модуль фитнес-трекера,
который обрабатывает данные для трех видов тренировок:
для бега, спортивной ходьбы и плавани.
"""


class Training:
    """Базовые показатели тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        """Инцализация данных."""
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Расчёт дистанции в киллометрах."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Расчёт скорости в км/ч."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> None:
        pass

    def show_training_info(self):
        """Получаение данных о тренировке."""
        info_training = InfoMessage(self.__class__.__name__,
                                    self.duration,
                                    self.get_distance(),
                                    self.get_mean_speed(),
                                    self.get_spent_calories())
        return info_training


class Running(Training):
    """Класс тренировки бега."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Подсчёт каллорий."""
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        spent_calories = ((coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2) *
                          self.weight / self.M_IN_KM * self.duration * 60)
        return spent_calories


class SportsWalking(Training):
    """Класс тренировки спортивной ходьбы."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        """Инцализация данных."""
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Подсчёет каллорий."""
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        spent_calories = ((coeff_calorie_1 * self.weight + (self.get_mean_speed() ** 2 //
                          self.weight) * coeff_calorie_2 * self.weight) * self.duration * 60)
        return spent_calories


class Swimming(Training):
    """Класс тренировки плавания."""
    LEN_STEP = 1.38
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        """Инцализация данных."""
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        """Расчёт дистанции в киллометрах."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Расчёт средней скорости в км/ч."""
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Расчёт каллорий."""
        spent_calories = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return spent_calories


class InfoMessage:
    """Класс тренировки для вывода результата."""
    def __init__(self, training_type: str,
                 duration: float,
                 distance: float,
                 mean_speed: float,
                 spent_calories: float) -> None:
        self.duration = duration
        self.distance = distance
        self.mean_speed = mean_speed
        self.spent_calories = spent_calories
        self.training_type = training_type

    def get_message(self) -> str:
        """Вывод сообщения."""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. cкорость: {self.mean_speed:.3f} км/ч; '
                f'Потрачено ккал: {self.spent_calories:.3f}. ')


def read_package(workout_type: str, data: list) -> Training:
    """Создания объектов класса."""
    dict_train = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    return dict_train[workout_type](*data)


def main(training: Training) -> None:
    """Вызов объекта класса."""
    info = training.show_training_info()
    print(InfoMessage.get_message(info))


if __name__ == '__main__':
    """Главная фунцкия для проверки."""
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
