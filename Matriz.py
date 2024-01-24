class Matriz:
    def __init__(self, *data) -> None:
        """
         0 1 2 3 4 5 6 7 8
         | | | | 
         V V V V
        [1,2,3,4,5,6,7,8,9]
        Explicar esto
        """
        self.data = []

        n = int(len(data)**(1/2))

        for i in range(n):
            self.data.append([])
            for j in range(n):
                self.data[i].append(data[i*n+j])


    def __init__(self, *data, n, m) -> None:
        pass

        



    def __add__(self, other):
        pass

    def __mul__(self, other: object):
        pass


if __name__ == "__main__":
    pass