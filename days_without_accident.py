import feedparser
from datetime import datetime,timedelta
from time import mktime
import argparse

def get_latest_entry(feed_url, blocklist):
    StatusFeed = feedparser.parse(feed_url)
    
    for entry in StatusFeed.entries:
        if blocklist:
            if not any(x.lower() in entry.title.lower() for x in blocklist):
                return entry
        else:
            return entry

    return None

def get_days_since_entry(entry):
    last_published_date = entry.published_parsed

    dt = datetime.fromtimestamp(mktime(last_published_date))
    return (datetime.today() - dt).days


parser = argparse.ArgumentParser(description='Return the days since the last entry on a Cachet-Statuspage')
parser.add_argument('--blocklist', '-b', help='comma-seperated list of word in title which should be ignored')
parser.add_argument('--plain', '-p', help='Only return the number of days without any fancy stuff', action='store_true')
parser.add_argument('url', help='Url to the feed you want to monitor')

args = parser.parse_args()

if args.blocklist is None:
    entry = get_latest_entry(args.url, None)
else:
    entry = get_latest_entry(args.url, args.blocklist.split(','))

if entry is None:
    delta_days = "∞"
else:
    delta_days = str(get_days_since_entry(entry))

if args.plain:
    print(delta_days)
else:
    print("Days since last accident: " + delta_days)
