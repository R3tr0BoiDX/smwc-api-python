# SMW Central API Python Wrapper

<p align="center">
  <img src=".github/smw-central-api-small.png" alt="SMW Central API Logo">
  <br>
  <img src="https://img.shields.io/badge/API_revision-1-blue" alt="revision">
  <img src="https://img.shields.io/badge/contributions-welcome-green" alt="contributions - welcome">
  <img src="https://img.shields.io/badge/documentation-please_see_docstrings_(WIP)!-orange" alt="contributions - welcome">
</p>

- [SMW Central API Python Wrapper](#smw-central-api-python-wrapper)
  - [What is this?](#what-is-this)
  - [Example usage](#example-usage)
    - [Get section entries](#get-section-entries)
    - [Get a file](#get-a-file)
  - [TODO](#todo)

## What is this?

This is a wrapper for the recently released [SMW Central API](https://cloud.smwcentral.net/s/XYwZsN5FyQi53Ee). This wrapper is currently supporting all features of **revision 1** of the API.

## Example usage

Using this is quite simple. It's made sure that all identifiers reflect how the site and API names their counterparts. So if you're familiar with the site, this should be easy to get used to. All parameter and attributes are explained in the attached **docstrings**!

```python
from api import get_section_list
from smwc_filters import SMW, SMWDifficulty
from smwc_types.section import Section

if __name__ == "__main__":
    # Create filter parameter for the SMW Hacks section
    filter_param = SMW.get_smwhacks_param(
        name="Mario",
        difficulty=SMWDifficulty.NORMAL
    )

    # Get results from SMW Hacks section
    # ! Make sure to use right section !
    results = get_section_list(Section.SMW.HACKS, filters=filter_param)

    # Print results
    print(results.total)
    for file in results.data:
        print(file.id, file.name)

```

### Get section entries

To get all sections entries, you use the `get_section_list()`. As shown in the example above, to get all SMW hacks, having the word "*Mario*" in the name and being a kaizo beginner hack. First create yourself a filter parameter object, which you can then hand together with the associated section to the API.

Every `xxx_filters.get_xxx_param()` function offers all the parameter, the site offers you for this section. The `api.get_section_list()` has more parameter, what and how to display the results!

A call to the `api.get_section_list()` will return a `Pagination` object. Those are essentially a page of the sections catalogs entries. They have attributes like a link to the next page, how many entries are on that page and most importantly, the `data` list, with the entries.

### Get a file

A file is any submission on SMW Central. To retrieve a files details, you use the `api.get_file()` function. This expects a file ID from you. Those you can get from the `File` objects, a `Pagination` object may hold within their `data` list.

## TODO

- revision 2
- complete the docstrings
- improving the sections and filter structure
