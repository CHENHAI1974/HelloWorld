# Wait for user input to start the programe
input('Press Enter To start...')

# This will print Hello World 100 times
import time
num = 50
for i in range(num):
  print(" "*i + "hello world!")
  time.sleep(0.05)
for i in range(num):
  print(" "*(num-i) + "hello world!")
  time.sleep(0.05)

  
# This line will wait for user input and allow user to see the printed statements
input()
