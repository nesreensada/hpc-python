from add_module import ffi, lib

a = np.random.random((1000000,1))
b = np.random.random((1000000,1))
c = np.zeros_like(a)

# Pointer objects need to be passed to library
aptr = ffi.cast("double *", ffi.from_buffer(a))
bptr = ffi.cast("double *", ffi.from_buffer(b))
cptr = ffi.cast("double *", ffi.from_buffer(c))

lib.add(aptr, bptr, cptr, len(a))