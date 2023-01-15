def read_input(day: str, file_name: str, split_by='\n') -> list[str]:
    input = f'/Users/igorgarbuz/Documents/advent_of_code_2022/{day}/{file_name}'
    f = open(input, 'r')
    content = f.read().rstrip('\n')  # remove trailing newline
    f.close()
    return content.split(split_by)
