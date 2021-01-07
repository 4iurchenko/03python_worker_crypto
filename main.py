import requests
import time


GA_TRACKING_ID =  'UA-186484948-1'

def track_event(category, action, label=None, value=0):
    data = {
        'v': '1',  # API Version.
        'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': '555',
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        'ua': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
    }

    response = requests.post(
        'https://www.google-analytics.com/collect', data=data)

    response.raise_for_status()

def get_transaction(acc):
    response = requests.get(
        "https://wax.cryptolions.io/v2/history/get_actions?account={acc}&sort=desc&simple=true&noBinary=true&checkLib=true".format(acc = acc))

    for x in response.json()['simple_actions']:
        if x['irreversible'] == True:
            return x['transaction_id']


if __name__ == '__main__':

    print("Started to send data to GA. The link is:")
    print("https://analytics.google.com/analytics/web/#/realtime/rt-event/a186484948w258037593p235355168/filter.list=33==DESKTOP;/")
    print("Web version is here:")
    print("https://wax.bloks.io/account/cryptolions1")
    
    while True:
        track_event(
            category='Last irreversible TR id',
            action= get_transaction("cryptolions1"),
            value = 1)
        time.sleep(1)



