# set PYTHONPATH=C:\python_web
# python module_package\module_ex.py

# echo. > __init__.py
# echo. > module_package\__init__.py

from python_basic.module_package import fah_converter

if __name__ == "__main__":
    print ("Enter a celsius value: "),
    celsius = float(input())
    fahrenheit = fah_converter.covert_c_to_f(celsius) # my_module의 c_to_f 호출
    print ("That's ", fahrenheit, " degrees Fahrenheit")
