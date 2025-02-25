"""
@fileoverview    {Application}

@version         2.0

@author          Dyson Arley Parra Tilano <dysontilano@gmail.com>

@copyright       Dyson Parra
@see             github.com/DysonParra

History
@version 1.0     Implementation done.
@version 2.0     Documentation added.
"""
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