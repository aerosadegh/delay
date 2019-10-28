# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:05:15 2019

@author: aerosadegh
"""

import time

class Delay:
    """Delay on-off Function Block"""
    def __init__(self, delay_on=0, delay_off=0):
        self.delay_on = delay_on
        self.delay_off = delay_off
        self.ctime = time.time()-10e10     # change signal time
        self.isig = None                   # previous input signal
        self.osig = False                  # current output signal

    def output(self, signal, changed=False, timestamp=0):
        '''return output of process'''
        if changed:
            #print("*$* Time changed! *$*")
            self.ctime = timestamp if timestamp else time.time()

        self.osig = signal
        #print(f"                        {signal} ---------- {self.osig}")
        return signal


    def _inner(self, signal, timestamp=0):
        delay = timestamp - self.ctime if timestamp else time.time() - self.ctime
        print(f"{float(delay):.3f}, input sig:{signal}, timestamp: {timestamp}")
        assert signal in [True, False], "Signal must be bool value!"

        if (signal and self.delay_on == 0) or (not signal and self.delay_off == 0):
            cht = (self.isig != signal)
            self.isig = signal
            return self.output(signal, cht, timestamp)

        if signal == self.isig and delay >= self.delay_off and not signal:
            #print("1 return                       =======")
            return self.output(signal)
        elif not signal:
            #print("2 return                      === ̷= ===")
            cht = (self.isig != signal)
            #print(" previous input sig1:", self.isig)
            self.isig = signal
            #print(" previous input sig2:", self.isig)
            return self.output(self.osig, cht, timestamp)

        if signal == self.isig and delay >= self.delay_on and signal:
            #print("3 return                       =======")
            return self.output(signal)
        elif signal:
            #print("4 return                      === ̷= ===")
            cht = (self.isig != signal)
            #print(" previous input sig1:", self.isig)
            self.isig = signal
            #print(" previous input sig2:", self.isig)
            return self.output(self.osig, cht, timestamp)


    def __call__(self, sig, timestamp=0):
        return self._inner(sig, timestamp)
