import graphviz as gv
import courses
from Course import Course


if __name__ == "__main__":

    courses.create_courses()
    graph = gv.Digraph("GT Courses")
    for course in Course.all_courses.values():
        graph.node(course.name, course.description)

    for course in Course.all_courses.values():
        for pre in course.prerequisites:
            graph.edge(pre.name, course.name)

    for course in Course.all_courses.values():
        for co in course.corequisites:
            graph.edge(co.name, course.name, dir="both", style="dashed")

    graph.render('out', view=True)
