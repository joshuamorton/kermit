import unittest
from ..Course import Course, And, Or


class Test_Course(unittest.TestCase):
    def setUp(self):
        self.course = Course("CS1301", 3,
                             description="An Introductory python course")

    def tearDown(self):
        Course.all_courses = dict()

    def test_instantiation(self):
        self.assertEqual(len(Course.all_courses), 1)
        self.assertEqual(Course.all_courses[self.course.name], self.course)
        self.assertEqual(type(self.course.prerequisites), type(And()))
        self.assertEqual(self.course.name, "CS1301")
        self.assertEqual(self.course.hours, 3)
        self.assertEqual(self.course.description,
                         "An Introductory python course")
        self.assertEqual(str(self.course), 
                         "CS1301 (An Introductory python course)")
        self.assertEqual(self.course.__repr__(),
                         "CS1301 (An Introductory python course)")

    def test_no_name(self):
        course = Course("CS1332", 3)
        self.assertEqual(course.description, "CS1332")

    def test_prerequisites(self):
        course = Course("CS1331", 3, prerequisites=And(self.course))
        self.assertEqual(len(Course.all_courses), 2)
        self.assertListEqual([i for i in course.prerequisites], [self.course])

    def test_and(self):
        my_and = And(1, 2, 3)
        self.assertEqual(set([i for i in my_and]), {1, 2, 3})

    def test_or_courses(self):
        CS1332 = Course("CS1332", 3)
        CS2110 = Course("CS2110", 3)
        my_or = Or(CS1332, CS2110)

        self.assertEqual(my_or.hours, 0)
        self.assertSetEqual({x for x in my_or.prerequisites}, {CS1332, CS2110})
        self.assertSetEqual({x for x in my_or}, {CS1332, CS2110})

    def test_or_and(self):
        CS1332 = Course("CS1332", 3)
        CS2110 = Course("CS2110", 3)
        my_or = Or(And(CS1332, CS2110))
        self.assertEqual(my_or.hours, 0)
        self.assertEqual(my_or.height, 0)

    def test_complex_and_or_course_consistency(self):
        """
        A weird situation involving nested Ands and Ors that can cause problems

        Catches a wonky situation where an And is contained within an Or is
        contained by an And, and you get extra courses appearing out of nowhere
        on the rendered graph
        """
        CS0 = Course("0", 1)
        CS1 = Course("1", 1)
        CS2 = Course("2", 1)
        CS3 = Course("3", 1)
        CS4 = Course("4", 1, And(CS3, Or(And(CS0, CS1), CS2)))
        CS5 = Course("5", 1, And(Or(CS2, And(CS0, CS1)), CS3))
        self.courses = [CS0, CS1, CS2, CS3, CS4, CS5]
        self.assertEqual(CS5.prerequisites.courses, CS4.prerequisites.courses)

    def test_corequisites(self):
        CS1 = Course("1", 1)
        CS12 = Course("2", 2, corequisites=And(CS1))

        self.assertEqual(CS12.corequisites, And(CS1))
        self.assertEqual(CS1.corequisites, And(CS12))
