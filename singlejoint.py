# This is a sample Python script.
import numpy as np
import queue
from threading import Thread
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def changeDir():
        while True:
            angle = int(input("desired angle"))
            q.put(angle)

    q = queue.Queue()
    t2 = Thread(target=changeDir)
    t2.start()
    IP = [0, 0, 0, 90, 0, 0, 0]
    tf = 4


    goal = 40
    t0 = 0
    qdot = 0
    t = t0
    v0 = 0
    q_i = 0
    q_f = q_i + goal
    q_dot_i = 0
    q_dot_f = 0
    q_dotdot_i = 0
    q_dotdot_f = 0
    t_array = np.arange(0, tf, 0.005)
    while True:
        goal = q.get()
        q_i = 0
        q_dot_i = 0
        q_dotdot_i = 0
        q_f = goal
        i = 0

        while i <= len(t_array):
            if q.empty() == False:
                goal = q.get()
                q_i = p
                q_dot_i = v
                q_dotdot_i = a
                q_f = p + goal
                i = 0
                print("switch")
            if i == len(t_array):
                t = tf
            else:
                t = t_array[i]
            a0 = q_i
            a1 = q_dot_i
            a2 = 0.5 * q_dotdot_i
            a3 = 1.0 / (2.0 * tf**3.0) * (20.0 * (q_f - q_i) - (8.0 * q_dot_f + 12.0 * q_dot_i) * tf - (3.0 * q_dotdot_f - q_dotdot_i) * tf**2.0)
            a4 = 1.0 / (2.0 * tf**4.0) * (30.0 * (q_i - q_f) + (14.0 * q_dot_f + 16.0 * q_dot_i) * tf + (3.0 * q_dotdot_f - 2.0 * q_dotdot_i) * tf**2.0)
            a5 = 1.0 / (2.0 * tf**5.0) * (12.0 * (q_f - q_i) - (6.0 * q_dot_f + 6.0 * q_dot_i) * tf - (q_dotdot_f - q_dotdot_i) * tf**2.0)

            p = a0 + a1*t + a2*t**2 + a3*t**3 + a4*t**4 + a5*t**5
            v = a1 + 2*a2*t + 3*a3*t**2 + 4*a4*t**3 + 5*a5*t**4
            a = 2*a2 + 6*a3*t + 12*a4*t**2 + 20*a5*t**3

            i += 1
            time.sleep(0.005)
            if t == 1:
                print(t, p, v, a)
        print("done")


