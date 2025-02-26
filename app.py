"""
@fileoverview    {FileName}

@version         2.0

@author          Dyson Arley Parra Tilano <dysontilano@gmail.com>

@copyright       Dyson Parra
@see             github.com/DysonParra

History
@version 1.0     Implementation done.
@version 2.0     Documentation added.
"""
import os, ctypes
from ctypes import *
from datetime import datetime
#print(windll.kernel32)
#print(cdll.msvcrt)
#libc = cdll.msvcrt


def factorial_cdecl(number):
	"""
	Wrapper para llamar a la funcion de C con cdecl.
	"""
	return libcdec.factorial(number)


def helloWorld_cdecl(number1, *args):
	"""
	Wrapper para llamar a la funcion de C con cdecl.
	"""
	return libcdec.helloWorld(number1, *args)


def main():
	"""
	Entrada principal del sistema.
	"""
	DATE_FORMAT ="%Y-%m-%d %H:%M:%S"
	print(f"\nStart date: {datetime.now().strftime(DATE_FORMAT)}")

	# python must be 32-bit to could load the c 32-bit lib.
	libFile = "std_cdecl_lib_x86.dll"
	try:
		global libcdec
		libcdec = cdll.LoadLibrary(f"{os.getcwd()}/{libFile}")
		#libcdec = ctypes.CDLL('lib.dll')
		print("\nLoaded with cdecl")
		print(f"{libcdec}")
		global libstd
		libstd = windll.LoadLibrary(f"{os.getcwd()}/{libFile}")
		print("\nLoaded with stdcall")
		print(f"{libstd}")

		# Se definen los tipos de los argumentos y el tipo de retorno.
		libcdec.factorial.argtypes = [ctypes.c_int]
		libcdec.factorial.restype = ctypes.c_int

		libcdec.helloWorld.argtypes = [ctypes.c_int,ctypes.c_int]
		libcdec.helloWorld.restype = None

		try:
			print("\nCalling with cdecl")
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

		try:
			print("\nCalling with stdcall")
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

	print(f"End date:   {datetime.now().strftime(DATE_FORMAT)}")


if __name__ == "__main__":
	main()
