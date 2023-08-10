import os

GDBC_HEADERS = {
  "content-type": "application/json", ##it needs to be added for graphQl version
	"X-RapidAPI-Key": os.environ['GEODBCITIES_APIKEY'],
	"X-RapidAPI-Host": "geodb-cities-graphql.p.rapidapi.com"
}

GDBC_URL = "https://geodb-cities-graphql.p.rapidapi.com/"

GITHUB_HEADERS = {"Authorization": os.environ['GH_APIKEY']}

GITHUB_URL = "https://api.github.com/graphql"

RAPIDAPI_HEADERS = {
        "content-type": "application/json", ##it needs to be added for graphQl version
	    "X-RapidAPI-Key":  os.environ['RAPIDAPI_APIKEY'],
	    "X-RapidAPI-Host": "graphql-rapidapi-test.p.rapidapi.com"
        }

RAPIDAPI_URL = 'https://graphql-rapidapi-test.p.rapidapi.com/'

RE_HEADERS = { "Content-Type": "application/json" }

RE_URL = "https://rippleenergy.com/graphql"
