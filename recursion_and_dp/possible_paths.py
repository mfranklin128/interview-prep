def possible_paths(x, y, path):
    this_path = [foo for foo in path]
    this_path.append('(%d, %d)'%(x, y))
    print('visiting %d, %d' % (x, y))
    if x == 0 and y == 0:
        print('path=%s'%(', '.join(path)))
        return 1
    if x == 0:
        return possible_paths(x, y - 1, this_path)
    if y == 0:
        return possible_paths(x - 1, y, this_path)
    return possible_paths(x - 1, y, this_path) + possible_paths(x, y - 1, this_path)
    
print(possible_paths(2, 2, []))