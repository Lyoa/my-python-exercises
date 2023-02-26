# class Student:
#     def __init__(self, name, gender, course):
#         self._first_name = first_name
#         self._last_name = last_name
#         self._gender = gender
#         self._course = course
#         pass

#     @property
#     def name(self):
#         return f'{self._first_name} {self._last_name}'
#         pass

#     @name.setter
#     def name(self, value):
#         first_name, last_name = value.split()
#         self._first_name = first_name
#         self._last_name = last_name
#         pass

#     @property
#     def gender(self):
#         return self._gender
#         pass

#     @gender.setter
#     def gender(self, value):
#         self._gender = value
#         pass

#     @property
#     def course(self):
#         return self._course
#         pass

#     @course.setter
#     def course(self, value):
#         self._course = value
#         pass

# class Student:
#     def __init__(self, fname, lname, gender, course):
#         self.fname = fname
#         self.lname = lname
#         self.gender = gender
#         self.course = course

#     @property
#     def name(self):
#         return f'{self.fname} {self.lname}'

#     @property
#     def gender(self):
#         return self.gender

#     @property
#     def course(self):
#         return self.course

# class Student:
#     def __init__(self, first_name="", last_name="", gender="", course=""):
#         self._first_name = first_name
#         self._last_name = last_name
#         self._gender = gender
#         self._course = course

#     @property
#     def name(self):
#         return f'{self._first_name} {self._last_name}'

#     @name.setter
#     def name(self, value):
#         first_name, last_name = value.split()
#         self._first_name = first_name
#         self._last_name = last_name

#     @property
#     def gender(self):
#         return self._gender

#     @gender.setter
#     def gender(self, value):
#         self._gender = value

#     @property
#     def course(self):
#         return self._course

#     @course.setter
#     def course(self, value):
#         self._course = value

class Student:
    def __init__(self, name, gender, course):
        self._name = name
        self._gender = gender
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value

