from filters import SM64, Difficulty

if __name__ == "__main__":
    filter_param = SM64.get_sm64hacks_param(
        name="Super Mario 64: Ocarina of Time",
        author="Kaze Emanuar",
        tags=["multiplayer", "demo"],
        difficulty=[Difficulty.INTERMEDIATE, Difficulty.HARD],
        demo=True,
        desc="This is a demo description",
    )

    print(filter_param)

    # todo: finish checking filter fields names (SMW, YI)
    # todo: finish transform from list to ParamSet (Generic, SMW, YI)
