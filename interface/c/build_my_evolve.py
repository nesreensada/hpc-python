import os
from cffi import FFI 

ffibuilder = FFI()

with open(os.path.join(os.path.dirname(__file__), "evolve.h")) as f:
        ffibuilder.cdef(f.read())

ffibuilder.set_source("_my_evolve",
    """ #include "evolve.h"  """,
    sources = ['evolve.c'],
    library_dirs = [os.path.dirname(__file__), ],
    libraries = ["m"]
    )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

