from api import get_section_list, get_file
from smwc_filters import SMW, SMWDifficulty
from smwc_types.section import Section

if __name__ == "__main__":
    # Create filter parameter for the SMW Hacks section
    filter_param = SMW.get_smwhacks_param(name="Mario", difficulty=SMWDifficulty.NORMAL)

    # Get results from SMW Hacks section
    results = get_section_list(Section.SMW.HACKS, filters=filter_param)

    # Print results
    print(results.total)
    for file in results.data:
        print(file.name)

    # Get first file from results
    file = results.data[0]

    # Get additional information about the file
    file = get_file(file.id)
    if file.extended:
        print(file.name, file.tags)
