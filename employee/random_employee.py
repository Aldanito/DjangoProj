from .models import Employee
from .forms import EmployeeForm

from django.core.files import File

import random


FirstName = "Jay", "Jim", "Roy", "Axel", "Billy", "Charlie", "Jax", "Gina", "Paul"

LastName = "Barker", "Style", "Spirits", "Murphy", "Blacker", "Bleacher", "Rogers"

Salary_level_1 = "15000", "14000", "17000"
Salary_level_2 = "10000", "11000", "10500", "9500", "9700", "9200"
Salary_level_3 = "7500", "6500", "6700", "6900", "6850", "7250", "7450", "7350", "7150", "6800"
Salary_level_4 = "4000", "5000", "4200", "4300", "4450", "4550", "4250", "4150", "4600", "4700"
Salary_level_5 = "2000", "3000", "2200", "2300", "2450", "2550", "2250", "2150", "2600", "2700"

Day = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",\

Month = "01", "02", "03", "04", "05", "06", "07", "08",\
        "09", "10", "11", "12"

Year = "2016", "2017", "2018"

folder_name = 'media/ '

folder_name = folder_name.strip()


img_file_name = "001", "002", "003", "005", "006", "007", "008", "009", "010"


def run_random():
    count_one = 0
    for i_one in range(5):
        count_one = count_one + 1
        First = random.choice(FirstName)
        Last = random.choice(LastName)
        Employee_Salary_level_1 = random.choice(Salary_level_1)
        Employee_Year = random.choice(Year)
        Employee_Month = random.choice(Month)
        Employee_Day = random.choice(Day)
        form = EmployeeForm(data={'name': First + ' ' + Last, 'employment_position': "level 1", 'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_1})
        form.save()
        img_name = random.choice(img_file_name)
        file_name = folder_name +img_name + '.jpg'
        file_name = file_name[0:5]+file_name[5:]
        reopen = open(file_name, "rb")
        django_file = File(reopen)
        current_child_len = Employee.objects.order_by('date_added')
        current_child_id = current_child_len[(len(current_child_len) - 1)]
        boss_level_1_id = current_child_id.id
        boss_level_1 = Employee.objects.get(id=current_child_id.id)
        #print(boss_level_1.name)
        boss_level_1.employment_photo.save(img_name + '.jpg', django_file, save=True)
        reopen.close()
        boss_level_1.move_to(None, 'left')
        boss_level_1.save()

        count_two = 0
        for i_two in range(3):
            count_two = count_two + 1
            #print('count_two - ', count_two)
            First = random.choice(FirstName)
            Last = random.choice(LastName)
            Employee_Salary_level_2 = random.choice(Salary_level_2)
            Employee_Year = random.choice(Year)
            Employee_Month = random.choice(Month)
            Employee_Day = random.choice(Day)
            try:
                form = EmployeeForm(data={'name': First + ' ' + Last, 'employment_position': "level 2", 'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_2})
                form.save()
                img_name = random.choice(img_file_name)
                file_name = folder_name + img_name + '.jpg'
                reopen = open(file_name, "rb")
                django_file = File(reopen)
                current_child_len = Employee.objects.order_by('date_added')
                current_child_id = current_child_len[(len(current_child_len) - 1)]
                boss_level_2_id = current_child_id.id
                boss_level_2 = Employee.objects.get(id=current_child_id.id)
                boss_level_2.employment_photo.save(img_name + '.jpg', django_file, save=True)
                reopen.close()
                boss_level_1 = Employee.objects.get(id=boss_level_1_id)
                boss_level_2.move_to(boss_level_1, 'first-child')
                boss_level_2.save()
                #print('boss - ', boss_level_1)
                #print('child - ', boss_level_2)
            except:
                print('some bad')

            count_three = 0
            for i_three in range(3):
                count_three = count_three + 1
                #print('count_three - ', count_three)
                First = random.choice(FirstName)
                Last = random.choice(LastName)
                Employee_Salary_level_3 = random.choice(Salary_level_3)
                Employee_Year = random.choice(Year)
                Employee_Month = random.choice(Month)
                Employee_Day = random.choice(Day)
                try:
                    form = EmployeeForm(data={'name': First + ' ' + Last, 'employment_position': "level 3", 'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_3})
                    form.save()
                    img_name = random.choice(img_file_name)
                    file_name = folder_name + img_name + '.jpg'
                    reopen = open(file_name, "rb")
                    django_file = File(reopen)
                    current_child_len = Employee.objects.order_by('date_added')
                    current_child_id = current_child_len[(len(current_child_len) - 1)]
                    boss_level_3_id = current_child_id.id
                    boss_level_3 = Employee.objects.get(id=current_child_id.id)
                    boss_level_3.employment_photo.save(img_name + '.jpg', django_file, save=True)
                    reopen.close()
                    boss_level_2 = Employee.objects.get(id=boss_level_2_id)
                    boss_level_3.move_to(boss_level_2, 'first-child')
                    boss_level_3.save()
                    #print('boss - ', boss_level_2)
                    #print('child - ', boss_level_3)
                except:
                    print('some bad')

                count_four = 0
                for i_four in range(4):
                    count_four = count_four + 1
                    #print('count_four - ', count_four)
                    First = random.choice(FirstName)
                    Last = random.choice(LastName)
                    Employee_Salary_level_4 = random.choice(Salary_level_4)
                    Employee_Year = random.choice(Year)
                    Employee_Month = random.choice(Month)
                    Employee_Day = random.choice(Day)
                    try:
                        form = EmployeeForm(data={'name': First + ' ' + Last, 'employment_position': "level 4", 'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_4})
                        form.save()
                        img_name = random.choice(img_file_name)
                        file_name = folder_name + img_name + '.jpg'
                        reopen = open(file_name, "rb")
                        django_file = File(reopen)
                        current_child_len = Employee.objects.order_by('date_added')
                        current_child_id = current_child_len[(len(current_child_len) - 1)]
                        boss_level_4_id = current_child_id.id
                        boss_level_4 = Employee.objects.get(id=current_child_id.id)
                        boss_level_4.employment_photo.save(img_name + '.jpg', django_file, save=True)
                        reopen.close()
                        boss_level_3 = Employee.objects.get(id=boss_level_3_id)
                        boss_level_4.move_to(boss_level_3, 'first-child')
                        boss_level_4.save()
                        #print('boss - ', boss_level_3)
                        #print('child - ', boss_level_4)
                    except:
                        print('some bad')

                    count_five = 0
                    for i_five in range(5):
                        count_five = count_five + 1
                        #print('count_five - ', count_five)
                        First = random.choice(FirstName)
                        Last = random.choice(LastName)
                        Employee_Salary_level_5 = random.choice(Salary_level_5)
                        Employee_Year = random.choice(Year)
                        Employee_Month = random.choice(Month)
                        Employee_Day = random.choice(Day)
                        try:
                            form = EmployeeForm(data={'name': First + ' ' + Last, 'employment_position': "level 5", 'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day, 'salary': Employee_Salary_level_5})
                            print('name - ',First, ' ', Last)
                            form.save()
                            img_name = random.choice(img_file_name)
                            file_name = folder_name + img_name + '.jpg'
                            reopen = open(file_name, "rb")
                            django_file = File(reopen)
                            current_child_len = Employee.objects.order_by('date_added')
                            current_child_id = current_child_len[(len(current_child_len) - 1)]
                            #boss_level_5_id = current_child_id.id
                            boss_level_5 = Employee.objects.get(id=current_child_id.id)
                            boss_level_5.employment_photo.save(img_name + '.jpg', django_file, save=True)
                            reopen.close()
                            boss_level_4 = Employee.objects.get(id=boss_level_4_id)
                            boss_level_5.move_to(boss_level_4, 'first-child')
                            boss_level_5.save()
                            #print('boss - ', boss_level_4)
                            #print('child - ', boss_level_5)
                        except:
                            print('some bad')
run_random()
