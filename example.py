import section_list

if __name__ == "__main__":
    page = section_list.get_section_list(section_list.Section.smw)

    for item in page.data:
        print(item.name)
