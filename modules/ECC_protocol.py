"""
Author: Wallaby
Created: 2025-09-19
Description: implémentation de la méthode ECC
TODO:   - classe Elliptic Curve avec definition et calcule
        - optimisation du calcule
        - échange de clefs et protocole
"""

class Point:
    """
    equation : y2 = x3 + 486662x2 + x
    point : x = 9
    """
    def __init__(self,coef_A, coef_B, point_G, p):
        self.A = coef_A
        self.B = coef_B
        self.x = point_G[0]
        self.y = point_G[1]
        self.p = p
    

    def __add__(self, point: 'Point'):
        """
        Addition de deux point situer sur la courbe
        """
        up = (point.y - self.y)
        down = (point.x - self.x)
        if down != 1 and down != up :
            down = (down ** (self.p-2)) % self.p
            lam = (up * down) % self.p
        else:
            lam = (up / down) % self.p
        
        print("addition : ",up, down, lam)

        x = (lam**2 - self.x - point.x) % self.p
        y = (lam * (self.x - x) - self.y) % self.p

        return Point(self.A, self.B, (x, y), self.p)
    
    def doubling(self):
        up = (3*(self.x**2) + self.A)
        down = (2*self.y)
        if down != 1 and down != up :
            down = (down ** (self.p-2)) % self.p
            lam = (up * down) % self.p
        else:
            lam = (up / down) % self.p

        x2 = (lam**2 - self.x*2) % self.p
        y2 = (lam * (self.x - x2) - self.y) % self.p

        return Point(self.A, self.B, (x2, y2), self.p)

    def int_to_bin(self, num):
        if num <= 1:
            return str(num)
        return self.int_to_bin(num // 2) + str(num % 2)


    def __mul__(self, coef: int):
        """
        multiplication d'un point avec lui même
        """
        binary = self.int_to_bin(coef)
        print(binary)
        result = None
        for i in range(len(binary)):
            # print(result, binary[i])
            if int(binary[i]):
                temp = self
                print("2^",len(binary)-(i+1))
                for i in range(len(binary)-(i+1)):
                    temp = temp.doubling()
                    print(temp)
                if result == None:
                    result = temp
                else:
                    result += temp 
                print(result)
        return result
    
    def __str__(self):
        return str(self.x)+","+str(self.y)

if __name__ == "__main__":
    point = Point(1,6,(2,4), 997)

    # print(point.int_to_bin(1407279411114289712345678900000982738454854197365687256127597413785197326215693767521367))
    point *= 5
    print(point)




