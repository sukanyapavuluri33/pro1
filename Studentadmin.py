import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
       writer=csv.writer(csv_file)
       if csv_file.tell() == 0:
          writer.writenow(["Name","Age","Contact Number","E-Mail ID"])
       writer.writerow(info_list)
if __name__=='__main__':
   condition=True
   student_num = 1

   while(condition):
       student_info=input("enter student infomtion for student #{} in the following format (Name Age Contact_Number E_mail_ID): ".format(student_num))
      # print("Entered Information" +student_info)

       student_info_list=student_info_split('')
      # print("entered split up  information is "+str(student_info_list))
       print("\n the entered information is -\nName: {}\nAge: {}\nContact_Number: {}\nE-Mail ID: {}"
       .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
      choice_check = print("Is the entered information correct? (Yes/No:")
      if choice_check == "Yes":
         write_into_csv(student_info_list)
         condition_check=input("enter (yes/no) if you want to enter information for another student: ")
         if condition_check=="yes":
          condition=True
          student_num = student_num + 1
         elif condition_check=="no":
          condition=False
      elif choice_check == "No":
         print("\nplease re-enter the values!")  
