def route_planner(peaks):
    route = [peaks.split()[0]]

    for peak in peaks.split():
        if int(peak) > int(route[-1]):
            route.append(peak)

    return route


print(route_planner('0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15'))
