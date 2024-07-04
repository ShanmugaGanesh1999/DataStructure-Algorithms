def minUnitIntervals(points):
    points.sort()
    intervals = []

    i = 0
    n = len(points)

    while i < n:
        start = points[i]
        interval = [start, start + 1]

        intervals.append(interval)

        while i < n and points[i] <= start + 1:
            i += 1

    return intervals


points = [0.3, 0.5, 0.6, 1.4, 1.6, 2.3, 3.8]
print(minUnitIntervals(points))
