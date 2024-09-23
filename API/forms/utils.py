def translate_psqi(json_data):
    frequency_map = {
        "opt-1-a": 0, "opt-2-a": 1, "opt-3-a": 2, "opt-4-a": 3,
        "opt-1-b": 0, "opt-2-b": 1, "opt-3-b": 2, "opt-4-b": 3,
        "opt-1-c": 0, "opt-2-c": 1, "opt-3-c": 2, "opt-4-c": 3,
        "opt-1-d": 0, "opt-2-d": 1, "opt-3-d": 2, "opt-4-d": 3,
        "opt-1-e": 0, "opt-2-e": 1, "opt-3-e": 2, "opt-4-e": 3,
        "opt-1-f": 0, "opt-2-f": 1, "opt-3-f": 2, "opt-4-f": 3,
        "opt-1-g": 0, "opt-2-g": 1, "opt-3-g": 2, "opt-4-g": 3,
        "opt-1-h": 0, "opt-2-h": 1, "opt-3-h": 2, "opt-4-h": 3,
        "opt-1-i": 0, "opt-2-i": 1, "opt-3-i": 2, "opt-4-i": 3,
        "opt-1-j": 0, "opt-2-j": 1, "opt-3-j": 2, "opt-4-j": 3,
        "6-a": 0, "6-b": 1, "6-c": 2, "6-d": 3,
        "7-a": 0, "7-b": 1, "7-c": 2, "7-d": 3,
        "8-a": 0, "8-b": 1, "8-c": 2, "8-d": 3,
        "9-a": 0, "9-b": 1, "9-c": 2, "9-d": 3,
    }

    translated_data = {
        "question1": json_data.get("question1"),
        "question2": int(json_data.get("question2", 0)),
        "question3": json_data.get("question3"),
        "question4": int(json_data.get("question4", 0)),
        "question5a": frequency_map.get(json_data.get("question5A"), 0),
        "question5b": frequency_map.get(json_data.get("question5B"), 0),
        "question5c": frequency_map.get(json_data.get("question5C"), 0),
        "question5d": frequency_map.get(json_data.get("question5D"), 0),
        "question5e": frequency_map.get(json_data.get("question5E"), 0),
        "question5f": frequency_map.get(json_data.get("question5F"), 0),
        "question5g": frequency_map.get(json_data.get("question5G"), 0),
        "question5h": frequency_map.get(json_data.get("question5h"), 0),
        "question5i": frequency_map.get(json_data.get("question5i"), 0),
        "question5j": frequency_map.get(json_data.get("question5j"), 0),
        "question5jTitle": json_data.get('question5jTitle', None),
        "question6": frequency_map.get(json_data.get("question6"), 0),
        "question7": frequency_map.get(json_data.get("question7"), 0),
        "question8": frequency_map.get(json_data.get("question8"), 0),
        "question9": frequency_map.get(json_data.get("question9"), 0)
    }

    return translated_data


def calculate_psqi_scores(data):
    quality_score = int(data.get('question6', 0))

    latency_score = 0
    if data.get('question2') is not None:
        if data['question2'] <= 15:
            latency_score = 0
        elif 16 <= data['question2'] <= 30:
            latency_score = 1
        elif 31 <= data['question2'] <= 60:
            latency_score = 2
        else:
            latency_score = 3

    frequency_map = {
        "opt-1-a": 0, "opt-2-a": 1, "opt-3-a": 2, "opt-4-a": 3,
        "opt-1-b": 0, "opt-2-b": 1, "opt-3-b": 2, "opt-4-b": 3,
        "opt-1-c": 0, "opt-2-c": 1, "opt-3-c": 2, "opt-4-c": 3,
        "opt-1-d": 0, "opt-2-d": 1, "opt-3-d": 2, "opt-4-d": 3,
        "opt-1-e": 0, "opt-2-e": 1, "opt-3-e": 2, "opt-4-e": 3,
        "opt-1-f": 0, "opt-2-f": 1, "opt-3-f": 2, "opt-4-f": 3,
        "opt-1-g": 0, "opt-2-g": 1, "opt-3-g": 2, "opt-4-g": 3,
        "opt-1-h": 0, "opt-2-h": 1, "opt-3-h": 2, "opt-4-h": 3,
        "opt-1-i": 0, "opt-2-i": 1, "opt-3-i": 2, "opt-4-i": 3,
        "opt-1-j": 0, "opt-2-j": 1, "opt-3-j": 2, "opt-4-j": 3,
    }

    disturbance_score = sum([frequency_map.get(data.get(f'question5{chr(65 + i)}'), 0) for i in range(10)])
    disturbance_score = min(27, disturbance_score)

    if disturbance_score == 0:
        disturbances_component = 0
    elif 1 <= disturbance_score <= 9:
        disturbances_component = 1
    elif 10 <= disturbance_score <= 18:
        disturbances_component = 2
    else:
        disturbances_component = 3

    duration_score = 0
    if data.get('question4') is not None:
        if data['question4'] > 7:
            duration_score = 0
        elif 6 <= data['question4'] <= 7:
            duration_score = 1
        elif 5 <= data['question4'] <= 6:
            duration_score = 2
        else:
            duration_score = 3

    sleep_hours = data.get('question4', 0)
    try:
        hours_in_bed = int(data.get('question3', 0)) - int(data.get('question1', 0))
        efficiency = (sleep_hours / hours_in_bed) * 100 if hours_in_bed > 0 else 0
    except ValueError:
        efficiency = 0

    if efficiency > 85:
        efficiency_score = 0
    elif 75 <= efficiency <= 84:
        efficiency_score = 1
    elif 65 <= efficiency <= 74:
        efficiency_score = 2
    else:
        efficiency_score = 3

    medication_score = int(data.get('question7', 0))

    daytime_discomfort_score = sum([int(data.get('question8', 0)), int(data.get('question9', 0))])
    if daytime_discomfort_score <= 0:
        daytime_discomfort_component = 0
    elif 1 <= daytime_discomfort_score <= 2:
        daytime_discomfort_component = 1
    elif 3 <= daytime_discomfort_score <= 4:
        daytime_discomfort_component = 2
    else:
        daytime_discomfort_component = 3

    total_score = (
        quality_score + latency_score + duration_score + efficiency_score + disturbances_component + medication_score + daytime_discomfort_component
    )

    return {
        "quality_score": quality_score,
        "latency_score": latency_score,
        "duration_score": duration_score,
        "efficiency_score": efficiency_score,
        "disturbances_score": disturbances_component,
        "medication_score": medication_score,
        "daytime_discomfort_score": daytime_discomfort_component,
        "total_score": total_score
    }
