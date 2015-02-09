# FedWatch API

A barebones Django app and API for searching the [Federal Register](https://www.federalregister.gov/articles/search).

This application support the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Basic Features

### API

The API is built on Django using [Django REST framework](http://www.django-rest-framework.org/). The current API is fully consumable, without authentication, by any client at the following endpoints:

- `/api/keywords` [LIST, POST]
- `/api/keywords/<keyword_id>` [GET, PUT, DELETE]

### Application

The web application is a single-page app built upon a Django template. It RESTfully consumes from the API.

The app currently makes requests directly against the Federal Register upon each load of the front page; **no responses are persisted to database**. The only data currently being persisted are keywords that are posted directly to the API.

### Deployment

The app is currently deployed for production on [Heroku](https://heroku.com) at [http://fedwatch.herokuapp.com](http://fedwatch.herokuapp.com). Please contact [zeantsoi](https://github.com/zeantsoi) for details on accessing the Heroku account.

## Next steps

There are a lot of possibilities for where this API can next be taken. Here are just a few:

- Authenticated requests
- Date ranges
- Persist responses to database
- Cron job to periodically query against Federal Register
- Updated/new apps, including desktop/mobile clients

## Attribution

This code was written by [@johnDANGRstorey](https://twitter.com/johndangrstorey), [@eklect](https://twitter.com/eklect), and [@zeantsoi](https://twitter.com/zeantsoi) for [Hackdance 2015](http://hackdance2015.splashthat.com/). All rights to license and use are granted to the organization for which this project was created.