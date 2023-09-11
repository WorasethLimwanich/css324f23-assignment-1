def initial_state():
    return (8, 0, 0)  # Change initial state to (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4  # Check if the 8-liter and 5-liter bottles have 4 liters

def successors(s):
    a, b, c = s
    successors_list = []

    # Pour from A to B
    if a > 0 and b < 5:
        pour = min(a, 5 - b)
        new_state = (a - pour, b + pour, c)
        successors_list.append((new_state, pour))

    # Pour from A to C
    if a > 0 and c < 3:
        pour = min(a, 3 - c)
        new_state = (a - pour, b, c + pour)
        successors_list.append((new_state, pour))

    # Pour from B to A
    if b > 0 and a < 8:
        pour = min(b, 8 - a)
        new_state = (a + pour, b - pour, c)
        successors_list.append((new_state, pour))

    # Pour from B to C
    if b > 0 and c < 3:
        pour = min(b, 3 - c)
        new_state = (a, b - pour, c + pour)
        successors_list.append((new_state, pour))

    # Pour from C to A
    if c > 0 and a < 8:
        pour = min(c, 8 - a)
        new_state = (a + pour, b, c - pour)
        successors_list.append((new_state, pour))

    # Pour from C to B
    if c > 0 and b < 5:
        pour = min(c, 5 - b)
        new_state = (a, b + pour, c - pour)
        successors_list.append((new_state, pour))

    return successors_list
