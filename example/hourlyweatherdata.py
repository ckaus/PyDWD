import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydwd.crawler.hourlycrawler import HourlyCrawler

crawler = HourlyCrawler()
print(crawler.by_city('Berlin-Tegel'))
print(crawler.by_region('Berlin'))