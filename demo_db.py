from batch import Batch

class DemoDB:

    def __init__(self):
        self.__batch = Batch()
        self.__batches = []
        self.__students = []

    def existing_records(self):
        # batch info
        self.__batch.b_id = 1001
        self.__batch.b_name = "Corvit Python"
        # course info
        self.__batch.course.c_id = 101
        self.__batch.course.c_name = "Python"
        self.__batch.course.credits = 5
        # teacher info 
        self.__batch.teacher.p_id = 11
        self.__batch.teacher.name = "Bilal"
        self.__batch.teacher.cnic = "33103-1234567-1"
        self.__batch.teacher.fullAddress.city = "Fsd"
        self.__batch.teacher.fullAddress.country = "Pak"
        self.__batch.teacher.salary = 20000
        # student info 
        self.__batch.student.p_id = 1
        self.__batch.student.name = "Anas"
        self.__batch.student.cnic = "33103-1234567-2"
        self.__batch.student.fullAddress.city = "Lhr"
        self.__batch.student.fullAddress.country = "Pak"
        self.__batch.student.cgpa = 3.8
        self.__batch.student.fee = 40000

        self.__students.append(self.__batch.student)
        self.__batches.append(self.__batch)

    def display_all_records(self):
        records = ""
        batches_len = len(self.__batches)
        students_len = len(self.__students)
        for i in range(batches_len):
            records += "** Batach Info ** \n"
            records += "Batch Id: " + str(self.__batches[i].b_id) + "\n"
            records += "** Student Info ** \n"
            records += "Student Name: " + self.__batches[i].student.name

        return records

    def add_new_batch(self, new_batch):
        self.__batches.append(new_batch)

    def search_student_record(self):
        pass