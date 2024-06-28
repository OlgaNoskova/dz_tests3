def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0  # подсчитайте общую дистанцию зайца
    for km_hare in hare_distances:
        hare_all += km_hare

    turtle_all = 0  # подсчитайте общую дистанцию черепахи
    for km_turtle in turtle_distances:
        turtle_all += km_turtle

    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result

