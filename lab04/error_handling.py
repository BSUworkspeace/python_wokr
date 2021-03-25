# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2021/03/25 09:40:29
@Author      :soliva
@version      :1.0
'''
from functools import wraps
import sys, traceback
import time

def handle_error(re_raise=True,log_traceback=True,exc_type=(Exception),tries:int=1,delay:float=0.0,backoff=1):
    '''

    '''
    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            loop_number = tries
            if not re_raise:
                while loop_number>0:

                    try:
                        return func(*args, **kwargs)
                    except exc_type:
                        if log_traceback:
                            exc_trace = sys.exc_info()[2]
                            formatted_traceback = ''.join(traceback.format_tb(exc_trace))
                            print(formatted_traceback)
                    finally:
                        pass
                    loop_number= loop_number-1
                    time.sleep(delay*backoff)
        return wrapper

    return decorate


# suppress exception , log traceback
# @handle_error ( re_raise = False )
# def some_function(): x = 1 / 0 # ZeroDivisionError
# some_function ()
# print ( 1 ) # line will be executed as exception is suppressed

# re - raise exception and doesn ’t log traceback as exc_type doesn ’t match
# @handle_error ( re_raise =False , exc_type = KeyError )
# def some_function (): x = 1 / 0 # ZeroDivisionError
# some_function ()
# print ( 1 ) # line won ’t be executed as exception is re - raised


import random
@handle_error ( re_raise =True , tries =3 , delay=0.5 , backoff =2 )
def some_function ():
    if random . random () < 0.75: x = 1 / 0 # ZeroDivisionError
some_function ()