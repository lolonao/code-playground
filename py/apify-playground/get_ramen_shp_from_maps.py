# import Apify client
from apify_client import ApifyClient


# Client initialization with the API token
MY_API_TOKEN = "apify_api_6mLSKXL5rMjFMxsoXLKx0etBqgagP11XtJnC"
apify_client = ApifyClient(MY_API_TOKEN)

# Define the input for the Actor
actor_input = {
    "searchStringsArray": ["ramen"],
    "locationQuery": "New York, USA",
    "maxCrawledPlacesPerSearch": 10,
    "language": "en",
}
# Run an Actor with an input
print("Running the Actor...")
actor_run = apify_client.actor('compass/crawler-google-places').start(run_input=actor_input)

print("🚀 Actor was started")
print("💾 Check your run here: https://console.apify.com/actors/runs/%(id)s" % {"id": actor_run["id"]})

