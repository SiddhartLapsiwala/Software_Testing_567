import unittest


def classify_triangle(sideA, sideB, sideC):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return result[Type] as 'Equilateral'
        If exactly one pair of sides are equal, return result[Type] as'Isoceles'
        If no pair of  sides are equal, return result[Type] as 'Scalene'
        If not a valid triangle, then return result[Type] as 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return result[RightTriangle] as True

    """
    result = dict()
    if sideA + sideB <= sideC or sideA + sideC <= sideB or sideB + sideC <= sideA:
        result["Type"] = "Not Triangle"
        result["RightTriangle"] = False
    else:
        if sideA == sideB == sideC:
            result["Type"] = "Equilateral"
        elif (sideA == sideB) or (sideB == sideC) or (sideC == sideA):
            result["Type"] = "Isosceles"
        else:
            result["Type"] = "Scalene"

        if ((sideA*sideA) + (sideB*sideB)) == (sideC*sideC):
            result["RightTriangle"] = True
        elif ((sideB*sideB) + (sideC*sideC)) == (sideA*sideA):
            result["RightTriangle"] = True
        elif ((sideC*sideC) + (sideA*sideA)) == (sideB*sideB):
            result["RightTriangle"] = True
        else:
            result["RightTriangle"] = False

    return result


class FractionTest(unittest.TestCase):
    def test_not_triangle(self):
        """ test for side does not form triangle """
        result = classify_triangle(2, 3, 9)
        self.assertEqual(result.get("Type"), 'Not Triangle')

    def test_triangle_equilateral(self):
        """ test for Equilateral triangle """
        result = classify_triangle(3, 3, 3)
        self.assertEqual(result.get("Type"), 'Equilateral')
        self.assertFalse(result.get("RightTriangle"))

    def test_triangle_isoceles(self):
        """ test for Isoceles triangle """
        result = classify_triangle(3, 3, 5)
        self.assertEqual(result.get("Type"), 'Isosceles')
        self.assertFalse(result.get("RightTriangle"))

    def test_triangle_scalene(self):
        """ test for Scalene triangle """
        result = classify_triangle(3, 4, 6)
        self.assertEqual(result.get("Type"), 'Scalene')
        self.assertFalse(result.get("RightTriangle"))

    def test_triangle_scalene_right(self):
        """ test for Scalene Right triangle """
        result = classify_triangle(3, 4, 5)
        self.assertEqual(result.get("Type"), 'Scalene')
        self.assertTrue(result.get("RightTriangle"))


def get_number(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Invalid Value!! Please enter valid Integer Value")


def main():

    sideA = get_number("Enter A side of Triangle: ")
    sideB = get_number("Enter B side of Triangle: ")
    sideC = get_number("Enter C side of Triangle: ")

    result = classify_triangle(sideA, sideB, sideC)
    print("Result :: \n")
    print("Entered Triangle with length of side as (" + str(sideA) + "," + str(sideB) + "," + str(sideC) + ") is ")
    print(result.get("Type"))
    if result.get("Type") != "Not Triangle":
        if result.get("RightTriangle"):
            print("It is also Right Angle Triangle")
        else:
            print("It is also not Right Angle Triangle")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)