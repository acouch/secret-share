# Secret Share

## Requirments

>  Design and build a one time secret management system that allows users to anonymously create and share secrets with others on demand.

While a secret management system often has security implications, I interpreted this ask as a quick way to share a secret with a friend anonymously or with a pseudonym.

## User Stories

### Included user stories

As a user, I want to input a secret, so that I can share it with a friend

As a user, I want to include my name and my confidante's name, so that that I can personalize the secret.

As a user, I would like a URL for my secret, so that it is easy for me to share the secret with a friend.

As a user, I don't want my secret to be found through google or other search engines.

### Out of scope user stories

As a user, I want to email my secret through the site, so that I can send it to someone anonymously

As a user, I want my secret to dissappear after a specified amount of time, so that I know it will go away

As a user, I want to supply a password for my secret, so that I can ensure only my confidant can see it

As an administrator, I would like to see analytics about the use of the site, so that I can know how many people are using it and other success criteria

## Developer Instructions

Run ``docker-compose up -d`` in the root directory to start the app. Visit the app at http://localhost:5000.

The app can be run outside of docker with the following steps:

1. Ensure python 3.8+ is installed locally
2. Ensure postgres is running with a database that is specified with the ``POSTGRES_DB`` variable in the ``.env`` file and the postgres user/password variables are correct.
3. Update the ``HOST_IP`` address in the ``.env`` file to ``localhost``
4. Run ``pip install -r requirments.txt``
5. Run ``python run.py``
6. Visit the app at http://localhost:5000

### Updating CSS files

Run the following:

1. ``npm install``
2. ``npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/css/output.css --watch``

## Creating a Production Version

In response to:

> say what you would do instead if it was a production app

A production version would require tests, the app config set to production and debugging turned off, a production hosting setup with a production WSGI server, continous integration for deployment, a logo and art with the propper usage rights (current logo copy/pated from https://www.logomaker.com), and many other items.