#!/usr/bin/env python3

import shutil
import matplotlib.pyplot as plt
import numpy as np
from reproduce_plot import img_save, img_reproduce

def my_plot(data, fname):
    # Take exactly one argument with suffix {.pdf .png .eps .jpg .gif}
    plt.plot(data)
    plt.savefig(fname)
    plt.close()

def test_save_and_reproduce():
    data = np.random.randn(10)
    my_plot(data, "image1.pdf")  # Without wrapper
    img_save(my_plot, data, "image2.pdf")  # Pickle arguments with wrapper
    shutil.move("image2.pdf", "image2_orig.pdf")
    img_reproduce(my_plot, "image2.pkl")  # Reproduce from pickled arguments

if __name__ == "__main__":
    test_save_and_reproduce()
