shapes = [
	'Rock',
	'Paper',
	'Scissors'
]

map_shape = {
	'A': shapes[0],
	'B': shapes[1],
	'C': shapes[2],
	'X': shapes[0],
	'Y': shapes[1],
	'Z': shapes[2]
}

def play(shape_me, shape_opponent):
	point_for_shape = shapes.index(shape_me) + 1
	# print(point_for_shape)
	if (shape_me == shape_opponent):
		return 3 + point_for_shape
	elif ((shape_me == shapes[0] and shape_opponent == shapes[2])
			or (shape_me == shapes[1] and shape_opponent == shapes[0])
			or (shape_me == shapes[2] and shape_opponent == shapes[1])):
		return 6 + point_for_shape
	else:
		return point_for_shape

def solve():
	input = '/Users/igorgarbuz/Documents/advent_of_code_2022/2/abc_xyz.txt'
	f = open(input, 'r')
	content = f.read()
	f.close()
	games = content.splitlines()
	score = 0
	for game in games:
		
		opponent, me = game.split(' ')
		
		# print('opponent', opponent)
		# print('me', me)
		me = map_shape[me]
		opponent = map_shape[opponent]
		score += play(me, opponent)
	return score



if __name__ == '__main__':
	score = solve()
	print(score)
