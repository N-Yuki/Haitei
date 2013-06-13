# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import itertools
import random
import socket
import threading
import socketserver

def generate_tiles(tiles):
	return list(itertools.chain.from_iterable(
	       [list(itertools.repeat(tile, count)) for (tile, count) in tiles]
	       ))

game = 0
connected = {}
class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
	def handle(self):
		try:
			connected[self] = {'name': threading.current_thread().name}
			while 1:
				data = self.rfile.readline()
				print("{}: {}".format(name, data))
				if data[0] == 0xff: break
				recv = str(data, 'UTF-8')
				if recv[0] != '/':
					chat = bytes("{}: {}".format(name, recv), 'UTF-8')
					for con in connected.keys():
						con.wfile.write(chat)
						con.wfile.flush()
					print(chat)
				else:
					words = recv.split()
					invalid = False
					if words[0] == '/nick':
						if len(words) == 2: name = words[1]
						else: invalid = True
					elif words[0] == '/start':
						if len(words) == 1 and len(connected) == 4: game.start()
						else: invalid = True
					else:
						self.wfile.write(bytes('Unrecognised command.\n', 'UTF-8'))
						self.wfile.flush()
					if invalid:
						self.wfile.write(bytes('Unexpected use of command.\n', 'UTF-8'))
						self.wfile.flush()
		finally:
			del connected[self]

class Game(object):
	def __init__(self, ruleset, port):
		global game
		game = self
		self.ruleset = ruleset
		self.server = socketserver.ThreadingTCPServer(('localhost', port), ThreadedTCPRequestHandler)
		print('Server Address: ', self.server.server_address)
		self.server.serve_forever()
	
	def start(self):
		print('Generating tiles...', end=' ')
		tiles = generate_tiles(self.ruleset.tiles)
		print('Done.')
		print('Shuffling tiles...', end=' ')
		random.shuffle(tiles)
		print('Done.')
		print('Setting up wall...', end=' ')
		board = self.ruleset.Board(tiles)
		print('Done.')
		print('Player 1\'s hand: ', board.hands[0])
		print('Player 2\'s hand: ', board.hands[1])
		print('Player 3\'s hand: ', board.hands[2])
		print('Player 4\'s hand: ', board.hands[3])
		print('Revealed dora: ', board.dora())
		print('Player 1 draws: ', board.draw())
