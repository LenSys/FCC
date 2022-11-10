import re

def arithmetic_arranger(problems, showAnswers = False):
    arranged_problems = ''

    first_line = ''
    second_line = ''
    third_line = ''
    answers_line = ''
    problemsLength = 0
    errorMessage = ''
    for problem in problems:
      if "+" not in problem and "-" not in problem:
          errorMessage = "Error: Operator must be '+' or '-'."
          break
        
      problem_parts = problem.split('+')
      operator = '+'
      if len(problem_parts) == 1:
        problem_parts = problem.split('-')
        operator = '-'

      number_1 = problem_parts[0].strip()
      number_2 = problem_parts[1].strip()

      invalidNumberResult_1 = re.findall("([a-z]+)", number_1)
      if len(invalidNumberResult_1) > 0:
        errorMessage = "Error: Numbers must only contain digits."
        break

      invalidNumberResult_2 = re.findall("([a-z]+)", number_2)
      if len(invalidNumberResult_2) > 0:
        errorMessage = "Error: Numbers must only contain digits."
        break

      if len(number_1) > 4 or len(number_2) > 4:
        errorMessage = "Error: Numbers cannot be more than four digits."
      
      problemsLength = problemsLength + 1
      
      if operator == '+':
        answer = str(int(number_1) + int(number_2))
      else:
        answer = str(int(number_1) - int(number_2))
        
      maxNum = max([len(number_1), len(number_2)])
      
      number_1 = number_1.rjust(maxNum + 2,' ')
      number_2 = number_2.rjust(maxNum,' ')
      answer = answer.rjust(maxNum + 2,' ')

      # There should be four spaces between each problem
      spacesAfterProblem = '    '
      
      first_line = first_line + number_1 + spacesAfterProblem
      second_line = second_line + operator + ' ' + number_2 + spacesAfterProblem
      third_line = third_line + ''.rjust(maxNum + 2,'-') + spacesAfterProblem

      if showAnswers:
        answers_line = answers_line + answer + spacesAfterProblem
  
    if len(errorMessage) > 0:
      arranged_problems = errorMessage
    else:
      arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()

      if showAnswers:
        arranged_problems = arranged_problems + "\n" + answers_line.rstrip()
  
    if problemsLength > 5:
      arranged_problems = "Error: Too many problems."
    
  
    return arranged_problems