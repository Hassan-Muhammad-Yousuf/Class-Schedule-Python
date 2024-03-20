class Data:
    ''' '''
class Schedule:
    ''' '''
class Population:
    ''' '''
class GeneticAlgorithm:
    ''' '''
class Course:
    def __init__(self, number, name, instructors, maxNumberOfStudents):
        self._number = number
        self._name = name
        self._instructors = instructors
        self._maxNumberOfStudents = maxNumberOfStudents
    def get_number(self):
        return self._number
    def get_name(self):
        return self._name
    def get_instructors(self):
        return self._instructors
    def get_maxNumberOfStudents(self):
        return self._maxNumberOfStudents
    def __str__(self):
        return self._name
class Instructor:
    ''' '''
class Room:
    ''' '''
class MeetingTime:
    ''' '''
class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses
    def get_name(self):
        return self._name
    def get_courses(self):
        return self._courses
class Class:
    ''' '''