universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


# To calculate the total students
# We have to create a list for students from each institution.
def enrollment_stat():
    students_list = [i[1] for i in universities]
    tuition_list = [i[2] for i in universities]
    print(f'Total Students: {sum(students_list):,}')
    print(f'Total Tuition: ${sum(tuition_list):,}')
    print('\n')

    def mean():  # I created a nested function in order to make use of
        # students list and tuition list.
        length1 = len(students_list)
        students_mean = sum(students_list) / length1
        tuition_mean = sum(tuition_list) / length1
        print(f'Student mean: {students_mean:,.2f}')
        print(f'Tuition mean: ${tuition_mean:,.2f}')
        print('\n')

    def median():
        length = len(students_list)
        students_list.sort()
        tuition_list.sort()
        if length % 2 == 0:   # if the length is even
            students_median = (students_list[length // 2 - 1] + students_list[length // 2]) / 2
            tuition_median = (tuition_list[length // 2 - 1] + tuition_list[length // 2]) / 2
            print(f'Students median: {students_median:,}')
            print(f'Tuition median: ${tuition_median:,.2f}')

        else:   # if the length is odd
            students_median = students_list[length // 2]
            tuition_median = tuition_list[length // 2]
            print(f'Student median : {students_median:,}')
            print(f'Tuition median: ${tuition_median:,}')

    mean()
    median()


def main():
    print('*' * 30)
    enrollment_stat()
    print('*' * 30)


main()
