#!/usr/bin/env python3

from importlib import reload
from gpiozero import Button
from signal import pause

import subprocess

import patch

def main():
	def show(t=0):
		reload(patch)

		# TODO
		l = map(lambda xs: list(map(t, xs)), np.array(patch.source().tolist()))
		json.dump(list(l), open('source.json', 'w'))

		out = subprocess.run(
			['expono', 'source.json', '-e', str(patch.exposure)],
			capture_output=True
		)
		print(out.stdout.decode('ascii'))

	button = Button(4)
	button.when_pressed = show

	pause()

if __name__ == '__main__':
	main()
