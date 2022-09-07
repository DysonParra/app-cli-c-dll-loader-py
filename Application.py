'''
https://docs.python.org/3/library/ctypes.html
ctypes type			C type							Python type
c_bool				_Bool							bool (1)
c_char				char							1-character bytes object
c_wchar				wchar_t							1-character string
c_byte				char							int
c_ubyte				unsigned char					int
c_short				short							int
c_ushort			unsigned short					int
c_int				int								int
c_uint				unsigned int					int
c_long				long							int
c_ulong				unsigned long					int
c_longlong			__int64 or long long			int
c_ulonglong			unsigned __int64 				int
c_ulonglong			unsigned long long				int
c_size_t			size_t							int
c_ssize_t			ssize_t or Py_ssize_t			int
c_float				float							float
c_double			double							float
c_longdouble		long double						float
c_char_p			char * (NUL terminated)			bytes object or None
c_wchar_p			wchar_t * (NUL terminated)		string or None
c_void_p			void *							int or None
'''

import ctypes
from ctypes import *
#print(windll.kernel32)
#print(cdll.msvcrt)
#libc = cdll.msvcrt

try:
	libcdec = cdll.LoadLibrary("std_cdecl_lib.dll")
	#libcdec = ctypes.CDLL('lib.dll')
	print("\nLoaded with cdecl")
	print(libcdec)
	libstd = windll.LoadLibrary("std_cdecl_lib.dll")
	print("\nLoaded with stdcall")
	print(libstd)
	print()

	# Se definen los tipos de los argumentos y el tipo de retorno.
	libcdec.factorial.argtypes = [ctypes.c_int]
	libcdec.factorial.restype = ctypes.c_int

	libcdec.helloWorld.argtypes = [ctypes.c_int,ctypes.c_int]
	libcdec.helloWorld.restype = None

	# Wrapper para llamar a la funcion de C con cdecl.
	def factorial_cdecl(number):
		return libcdec.factorial(number)

	# Wrapper para llamar a la funcion de C con cdecl.
	def helloWorld_cdecl(number1, *args):
		return libcdec.helloWorld(number1, *args)

	try:
		print("Calling with cdecl")
		fact = factorial_cdecl(5)
		print("Factorial is: ", fact)
	except Exception as e:
		print(e, "\n")
		try:
			print("Calling with stdcall")
			fact = libstd.factorial(5)
			print("Factorial is: ", fact)
		except Exception as e:
			print(e)

	print("\n")
	try:
		print("Calling with stdcall")
		libstd.helloWorld(5, 3, 7, 9, 1)
	except Exception as e:
		print(e, "\n")
		try:
			print("Calling with cdecl")
			helloWorld_cdecl(5, 3, 7, 9, 1)
		except Exception as e:
			print(e)
except Exception as e:
	print('\nFailed to load lib')
	print(e)