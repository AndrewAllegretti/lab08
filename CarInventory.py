from Car import Car
from CarInventoryNode import CarInventoryNode


class CarInventory:
    def __init__(self):
        self.root = None

    def __addCar(self, car, current):

        if current is None:
            return CarInventoryNode(car)

        elif current.car.make == car.make and current.car.model == car.model:
            current.cars.append(car)

        elif current.car < car:
            current.right = self.__addCar(car, current.right)

        else:
            current.left = self.__addCar(car, current.left)

        return current

    def addCar(self, car):
        self.root = self.__addCar(car, self.root)

    def __inOrder(self, current):
        if current:
            return f'{self.__inOrder(current.left)}{str(current)}{self.__inOrder(current.right)}'
        else:
            return ''

    def inOrder(self):
        return self.__inOrder(self.root)



    def preOrder(self):
        return self.__preOrder(self.root)



    def __preOrder(self, current):
        if current:
            return f'{str(current)}{self.__preOrder(current.left)}{self.__preOrder(current.right)}'
        else:
            return ''



    def postOrder(self):
        return self.__postOrder(self.root)



    def __postOrder(self, current):
        if current:
            return f'{self.__postOrder(current.left)}{self.__postOrder(current.right)}{str(current)}'
        else:
            return ''



    def __getBestCar(self, car, current):

        if current is not None:

            if car.model == current.model and car.make == current.make:

                bestCar = current.car
                for myCar in current.cars:
                    if bestCar.year < myCar.year:
                        bestCar = myCar
                    elif bestCar.year == myCar.year and bestCar.price < myCar.price:
                        bestCar = myCar

                return bestCar

            elif car < current.car:
                return self.__getBestCar(car, current.left)

            else:
                return self.__getBestCar(car, current.right)



    def getBestCar(self, make, model):

        carToBeSearched = Car(make, model, 0, 0)

        return self.__getBestCar(carToBeSearched, self.root)



    def __getWorstCar(self, car, current):

        if current is not None:

            if car.model == current.model and car.make == current.make:

                worstCar = current.car
                for myCar in current.cars:
                    if worstCar.year > myCar.year:
                        worstCar = myCar
                    elif worstCar.year == myCar.year and worstCar.price > myCar.price:
                        worstCar = myCar

                return worstCar

            elif car < current.car:
                return self.__getWorstCar(car, current.left)

            else:
                return self.__getWorstCar(car, current.right)



    def getWorstCar(self, make, model):

        carToBeSearched = Car(make, model, 0, 0)

        return self.__getWorstCar(carToBeSearched, self.root)



    def __getTotalInventoryPrice(self, current):
        if current:

            sum = 0
            for car in current.cars:
                sum += car.price

            return self.__getTotalInventoryPrice(current.left) + sum + self.__getTotalInventoryPrice(current.right)
        else:
            return 0



    def getTotalInventoryPrice(self):
        return self.__getTotalInventoryPrice(self.root)



    def __doesCarExist(self, car, current):
        if current is not None:

            if current.car.model == car.model and current.car.make == car.make:

                for myCar in current.cars:

                    if myCar.year == car.year and myCar.price == car.price:
                        return True

                return False

            elif current.car > car:
                return self.__doesCarExist(car, current.left)

            else:
                return self.__doesCarExist(car, current.right)
        return False



    def doesCarExist(self, car):
        return self.__doesCarExist(car, self.root)

