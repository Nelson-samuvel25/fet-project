def sum_func(num1,num2):
    try:
        return num1 / num2;
    except (TypeError,ZeroDivisionError)as err:
        return err
    
    