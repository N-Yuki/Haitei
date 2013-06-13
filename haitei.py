# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import importlib
import pkgutil
import argparse
import game

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Starts a mahjong server.')
	parser.add_argument('-l', '--list', action='store_true', help='lists the supported rule sets')
	parser.add_argument('-r', '--rule', metavar='N', type=int, nargs=1, help='an integer defining the rule set to use')
	parser.add_argument('-p', '--port', metavar='N', type=int, nargs=1, help='the port to listen on')
	args = parser.parse_args()

	supported_rules = [name for (_, name, _) in pkgutil.iter_modules(['rules'])]
	if args.list:
		print('List of supported rule sets:')
		for (idx, rule) in enumerate(supported_rules):
			print('\t' + str(idx) + ') ' + rule)
	elif args.rule:
		selected_rule = 'rules.' + supported_rules[args.rule[0]]
		port = 0
		if args.port:
			port = args.port[0]
		game.Game(importlib.import_module(selected_rule), port)
	else:
		parser.print_help()
