api_keywords = ["api","beacons", "static", "sdk", "amazonaws", "aws", "client", "cdn", "rtb", "pbs", "fastlane", "cloudfront", "webapi", "service", "endpoint", "font", "fonts", "content", "json", "xml", "rpc", "rest", "graphql", "soap", "v1", "v2", "v3", "v4", "v5", "data", "get", "post", "put", "delete", "patch", "call", "method", "action", "query", "resource", "fetch", "retrieve", "send", "receive", "create", "update", "delete", 'googleapis']
url_data = []

def has_hiphen(words):
    return any('-' in word for word in words)

def hidden_api_word(words):
    return any(api_word in word for word in words for api_word in api_keywords)

def has_api_word(words):
    return any(keyword in words for keyword in api_keywords)

def has_ad(words):
    return any('ad' in word for word in words)

def has_single_char(words):
    return any(len(word) == 1 for word in words)

# ////////////////////////

def starts_with_www(words):
    return words[0] == 'www'

def ends_with_com(words):
    return words[-1] == 'com'

def ends_with_pk(words):
    if ends_with_com(words):
        return True
    elif words[-2] == 'com' and words[-1] == 'pk' :
        return True
    else:
        return False

def has_format_3_words(words):
    return starts_with_www(words) and ends_with_com(words)

def has_format_4_words(words):
    return starts_with_www(words) and ends_with_pk(words)

def has_domain_format(words):
    if len(words) == 3:
        return has_format_3_words(words)
    elif len(words) == 4:
        return has_format_4_words(words)
    elif len(words) == 2:
        return ends_with_com(words)
    else:
        return False

# ////////////////////////

def is_valid_url(dns_query_name):
    url_split = dns_query_name.split('.')[0:-1]
    return len(url_split) < 5 and has_api_word(url_split) == False and hidden_api_word(url_split) == False and has_ad(url_split) == False and has_hiphen(url_split) == False and has_domain_format(url_split) == True and has_single_char(url_split) == False
