def format_group(group):
	group_items = group.split('\n')
	total = sum([int(item) for item in group_items if item])
	return total

def solve():
	input = '/Users/igorgarbuz/Documents/advent_of_code_2022/1/elfs.txt'
	f = open(input, 'r')
	# print(f.read())
	content = f.read()
	f.close()
	content_split = content.split('\n\n')
	
	sorted_content_sums = sorted([format_group(group) for group in content_split], reverse=True)
	return sum(sorted_content_sums[:3])



if __name__ == "__main__":
	max_group = solve()
	print(max_group)
