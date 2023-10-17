**Classification**: __Public__

**Last modified**: 2023-10-14

# Public API Reference

## Overview

SMW Central's API is located at: `https://www.smwcentral.net/ajax.php`

All endpoints documented here are available for public use. We'll do our best to keep their input/output interfaces stable. If you use these APIs in a project, we'll appreciate it if you let the Developer team know - it helps us track the popularity of our APIs and we'll be able to update you on any changes.

If you need access to data which isn't exposed by our public API, please get in touch with the Developer team. We'll gladly work with you to provide APIs for any use-cases you might have.

Any endpoint not documented here is internal and may change, break, or be decommissioned at any time. Parsing HTML from the website is also unsupported and we won't make any efforts to accommodate such usage.

## General Usage

Parameters to GET APIs ("URL parameters") are passed in the URL, alongside the parameters that identify the endpoint.

Parameters to non-GET APIs ("request body") must be encoded as `application/x-www-form-urlencoded`.

Both URL parameters and the request body follow [PHP's rules for query strings](https://www.php.net/manual/en/language.variables.external.php).

All APIs return JSON data (regardless of request headers).

### Token

`GET` `/ajax.php?a=token` 

Certain authenticated non-GET requests may require a CSRF token.

**Response**

- `token`: *string*

  Current CSRF token for the authenticated user. This periodically changes.

### Pagination

Some endpoints return paginated results. Responses for these APIs have the following format:

- `total`: *number*

  Total records in the entire result set.
- `per_page`: *number*

  Number of records per page. Usually, there is no way to change this.
- `current_page`: *number*

  Page number returned in the current response.
- `last_page`: *number*

  Number of the last page.
- `first_page_url`: *string*

  URL of the first page. Make a request to this URL to get the first page of the results.
- `last_page_url`: *string*

  URL of the last page.
- `next_page_url`: *string | null*

  URL of the next page, or `null` if this response is the last page.
- `prev_page_url`: *string | null*

  URL of the previous page, or null if this response is the first page.
- `from`: *number*

  Index (starting at 1) of the first record in this response. For the first page, this is 1.
- `to`: *number*

  Index (starting at 1) of the last record in this response. For the last page, this is `total`.
- `data`: *object\[\]*

  Results, see the specific endpoint for information.

## Sections

### Types

#### `User`

- `id`: *number | null*

  User ID on SMW Central.

  Some `User` objects may refer to unregistered users, in which case this is `null`. References to a `User` will explicitly state whether this is possible.
- `name`: *string*

  Username. If the user is registered, this will be their SMW Central username.

#### `File`

- `id`: *number*

  File ID.
- `section`: *string*

  Section name.
- `name`: *string*

  File name.
- `time`: *number*

  Time at which the file was added to the section (for moderated files) or submitted (for waiting files). UNIX timestamp.
- `moderated`: *boolean*  
  Whether the file is moderated.
- `authors`: *User\[\]*

  Authors of the file. Users may be unregistered.
- `submitter`: *User | null*

  For waiting files, user who submitted the file. Always `null` for moderated files.
- `rating`: *number | null*

  File rating, if the section allows ratings.
- `size`: *number*

  File size in bytes.
- `downloads`: *number*

  Number of downloads.
- `download_url`: *string*  
  URL at which the file can be downloaded. Make a `GET` request to download the file.
- `obsoleted_by`: *number | null*

  If the file is obsolete (i.e. an update has been submitted), the ID of the newest version.
- `fields`: *string\[\]*

  Section-specific fields, returned as safe HTML. Localized values always use the `en_US` translation.

### Endpoints

#### Get section files

`GET` `/ajax.php?a=getsectionlist`

Fetches a list of all files in a section. Supports filtering and sorting.

This endpoint is completely equivalent to the section list page on the website and uses the same URL parameters. A `/?p=section&a=list` URL can be directly converted to this endpoint.

**URL parameters**

- `s`: *string*, **required**

  Name of the section to query.
- `u`: *int*

  If set to a non-zero value, show waiting files. If missing or `0`, show moderated files.
- `n`: *number*

  Page number.
- `o`: *string*

  Field to sort the results by, one of: `date`, `name`, `filesize`, `downloads`.

  Default value is section-dependent, typically `date`.
- `d`: *string*

  Sort direction (ascending or descending), one of: `asc`, `desc`

  Default value is `desc` for moderated files, `asc` for waiting files.
- `f`: *array*

  Filters to apply. This is an associative array keyed by the field name. For select and multi-select fields, values should be arrays.

  This parameter uses many internal names and IDs. Currently, it's best to reference existing URLs from section on the website.

**Response**

Returns a paginated response (see Pagination above). Records in the `data` array are `File` objects (see Types above).

#### Get file

`GET` `/ajax.php?a=getfile&v=2` 

Fetches detailed information about a file.

**URL parameters**

- `id`: *number*, **required**

  File ID.

**Response**

Returns a `File` object (see Types above). The returned object also contains the following additional values:

- `tags`: *string\[\]*

  Array of tags on the file.
- `versions`: *object\[\]*

  The full version history of the file, sorted from newest to oldest.

  One of these will correspond to the requested file. For up-to-date files, this will be the first entry. For obsolete files, it will be a later entry.
- `versions[].id`: *number*

  File ID of the version.
- `versions[].name`: *string*

  Name of the version.
- `versions[].obsolete`: *boolean*

  Whether this version is obsolete.
- `images`: *string\[\] | null*

  If the section has images, array of URLs for each image on the file.
