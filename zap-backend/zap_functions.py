#!/usr/bin/env python
import time
from zapv2 import ZAPv2

# The URL of the application to be tested

def connection():
  # target = 'https://www.google.com'
  # Change to match the API key set in ZAP, or use None if the API key is disabled
  apiKey = '3bgpquotvlhldlf16gjk2h3fl3'
  # apiKey='qiiutul4utrfub1b8veqs50bk0'

  # By default ZAP API client will connect to port 8080
  # zap = ZAPv2(apikey=apiKey)
  return ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090

def attack_target(target, zap):
  try:
    zap.urlopen(target)
  except Exception as e:
    print(e)

  print('Spidering target {}'.format(target))
  # The scan returns a scan id to support concurrent scanning
  scanID = zap.spider.scan(url=target)
  while int(zap.spider.status(scanID)) < 100:
      # Poll the status until it completes
      print('Spider progress %: {}'.format(zap.spider.status(scanID)))
      time.sleep(1)

  print('Spider has completed!')
  # Prints the URLs the spider has crawled
  # print('\n'.join(map(str, zap.spider.results(scanID))))
  return ('\n'.join(map(str, zap.spider.results(scanID))))
  # If required post process the spider results

def fetch_alerts(zap):
   alert_results = zap.core.alerts()
   return alert_results
  #  for alert in alert_results:
  #    print('URL: %s, Risk Level: %s' % (alert['url'], alert['risk']))


# zap = connection()
# attack_target("https://public-firing-range.appspot.com", zap)
# print(fetch_alerts(zap))