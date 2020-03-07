import unittest
from io import StringIO
from bs4 import BeautifulSoup

# Run via 'coverage run --source=. -m unittest rss_item.py'
# Then see the results via 'coverage report' or 'coverage html'

# From: https://en.wikipedia.org/wiki/RSS
XML = '''
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>RSS Title</title>
 <description>This is an example of an RSS feed</description>
 <link>http://www.example.com/main.html</link>
 <lastBuildDate>Mon, 06 Sep 2010 00:01:00 +0000 </lastBuildDate>
 <pubDate>Sun, 06 Sep 2009 16:20:00 +0000</pubDate>
 <ttl>1800</ttl>

 <item>
  <title>Example entry</title>
  <description>Here is some text containing an interesting description.</description>
  <link>http://www.example.com/blog/post/1</link>
  <guid isPermaLink="false">7bd204c6-1655-4c27-aeee-53f933c5395f</guid>
  <pubDate>Sun, 06 Sep 2009 16:20:00 +0000</pubDate>
 </item>

</channel>
</rss>
'''

# This is a class that takes a url file object and extracts the interesting
# parts.
class RSS():
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(url, 'xml')

    def title(self):
        return self.soup.channel.title.text

# This is a class that mocks a file via StringIO and tests the RSS class.
class TestRss(unittest.TestCase):
    def test_title(self):
        rss = RSS(StringIO(XML))
        self.assertEqual(rss.title(), 'RSS Title')
