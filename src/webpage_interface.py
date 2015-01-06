import httplib2
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup


def pull_webpage(wiki_page):
    http = httplib2.Http()
    request_status, response = http.request(wiki_page)
    if request_status.status == 200:
        return response
    else:
        raise LookupError


def get_all_links(wiki_page, page_contents):
    soup = BeautifulSoup(page_contents)

    all_links = []

    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(wiki_page, tag['href'])
        all_links.append(tag['href'])

    return all_links


def filter_links(wiki_page, all_links):
    base_url = urlparse(wiki_page).netloc
    base_url += '/wiki/'

    filtered_list = []
    for link in all_links:
        if base_url not in link:
            continue
        if 'cite_note' in link:
            continue
        if 'cite_ref' in link:
            continue
        if 'CITEREF' in link:
            continue
        if link.count(':') > 1:
            continue

        if '#' in link:
            link = link.split('#')[0]

        filtered_list.append(link)

    filtered_list = list(set(filtered_list))

    return filtered_list