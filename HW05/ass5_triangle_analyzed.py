"""Assignment5 Static Code Analysis"""
import unittest


def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return result[Type] as 'Equilateral'
        If exactly one pair of sides are equal, return result[Type] as'Isoceles'
        If no pair of  sides are equal, return result[Type] as 'Scalene'
        If not a valid triangle, then return result[Type] as 'NotATriangle'
        If the sum of any two sides equals the squate of the third side,
        then return result[RightTriangle] as True

    """
    result = dict()
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        result["Type"] = "Not Triangle"
        result["RightTriangle"] = False
    else:
        if side_a == side_b == side_c:
            result["Type"] = "Equilateral"
        elif (side_a == side_b) or (side_b == side_c) or (side_c == side_a):
            result["Type"] = "Isosceles"
        else:
            result["Type"] = "Scalene"

        if ((side_a * side_a) + (side_b * side_b)) == (side_c * side_c):
            result["RightTriangle"] = True
        elif ((side_b * side_b) + (side_c * side_c)) == (side_a * side_a):
            result["RightTriangle"] = True
        elif ((side_c * side_c) + (side_a * side_a)) == (side_b * side_b):
            result["RightTriangle"] = True
        else:
            result["RightTriangle"] = False

    return result


class FractionTest(unittest.TestCase):
    """TestCases"""
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

    def test_triangle_scalene_right1(self):
        """ test for Scalene Right triangle """
        result = classify_triangle(5, 3, 4)
        self.assertEqual(result.get("Type"), 'Scalene')
        self.assertTrue(result.get("RightTriangle"))

    def test_triangle_scalene_right2(self):
        """ test for Scalene Right triangle """
        result = classify_triangle(4, 3, 5)
        self.assertEqual(result.get("Type"), 'Scalene')
        self.assertTrue(result.get("RightTriangle"))

    def test_triangle_scalene_right3(self):
        """ test for Scalene Right triangle """
        result = classify_triangle(4, 5, 3)
        self.assertEqual(result.get("Type"), 'Scalene')
        self.assertTrue(result.get("RightTriangle"))


def get_number(text):
    """To get validate input"""
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Invalid Value!! Please enter valid Integer Value")


def main():
    """Main method"""
    side_a = get_number("Enter A side of Triangle: ")
    side_b = get_number("Enter B side of Triangle: ")
    side_c = get_number("Enter C side of Triangle: ")

    result = classify_triangle(side_a, side_b, side_c)
    print("Result :: \n")
    print("Entered Triangle with "
          "length of side as (" + str(side_a) + "," + str(side_b) + "," + str(side_c) + ") is ")
    print(result.get("Type"))
    if result.get("Type") != "Not Triangle":
        if result.get("RightTriangle"):
            print("It is also Right Angle Triangle")
        else:
            print("It is also not Right Angle Triangle")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)
