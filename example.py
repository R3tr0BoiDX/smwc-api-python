import api
from smwc_types.section import Section

if __name__ == "__main__":
    page = api.get_section_list(Section.SMW.HACKS)

    for item in page.data:
        print(item.name)
