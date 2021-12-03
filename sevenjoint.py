# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from threading import Thread
import numpy as np
import time
import queue
from xarm.wrapper import XArmAPI



def liveTraj(qtraj):

    receive = qtraj.get()
    arm2.set_mode(1)
    arm2.set_state(0)
    position = receive[0]
    robot = receive[1]
    q_i = arm2.angles
        # arm2.angles
    # q_i = s[1]
    q_dot_i = 0
    q_dot_f = 0
    q_dotdot_i = 0
    q_dotdot_f = 0
    q_f = position
    i = 0
    tf = 3
    p=q_i[:]

    t_array = np.arange(0, tf, 0.006)
    print("start")

    while i <= len(t_array):
        for j in range(7):
            start_time = time.time()

            if i == len(t_array):
                t = tf
            else:
                t = t_array[i]
            a0 = q_i[j]
            a1 = q_dot_i
            a2 = 0.5 * q_dotdot_i
            a3 = 1.0 / (2.0 * tf ** 3.0) * (20.0 * (q_f[j] - q_i[j]) - (8.0 * q_dot_f + 12.0 * q_dot_i) * tf - (
                        3.0 * q_dotdot_f - q_dotdot_i) * tf ** 2.0)
            a4 = 1.0 / (2.0 * tf ** 4.0) * (30.0 * (q_i[j] - q_f[j]) + (14.0 * q_dot_f + 16.0 * q_dot_i) * tf + (
                        3.0 * q_dotdot_f - 2.0 * q_dotdot_i) * tf ** 2.0)
            a5 = 1.0 / (2.0 * tf ** 5.0) * (
                        12.0 * (q_f[j] - q_i[j]) - (6.0 * q_dot_f + 6.0 * q_dot_i) * tf - (q_dotdot_f - q_dotdot_i) * tf ** 2.0)

            p[j] = a0 + a1 * t + a2 * t ** 2 + a3 * t ** 3 + a4 * t ** 4 + a5 * t ** 5

        arm2.set_servo_angle_j(angles=p, is_radian=False)
        tts = time.time() - start_time
        sleep = 0.006 - tts

        if tts > 0.006:
            sleep = 0


        time.sleep(sleep)
        i += 1



if __name__ == '__main__':

    arm2 = XArmAPI('192.168.1.244')
    arm2.set_simulation_robot(on_off=False)

    arm2.clean_warn()
    arm2.clean_error()
    qtrajput = queue.Queue()
    # print(arm2.angles)
    rtpthread = Thread(target=liveTraj, args=(qtrajput,))
    rtpthread.start()
    input("press enter to move")
    time.sleep(3)
    pos = [0, -20, 0, 30, 15, 30, 50]
    qtrajput.put([pos, 1])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
