import api
from smwc_types.section import Section

from filters import SM64, Difficulty

if __name__ == "__main__":
    page = api.get_section_list(Section.SMW.HACKS)

    for item in page.data:
        print(item.name)

    filter_param = SM64.get_sm64hacks_param(
        difficulty=[Difficulty.HARD],
        demo=True,
        tags=["multiplayer", "demo"],
        name="Super Mario 64: Ocarina of Time",
    )

    print(filter_param)
