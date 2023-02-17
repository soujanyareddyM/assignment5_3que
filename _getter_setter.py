class Student:
    def _init_(self):
        self._name = None
        self._rollNumber = None

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getRollNumber(self):
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber



student = Student()


student.setName("John")

student.setRollNumber(57)


name = student.getName()
rollNumber = student.getRollNumber()


print("Name:", name)

print("Roll Number:", rollNumber)