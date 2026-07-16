def get_schedule(crop):

    schedules={

        "rice":
        [
            "Day 1: Field preparation",
            "Day 15: First fertilizer application",
            "Day 45: Weed management",
            "Day 90: Harvest preparation"
        ],


        "wheat":
        [
            "Day 1: Sowing",
            "Day 25: Nitrogen application",
            "Day 80: Irrigation",
            "Day 120: Harvest"
        ],


        "maize":
        [
            "Day 1: Sowing",
            "Day 30: Fertilizer application",
            "Day 70: Irrigation",
            "Day 100: Harvest"
        ]

    }


    return schedules.get(
        crop.lower(),
        [
            "Follow local agricultural practices",
            "Monitor soil moisture",
            "Apply fertilizers based on soil condition"
        ]
    )