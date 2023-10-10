"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: Malcolm White
Date: 10/10/2023
Usage: 
"""

import logging

data = [] 
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20

file = None



#LECTURE SECTION 1
logging.basicConfig(level = logging.DEBUG,
                    filename = 'app.log',
                    filemode = 'w',
                    format = '%(asctime)s - %(levelname)s - %(message)s') 


try:   
      file = open('module_4_data.txt')
      data = file.readlines()

      1 / 0

except FileNotFoundError as e:               # Most specific to least specific order
      # print('Error opening file: ', e)
      logging.error(e)
except Exception as e:                       # Last exception
      # print('General Exception: ', e)
      logging.error(e)
finally:
      if file is not None:                   # Will occur regardless
            file.close()                     # If file was opened, we can still close it
            # print("File Closed")
            logging.info('File Closed')



#LECTURE SECTION 2
# CEO/Chair of Board,Jo-Anne Sinclair,140000 < format
try:
      if len(data) == 0:
            raise Exception("No data exists.")
      else: 
            for record in data:
                  items = record.split(',')
                  title = items[0]
                  name = items[1]
                  salary = float(items[2])         # Use if / else for assignment 4

                  #LECTURE SECTION 3
                  #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
                  #timestamp WARNING Jo-Anne Sinclair's salary 140000.0 is currently above blah
                  if salary > HIGH_SALARY:
                        logging.warning(f"{name}'s salary {salary} "
                                        + f"is currently above "
                                        + f"the reccomended maximum of "
                                        + f"{HIGH_SALARY}.")

                  salary *= (1 - RECOMMENDED_INCREASE)
                  new_data.append([title,name,salary])
except Exception as e:
      # print(e)
      logging.error(e)



#LECTURE SECTION 4
try: 
      file = open('updated_salaries.txt', 'w')
      for record in new_data:
            row = ""
            for index, item in enumerate(record):
                  row += str(item)
                  if index < len(record) - 1:
                        row += (",")
            row += '\n'
            file.write(row)
except Exception as e:
      # print(e)
      logging.error(e)



#LECTURE SECTION 5
logging.debug('Debug level logging.')
logging.info('Info level logging.')
logging.warning('Warning level logging.')
logging.error('Error level logging.')
logging.critical('Critical level logging.')

print("End of Program")

