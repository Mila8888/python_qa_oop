class Figure:
    name = None

    def get_area(self):
        pass

    def add_area(self, figure):
        joint_area = self.get_area + figure.get_area
        return joint_area
