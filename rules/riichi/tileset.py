# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

tiles = [(n, 4) for n in ('Ton', 'Nan', 'Shā', 'Pei', 'Haku', 'Hatsu', 'Chun',
         'Īpin', 'Ryanpin', 'Sanpin', 'Sūpin', 'Ūpin', 'Ryūpin', 'Chīpin', 'Pāpin', 'Chūpin',
         'Īsou', 'Ryansou', 'Sansou', 'Sūsou', 'Ūsou', 'Ryūsou', 'Chīsou', 'Pāsou', 'Chūsou',
         'Īwan', 'Ryanwan', 'Sanwan', 'Sūwan', 'Ūwan', 'Ryūwan', 'Chīwan', 'Pāwan', 'Chūwan')]

class TileType:
	honour, terminal, simple = range(3)

class TileSuit:
	kazehai, sangenpai, pinzu, souzu, manzu = range(5)

class TileValue:
	east, south, west, north, white, green, red, one, two, three, four, five, six, seven, eight, nine = range(16)

class Tile(object):
	def __init__(self, group, suit, value, dora):
		self.group, self.suit, self.value, self.dora = group, suit, value, dora

tile_spec = {'Ton': Tile(TileType.honour, TileSuit.kazehai, TileValue.east, 'Nan'),
            'Nan': Tile(TileType.honour, TileSuit.kazehai, TileValue.south, 'Shā'),
            'Shā': Tile(TileType.honour, TileSuit.kazehai, TileValue.west, 'Pei'),
            'Pei': Tile(TileType.honour, TileSuit.kazehai, TileValue.north, 'Ton'),
            'Haku': Tile(TileType.honour, TileSuit.sangenpai, TileValue.white, 'Hatsu'),
            'Hatsu': Tile(TileType.honour, TileSuit.sangenpai, TileValue.green, 'Chun'),
            'Chun': Tile(TileType.honour, TileSuit.sangenpai, TileValue.red, 'Haku'),
            'Īpin': Tile(TileType.terminal, TileSuit.pinzu, TileValue.one, 'Ryanpin'),
            'Ryanpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.two, 'Sanpin'),
            'Sanpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.three, 'Sūpin'),
            'Sūpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.four, 'Ūpin'),
            'Ūpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.five, 'Ryūpin'),
            'Ryūpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.six, 'Chīpin'),
            'Chīpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.seven, 'Pāpin'),
            'Pāpin': Tile(TileType.simple, TileSuit.pinzu, TileValue.eight, 'Chūpin'),
            'Chūpin': Tile(TileType.terminal, TileSuit.pinzu, TileValue.nine, 'Īpin'),
            'Īsou': Tile(TileType.terminal, TileSuit.souzu, TileValue.one, 'Ryansou'),
            'Ryansou': Tile(TileType.simple, TileSuit.souzu, TileValue.two, 'Sansou'),
            'Sansou': Tile(TileType.simple, TileSuit.souzu, TileValue.three, 'Sūsou'),
            'Sūsou': Tile(TileType.simple, TileSuit.souzu, TileValue.four, 'Ūsou'),
            'Ūsou': Tile(TileType.simple, TileSuit.souzu, TileValue.five, 'Ryūsou'),
            'Ryūsou': Tile(TileType.simple, TileSuit.souzu, TileValue.six, 'Chīsou'),
            'Chīsou': Tile(TileType.simple, TileSuit.souzu, TileValue.seven, 'Pāsou'),
            'Pāsou': Tile(TileType.simple, TileSuit.souzu, TileValue.eight, 'Chūsou'),
            'Chūsou': Tile(TileType.terminal, TileSuit.souzu, TileValue.nine, 'Īsou'),
            'Īwan': Tile(TileType.terminal, TileSuit.manzu, TileValue.one, 'Ryanwan'),
            'Ryanwan': Tile(TileType.simple, TileSuit.manzu, TileValue.two, 'Sanwan'),
            'Sanwan': Tile(TileType.simple, TileSuit.manzu, TileValue.three, 'Sūwan'),
            'Sūwan': Tile(TileType.simple, TileSuit.manzu, TileValue.four, 'Ūwan'),
            'Ūwan': Tile(TileType.simple, TileSuit.manzu, TileValue.five, 'Ryūwan'),
            'Ryūwan': Tile(TileType.simple, TileSuit.manzu, TileValue.six, 'Chīwan'),
            'Chīwan': Tile(TileType.simple, TileSuit.manzu, TileValue.seven, 'Pāwan'),
            'Pāwan': Tile(TileType.simple, TileSuit.manzu, TileValue.eight, 'Chūwan'),
            'Chūwan': Tile(TileType.terminal, TileSuit.manzu, TileValue.nine, 'Īwan')}
