import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydwd.crawler.dailycrawler import DailyCrawler

crawler = DailyCrawler()
print(crawler.by_city('Berlin-Tegel'))

