# FemboyRoulette-API v1.01
The API for femboyroulette.xyz.

## Usage

Install the needed python modules for the api

```
pip install -r requirements.txt
```

After installing the requirements run the API with

```
uvicorn main:app --reload
```

## How to add objects to database

Add json files to folder json, their name will be used as ID, so make sure they are named after last object in db (If unsure add.py script shows it at the beginning.)

Then simply run 

```
python add.py
```

and follow instructions.

## How to fetch from the API:

### Javascript (node.js):

Firstly install the request module.


```
npm install request
```

once that is done do the following

```javascript
var request = require('request');

var options = {
  'method': 'GET',
  'url': 'https://api.femboyroulette.ga', //or whatever ip uvicorn spits if you're hosting the api locally
  'headers': {
  }
};

request(options, function (error, response) {
                    if (error) throw new Error(error);
                    var parsed = JSON.parse(response.body); //turns the api into a parsed json file
                    const { image, artist, link} = (parsed) //Requires that parsed json file

console.log("Image: " + image + "\n" + "Artist: " + artist + "\n" + "Link: " + link)

});
```

after this run the script with
```
node (file name).js
```

## Modding:
You're allowed to mod the api as you see fit aslong as it's nature is not malicious.
