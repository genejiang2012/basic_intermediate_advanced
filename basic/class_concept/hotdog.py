class HotDog:
    def __init__(self):  # 初始化属性
        self.cooked_level = 0
        self.cooked_string = "raw"
        self.condiments = []

    def cooke_dog(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "糊了"
        elif self.cooked_level > 5:
            self.cooked_string = "好了"
        elif self.cooked_level > 3:
            self.cooked_string = "半生不熟"
        else:
            self.cooked_string = "生的"


mydog = HotDog()
print(mydog.cooked_level)

