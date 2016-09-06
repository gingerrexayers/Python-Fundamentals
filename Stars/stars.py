def star_line(i, char):
    return ''.join([char for s in xrange(i)])

def draw_stars(x):
    for i in range(0, len(x)):
        if type(x[i]) is str:
            print star_line(len(x[i]), x[i][0].lower())
        else:
            print star_line(x[i], "*")

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
