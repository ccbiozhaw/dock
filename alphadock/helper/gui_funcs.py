def sort_history(in_dict):
    d = list(in_dict.keys())
    is_save = "temp" in d
    d = [x for x in d if x not in ["temp"]]

    d = sorted([int(x) for x in d])
    try:
        max_experiment = d[-1]
    except:
        max_experiment = 0
    d = [str(x) for x in d]

    # ".ini" in os.listdir(in_dict)

    # if is_save:
    #     d += ["temp"]
    return d, max_experiment
