#!/usr/bin/env python3

from os.path import splitext
import pickle

def img_save(func, *args, **kwargs):
    avals = args + tuple(kwargs.values())
    figure_names = [a for a in avals if __is_figure_name(a)]
    nf = len(figure_names)
    if nf == 1:
        __save_to_pkl(figure_names[0], func.__name__, *args, **kwargs)
        return func(*args, **kwargs)
    else:
        raise Exception(f"img_save: Wrong number ({nf}) of figure-name-like"
            + f" arguments are passed to function {func.__name__}.")

def img_reproduce(func, pkl_name):
    with open(pkl_name, "rb") as f:
        all_args = pickle.load(f)
    func_name, args, kwargs = all_args
    assert func.__name__ == func_name
    return func(*args, **kwargs)

def __is_figure_name(arg):
    if isinstance(arg, str):
        root, ext = splitext(arg)
        if ext in [".pdf", ".png", ".jpg", ".gif", ".eps"]:
            return True
    return False

def __save_to_pkl(figure_name, func_name, *args, **kwargs):
    all_args = (func_name, args, kwargs)
    root, ext = splitext(figure_name)
    pkl_name = root + ".pkl"
    with open(pkl_name, "wb") as f:
        pickle.dump(all_args, f)

