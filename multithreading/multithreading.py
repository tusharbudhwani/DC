import threading
import time

def cubes(num):
    print(num**3)

def square(num):
    print(num**2)

#Create and start threads
square_thread = threading.Thread(target=square, args=(100000,))
cube_thread = threading.Thread(target=cubes, args=(200000,))

square_thread.start()
print("thread 1 executed")
cube_thread.start()
print("thread 2 executed")

#wait for other threads to finish
square_thread.join()
cube_thread.join()