import os

gdbcHeaders = {
  "content-type": "application/json", ##it needs to be added for graphQl version
	"X-RapidAPI-Key": os.environ['GEODBCITIES_APIKEY'],
	"X-RapidAPI-Host": "geodb-cities-graphql.p.rapidapi.com"
}

gdbcUrl = "https://geodb-cities-graphql.p.rapidapi.com/"

githubHeaders = {"Authorization": os.environ['GH_APIKEY']}

githubUrl = "https://api.github.com/graphql"

rapidApiHeaders = {
        "content-type": "application/json", ##it needs to be added for graphQl version
	    "X-RapidAPI-Key":  os.environ['RAPIDAPI_APIKEY'],
	    "X-RapidAPI-Host": "graphql-rapidapi-test.p.rapidapi.com"
        }

rapidApiUrl = 'https://graphql-rapidapi-test.p.rapidapi.com/'
