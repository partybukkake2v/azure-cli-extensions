# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
import inspect
import os


__path__ = __import__('pkgutil').extend_path(__path__, __name__)


def try_manual(func):
    def import_manual_function(origin_func):
        from importlib import import_module
        decorated_path = inspect.getfile(origin_func)
        module_path = __path__[0]
        if not decorated_path.startswith(module_path):
            raise Exception("Decorator can only be used in submodules!")
        manual_path = os.path.join(
            decorated_path[module_path.rfind(os.path.sep) + 1:])
        manual_file_path, manual_file_name = os.path.split(manual_path)
        module_name, _ = os.path.splitext(manual_file_name)
        manual_module = "..manual." + \
            ".".join(manual_file_path.split(os.path.sep) + [module_name, ])
        return getattr(import_module(manual_module, package=__name__), origin_func.__name__)

    def get_func_to_call():
        func_to_call = func
        try:
            func_to_call = import_manual_function(func)
        except (ImportError, AttributeError):
            pass
        return func_to_call

    def wrapper(*args, **kwargs):
        func_to_call = get_func_to_call()
        print("running {}()...".format(func.__name__))
        return func_to_call(*args, **kwargs)

    if inspect.isclass(func):
        return get_func_to_call()
    return wrapper
