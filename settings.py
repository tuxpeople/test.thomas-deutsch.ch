AUTHOR = "Thomas Deutsch"
SITEURL = "http://test.thomas-deutsch.ch"
SITENAME = "Thomas Deutsch"
LOCALE = 'en_US.utf8'
TIMEZONE = 'Europe/Zurich'

DISPLAY_PAGES_ON_MENU = True
WITH_PAGINATION = True
DEFAULT_PAGINATION = 7
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

TWITTER_USERNAME = "tdeutsch"
GITHUB_URL = "https://github.com/tuxpeople"
#DISQUS_SITENAME = "mathieuleplatre"
PIWIK_URL = "http://stat.thomas-deutsch.ch/"
PIWIK_SITE_ID = 4

SOCIAL = (
        ("LinkedIn", "http://ch.linkedin.com/pub/thomas-deutsch/39/a18/844"),
    ("GitHub", "https://github.com/tuxpeople"),
    ("Twitter", "http://twitter.com/tdeutsch"),
)

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
