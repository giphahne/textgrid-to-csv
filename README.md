# TextGrid

This simple example app uses Dropbox webhooks to convert TextGrid files to CSV

Read more about webhooks and this example on [the Dropbox developers site](https://www.dropbox.com/developers/webhooks/tutorial).

## Running the sample yourself

You can just set the required environment variables (using `.env_sample` as a guide) and run the app directly with `python app.py`.

## Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
=======
You can deploy directly to Heroku with the button below. First you'll need to create an API app via the [App Console](https://www.dropbox.com/developers/apps). Make sure your app has access to files (not just datastores), and answer "Yes - My app only needs access to files it creates" to ensure your app gets created with "App folder" permissions.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Once you've deployed, you can easily clone the app and make modifications:

```
$ heroku clone -a new-app-name
...
$ emacs index.js
$ git add .
$ git commit -m "update index.js"
$ git push heroku master
...
```
