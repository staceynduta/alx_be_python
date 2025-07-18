
#_ OBJECTIVE: LEARN TO USE MATCH CASE STATEMENTS FOR HANDLING MULTIPLE OPERATIONS IN A SIMPLE CALCULATOR PROGRAM.


#! DEVELOP A PYTHON SCRIPT NAMED MATCH_CASE_CALCULATOR.PY. 
#! THIS CALCULATOR WILL PROMPT THE USER TO ENTER TWO NUMBERS AND SELECT AN OPERATION (ADDITION, SUBTRACTION, MULTIPLICATION, OR DIVISION). 
#! THE SCRIPT WILL THEN PERFORM THE SELECTED OPERATION USING A MATCH CASE STATEMENT AND DISPLAY THE RESULT.


#* TASK DESCRIPTION:

#! ASK THE USER TO INPUT TWO NUMBERS (ONE AT A TIME) USING: ENTER THE FIRST NUMBER: ENTER THE SECOND NUMBER:

num1 = int(input('enter the first number:'))  
num2 = int(input('enter the second number:'))

#! ASK FOR THE TYPE OF OPERATION THEY’D LIKE TO PERFORM: CHOOSE THE OPERATION (+, -, *, /):.

operation = input('choose the operation (+, -, *, /):')

#! IMPLEMENT A MATCH CASE STATEMENT THAT EXECUTES THE CHOSEN OPERATION BASED ON THE USER’S INPUT.

match operation: 
    case '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case '-':
        result = num1 - num2
        print(f'The result is {result}.')
    case '*':
        result = num1 * num2
        print(f'The result is {result}.')
    case '/':
        if num2 != 0:
            result =num1 / num2
            print(f'The result is {result}.')
        else:
            print('Cannot divide by zero.')