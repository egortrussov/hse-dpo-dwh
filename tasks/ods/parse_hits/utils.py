import re
from urllib.parse import urlparse, parse_qs

RAW_HITS_FILTER = """
(URL LIKE '%hse.ru/edu/dpo%' OR
URL LIKE '%busedu.hse.ru%' OR
URL LIKE '%bgoal://%') AND
NOT isNull("URL")
"""

def get_page_type(url):
    # main pages
    if re.fullmatch(".*hse.ru/edu/dpo/", url):
        return "main"
    
    if re.fullmatch(".*busedu.hse.ru/", url):
        return "main"

    # catalogue
    if re.fullmatch(".*hse.ru/edu/dpo/\?page=\d{1,2}", url):
        return "catalogue"

    # search pages
    if re.fullmatch(".*hse.ru/edu/dpo/\?q=.*", url):
        return "search"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\?types=.*", url):
        return "search"
    
    if re.fullmatch(".*hse.ru/edu/dpo/.*?page.*types=.*", url):
        return "search"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\?tags=.*", url):
        return "search"

    if re.fullmatch(".*hse.ru/edu/dpo/.*\?tags=.*", url):
        return "search"
    
    if re.fullmatch(".*hse.ru/edu/dpo/.*?page.*\?tags=.*", url):
        return "search"
    

    # program pages
    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}", url):
        return "program_page"

    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#.*", url):
        return "program_page"
    
    if re.fullmatch(".*busedu.hse.ru/catalog/\d{3,10}\.html", url):
        return "program_page"

    return "other"


def get_page_subtype(url):
    # main pages
    if re.fullmatch(".*hse.ru/edu/dpo/", url):
        return "main"
    
    if re.fullmatch(".*busedu.hse.ru/", url):
        return "main"

    # catalogue
    if re.fullmatch(".*hse.ru/edu/dpo/\?page=\d{1,2}", url):
        return "catalogue"

    # search pages
    if re.fullmatch(".*hse.ru/edu/dpo/\?q=.*", url):
        return "search_by_query"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\?types=.*", url):
        return "search_by_types"
    
    if re.fullmatch(".*hse.ru/edu/dpo/.*?page.*types=.*", url):
        return "search_by_types"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\?tags=.*", url):
        return "search_by_tags"

    if re.fullmatch(".*hse.ru/edu/dpo/.*\?tags=.*", url):
        return "search_by_tags"
    
    if re.fullmatch(".*hse.ru/edu/dpo/.*?page.*\?tags=.*", url):
        return "search_by_tags"
    

    # program pages
    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}", url):
        return "program_page"

    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#about.*", url):
        return "program_page_about"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#program.*", url):
        return "program_page_about"

    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#results.*", url):
        return "program_page_results"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#teachers.*", url):
        return "program_page_teachers"
    
    if re.fullmatch(".*hse.ru/edu/dpo/\d{3,10}#contacts.*", url):
        return "program_page_contacts"
    
    if re.fullmatch(".*busedu.hse.ru/catalog/\d{3,10}\.html", url):
        return "program_page"

    return "other"


def get_page_program_id(page_type, url):
    if page_type != 'program_page':
        return None
    return urlparse(url).path.split("/")[-1]


def get_query_param_value(url, param_type):
    url_parsed = parse_qs(urlparse(url).query)
    raw_param_key = get_raw_param_key(param_type)
    if raw_param_key not in url_parsed.keys():
        return []

    return get_parse_param_function(
        param_type
    )(url_parsed[raw_param_key])


def get_raw_param_key(param_type):
    if param_type == "query":
        return 'q'
    return param_type


def get_parse_param_function(param_type):
    if param_type == "query":
        return lambda x : x[0]
    return lambda x : x


def rename_fields(fields_list):
    return list(map(
        cast_camel_case_to_snake_case,
        fields_list,
    ))

def cast_camel_case_to_snake_case(s: str):
    result = ""

    for i in range(len(s)):
        if i == 0:
            result += s[i].lower()
            continue
        if s[i].isupper():
            result += "_" + s[i].lower() if not s[i - 1].isupper() else s[i].lower()
        else:
            result += s[i].lower()

    return result
