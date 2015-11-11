"""
:Author: Joshua Morton
"""


class And(object):
    """
    represents a set of prerequisites that must be taken together
    """
    def __init__(self, *components):
        """
        initializes the And object

        self - the And
        components: List[Union[Course, Or]] - the set of prerequisites that
        must each be taken
        """
        self.courses = frozenset(components)

    def __iter__(self):
        return self.courses.__iter__()


class Or(object):
    all_ors = dict()

    def __init__(self, *components):
        """
        initializes an Or object representing a set of courses of which only
        one must be taken

        self - the Or object
        name:str - the internal name for the object, should be unique
        components:List[Union[And, Course]] - the courses that combine to make
            up the Or, for example the probability and statistics requirement
            can be fulfilled using MATH3670, ISYE 3770, ISYE 2027 AND ISYE
            202uU8 or various other options

        In addition to setting the name and components, it constructs a course
            object for use when rendering the graph of courses
        """

        """
        In the uncommon but possible case where a class has an And of
            prerequisites, but one of those prerequisites is an Or, and that Or
            itself contains another And, there's special proceessing that needs
            to be done. Namely, for rendering as a graph on screen, we need to
            create a virtual course named "AND" that is a child of the "OR", so
            that the graph is human-parsable.
        """
        newcomponents = []
        for course in components:
            if isinstance(course, And):
                newcomponents.append(Course("("+" & ".join(c.name for c in
                                     course.courses)+")", 0,
                                     prerequisites=course.courses,
                                     description="AND"))
                newcomponents[-1].height -= 1
            else:
                newcomponents.append(course)

        self.courses = frozenset(newcomponents)

        if self.courses not in Or.all_ors:
            Or.all_ors[self.courses] = Course(
                " | ".join(c.name for c in sorted(self.courses,
                           key=lambda x: x.name)), 0,
                prerequisites=newcomponents, description="OR")

        self.course = Or.all_ors[self.courses]
        self.course.height -= 1
        # the course created doesn't actually
        # contribute to the time it takes to complete
        # complete later course

    def __iter__(self):
        return self.courses.__iter__()

    def __getattr__(self, key):
        try:
            return object.__getattribute__(self, key)
        except AttributeError:
            return self.course.__getattribute__(key)


class Course(object):
    """
    Represents a course
    
    name - the name of the course, this must be unique
    hours - number of credit hours
    prerequisites - a set of prerequisites, must be an And object or None by
        default
    corequisites - a set of corequisite courses, must be an And object or None
        by default
    description - a short string, either the course name, or "AND" or "OR", for
        rendering the graph on screen
    """
    all_courses = dict()

    def __init__(self, name, hours, prerequisites=None, corequisites=None,
                 description=None):
        """
        """
        if prerequisites is None:
            self.prerequisites = frozenset()
        else:
            self.prerequisites = prerequisites
        self.corequisites = corequisites or frozenset()
        self.height = None  # chain of prerequisites
        self.hours = hours  # class hours

        if prerequisites is None:
            self.height = 0
        else:
            self.height = max(req.height for req in prerequisites) + 1
        self.name = name

        if description is None:
            self.description = self.name
        else:
            self.description = description
        Course.all_courses[name] = self

    def __str__(self):
        return self.name + " (" + self.description + ")"

    def __repr__(self):
        return self.__str__()
