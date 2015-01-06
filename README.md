Wikipedia-Link-Map
==================

Search Wikipedia topics eminating from a central article

###Description:
Given a wikipedia article, as a starting point, the script will pull all 
articles it can navigate to within <Link Depth> hyperlink clicks. For example, 
suppose you are Oppenheimer's wiki page. You click on the 'nuclear power' link, and 
then from the Nuclear Power wiki article, you select 'Engineering Research'.

This means 'Engineering Research' is 2 click accessible from Oppenheimer.

###Usage:
wiki_link_map.py <Starting Page> <Link Depth (Optional)>
Example: wiki_link_map.py http://en.wikipedia.org/wiki/J._Robert_Oppenheimer 2

###Output:
The script currently outputs all unique articles in URL format followed by 
the total number of URLs in that order.

It also outputs progress indicators as this can take some time.

###Warning:
The default link depth is 2. I don't suggest going over 2, as the number of pages grows very fast, 
and each page must be pulled and parsed individually.

For example: 71,348 unique wikipedia articles are 2-click accessible from Oppenheimer at the time of writing this.
   The Oppenheimer page contained 578 unique Wikipedia article links, and thus 579 total pages needed
   to be pulled/parsed. If depth 3 was used it would need to pull/parse 71,349 pages.
