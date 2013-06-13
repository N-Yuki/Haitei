# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from .tileset import *

class Wind:
	east, south, west, north = range(4)

class Phase:
	draw, main, discard, minkan, replenish = range(5)

class Board(object):
	def __init__(self, tiles, short=False):
		self.wall = tiles[:-14]
		self.dead_wall = tiles[-14:]
		self.replenishing_tiles = self.dead_wall[:4]
		self.dora_tiles = self.dead_wall[4:]
		self.hands = [[self.wall.pop() for tile in range(13)] for player in range(4)]
		self.points = [25000 for player in range(4)]
		self.short = short
		self.wind = Wind.east
		self.dealer = 0
		self.player = 0
		self.phase = Phase.draw
	
	def draw(self, dead=False):
		if not dead:
			self.hands[self.player].append(self.wall.pop())
		else:
			self.hands[self.player].append(self.replenishing_tiles.pop())
		return self.hands[self.player][-1]
	
	def dora(self, riichi=False):
		revealed = 5 - len(self.replenishing_tiles)
		return [tile_spec[tile].dora for (idx, tile) in enumerate(self.dora_tiles) if idx/2 < revealed and (riichi or not idx % 2)]
	
	def minkan(self):
		pass
