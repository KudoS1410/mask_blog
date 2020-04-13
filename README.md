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
* <code>sudo snap install --classic heroku</code> to install heroku and run heroku command to check installation
* use heroku login to login: credentials: ***********@******.com, ***********
* ensure that directory has git version control, if not then <code>git init</code>, <code>git add -A</code>, <code>git commit -m "initial commit"</code>
* after heroku login , check the releases with <code>heroku releases</code>
* to run migrations: <code>heroku run python3 manage.py migrate</code>
* for logging into the server bash: <code>heroku run bash</code> 
* <code>git push heroku master</code> to push to heroku remote

## Targets:
 - [x] Deploy the blog in a free way 
 - [ ] Improve the look with more css and js 
