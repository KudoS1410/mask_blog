# MASK_Blog
<b>Disclaimer: can be used locally only work on deployment in progress</b></br>
A simple blog created using django,<br> <b>General Instructions</b>:
## To open:
* Clone the repo to a folder
* open the terminal and change directory to the current one
* run the command <code>python3 manage.py runserver</code> to run the test server locally
* open the localhost port 8000(localhost:8000)

## To use:
* Read the already available posts 
* login as an existing user
* or register as a user

## To operate on the site's deployment:
* sudo snap install --classic heroku to install heroku and run heroku command to check installation
* use heroku login to login: credentials: ***********@******.com, ***********
* ensure that directory has git version control, if not then git init, git add -A, git commit -m "initial commit"
* after heroku login , check the releases with heroku releases
* to run migrations: heroku run python3 manage.py migrate
* for logging into the server bash: heroku run bash 
* git push heroku master to push to heroku remote

## Targets:
 - [x] Deploy the blog in a free way 
 - [ ] Improve the look with more css and js 
