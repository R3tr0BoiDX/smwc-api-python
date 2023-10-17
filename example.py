import api

if __name__ == "__main__":
    page = api.get_section_list(api.Section.smw)

    for item in page.data:
        print(item.name)
