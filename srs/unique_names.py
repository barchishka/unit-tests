from srs.fixtures.basic_data import *


def top_unique_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0: 3]
    top = [f"{str(i[0])}: {str(i[1])} раз(а)" for i in top_3]
    return ", ".join(top)


def super_names(mentors):
    mentors_names = []

    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []
    list_mentors = []

    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    names_sorted = sorted(intersection_set)
                    list_mentors.append(
                        f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(names_sorted)}\n")
    return f'{list_mentors[0]}{list_mentors[1]}{list_mentors[2]}{list_mentors[3]}'


def unique_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)

    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'
