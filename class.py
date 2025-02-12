class student_details:
    def sutd_name(self):
        print("sripriya,hema,sandy,narmatha")
class department_details(student_details):
    def dep_name(self):
        print("bsc,mca,bca,ece")
class project_details(department_details):
    def pro_name(self):
        print("java,sql,python,r program")
obj=department_details()
obj.dep_name()
obj.sutd_name()