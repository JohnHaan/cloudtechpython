def main():
    try:
        num1 = int(input('input number:'))
        num2 = int(input('input number:'))
        print("result:",num1/num2)

    except ZeroDivisionError as e:
        print("error:",e)
    except ValueError as e1:
        print("input error:",e1)
    else:
        print("unknown error")
    finally:
        print("done")
    
if __name__ == '__main__':
    main()
