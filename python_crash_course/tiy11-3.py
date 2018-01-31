'''
11-3. Employee: Write a class called Employee . The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee . Write two test methods, test_give_
default_raise() and test_give_custom_raise() . Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.
'''
import unittest

class Employee():
    """Class to represent a company employee"""

    def __init__(self, first, last, salary):
        self.firstname = first
        self.lastname = last
        self.salary = salary

    def give_raise(self, increase=5000):
        """Raise the salary by the provided amount or $5000"""
        self.salary += increase
    
    def get_salary(self):
        """Return the salary"""
        return self.salary

    def get_formatted_name(self):
        """Generate a neatly formatted full name"""
        full_name = self.firstname + ' ' + self.lastname
        return full_name.title()


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class"""
    
    def setUp(self):
        """Create an Employee"""
        self.my_employee = Employee('Stephen', 'Donovan', 40000)

    def test_give_default_raise(self):
        """Test that the default $5000 increse works"""
        self.my_employee.give_raise()
        self.assertEqual(45000, self.my_employee.get_salary())

    def test_give_custom_raise(self):
        """Test that any value raise can be applied"""
        self.my_employee.give_raise(20000)
        self.assertEqual(60000, self.my_employee.get_salary())

    def test_formatted_name(self):
        """Test that names are generated correctly"""
        self.assertEqual('Stephen Donovan', self.my_employee.get_formatted_name())

unittest.main()
