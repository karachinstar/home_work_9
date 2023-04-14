# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект
# класса (см. урок)

from time import sleep


class Meta_traff(type):
    TrafficLight = None

    def __call__(cls):
        if cls.TrafficLight is None:
            cls.TrafficLight = super().__call__()
            return cls.TrafficLight
        else:
            return cls.TrafficLight


class TrafficLight(metaclass=Meta_traff):
    __color = {"красный": 7, "желтый": 2, "зелёный": 8}

    def running(self):
        print("красный")
        sleep(self.__color["красный"])
        print("желтый")
        sleep(self.__color["желтый"])
        print("зелёный")
        sleep(self.__color["зелёный"])


traffic_ligth = TrafficLight()
traffic_ligth1 = TrafficLight()
traffic_ligth2 = TrafficLight()

print(traffic_ligth is traffic_ligth1)
print(traffic_ligth1 is traffic_ligth2)
print(traffic_ligth2 is traffic_ligth)
