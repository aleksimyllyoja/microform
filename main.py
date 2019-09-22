#!/usr/bin/env python3

from importlib import reload
from gpiozero import Button
from signal import pause

from test_images import *

import subprocess

import patch

def main():
	def show(t=0):
		reload(patch)
		out = subprocess.run(
			['expono', patch.file, '-e', str(patch.exposure)],
			capture_output=True
		)
		print(out.stdout.decode('ascii'))

	button = Button(4)
	button.when_pressed = show

	pause()

if __name__ == '__main__':
	main()
