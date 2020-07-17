
def FinalGrades(per): 
    if per>= 70:
        return 'Congratulations! You got an A'
    elif per>= 60:
        return 'You got a B'
    elif per>= 50:
        return 'You got a C'
    elif per>= 40:
        return 'You got a D'
    else:
        return 'Unfortunately you failed and will need to resit the exam'


def get_grades():
  maths = int(input('Math grade: '))
  chemistry = int(input('Chemistry grade: '))
  physics = int(input('Physics grade: '))

  Ask = maths + chemistry + physics
  return Ask/3

percent = get_grades()
grade = FinalGrades(percent)
print (grade))
