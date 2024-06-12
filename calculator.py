import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("calculator.log"),
                              logging.StreamHandler()])

def add(num1, num2):
    result = num1 + num2
    logging.debug(f"Add: {num1} + {num2} = {result}")
    return result

def subtract(num1, num2):
    result = num1 - num2
    logging.debug(f"Subtract: {num1} - {num2} = {result}")
    return result

def multiply(num1, num2):
    result = num1 * num2
    logging.debug(f"Multiply: {num1} * {num2} = {result}")
    return result

def divide(num1, num2):
    if num2 == 0:
        logging.error("Divide: Division by zero error")
        raise ValueError("Cannot divide by zero!")
    result = num1 / num2
    logging.debug(f"Divide: {num1} / {num2} = {result}")
    return result
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 

select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if select == 1:
    print("The result is",
                    add(number_1, number_2))
 
elif select == 2:
    print("The result is",
                    subtract(number_1, number_2))
 
elif select == 3:
    print("The result is",
                    multiply(number_1, number_2))
 
elif select == 4:
    print("The result is",
                    divide(number_1, number_2))
else:
    print("Invalid input")
    
if __name__ == "__main__":
    try:
        add(10, 5)
        subtract(10, 5)
        multiply(10, 5)
        divide(10, 0)  
    except Exception as e:
        logging.exception("Exception occurred")