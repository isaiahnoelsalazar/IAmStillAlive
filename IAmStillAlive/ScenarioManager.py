scenario_list = []
scenario_index = 0


def start(camera):
    with open("scenarios/scenario_list", "r") as sl:
        for s in sl.readlines():
            exec(open("scenarios/" + s.strip() + ".py").read(), globals(), locals())
            globals().update(locals())
            class_instance = locals()[s.strip()](camera=camera)
            scenario_list.append(class_instance)


def update():
    scenario_list[scenario_index].update()


def display():
    scenario_list[scenario_index].display()