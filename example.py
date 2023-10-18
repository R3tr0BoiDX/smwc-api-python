import api
from smwc_types.section import Section

from filters import HackType, SMW

if __name__ == "__main__":
    # page = api.get_section_list(Section.SMW.HACKS)

    # for item in page.data:
    #     print(item.name)

    filter_param = SMW.get_smwhacks_param(
        hack_type=[HackType.EASY, HackType.NORMAL],
        featured=True,
        demo=True,
        desc="test",
    )

    print(filter_param)
