import sys
from webpage_interface import *


def build_link_map(wiki_page, link_depth=2):
    print '[+] Processing Depth Level: 1'
    total_list = current_list = get_links_from_page(wiki_page)

    for depth in range(link_depth - 1):
        print '[+] Processing Depth Level: {0}'.format(depth+2)
        sub_list = []

        count = 1
        total = len(current_list)
        for link in current_list:
            print '\t[+] Processing Link {0} of {1} - {2}%'.format(count, total, (float(count)/total)*100)
            sub_list += get_links_from_page(link)
            count += 1

        total_list += sub_list

        total_list = list(set(total_list))
        sub_list = list(set(sub_list))
        current_list = sub_list

    for link in total_list:
        print link

    print len(total_list)


def get_links_from_page(wiki_page):
    try:
        page_contents = pull_webpage(wiki_page)
    except LookupError:
        print 'Webpage Not Valid!'
        sys.exit(1)

    all_links = get_all_links(wiki_page, page_contents)
    filtered_links = filter_links(wiki_page, all_links)

    return filtered_links


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print 'Usage: {0} <Starting Page> <Link Depth (Optional)>'.format(sys.argv[0])
        sys.exit(1)
    elif len(sys.argv) == 2:
        wiki_page = sys.argv[1]
        build_link_map(wiki_page)
    else:
        wiki_page = sys.argv[1]
        link_depth = sys.argv[2]
        build_link_map(wiki_page, link_depth)