# Log Analysis
This is a project required for Full Stack Nanodegree - Udacity.

>basically this project is an internal reporting tool for a team working on a newspaper site, the database for the newspaper site contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. This reporting tool use information from the database to answer questions about the site's user activity.

>This project run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

# Why this project?
- Get practice interacting with a live database both from the command line and from python code.
- Build and refine complex queries.
- How to build a simple backend app.

# softwares and data needed for this project:
## Software Installation:
- Vagrant: [download](https://www.vagrantup.com/downloads.html)
- Virtual Machine: [download](https://www.virtualbox.org/wiki/Downloads)
- Download a FSND virtual machine: [download](https://github.com/udacity/fullstack-nanodegree-vm)
- Clone this repository "log-analysis-project".
- Add this project inside this FSND VM machine, exactly inside vagrant directory.
- For this project, you need to download “newsdata.sql” from [download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Move the “newsdata.sql” to the project directory inside vagrant “log-analysis-project”.
### Once you get the above software installed, write the following instructions in **terminal**:
- `cd vagrant`
- `vagrant up`
- `vagrant ssh`
- `cd /vagrant`
- `cd log-analysis-project`
- Load the data from the “newsdata.sql” by using the command: `psql -d news -f newsdata.sql`  _Note: this project using PostgreSQL DataBase_
- Once you have the data loaded into your database, connect to your database using: `psql -d news`

## Database content
- The “newsdata.sql” has three different tables:
i.**Authors**: table includes information about the authors of articles.
ii. **Articles**: table includes the articles themselves.
iii. **Log**: table includes one entry for each time a user has accessed the site.
- You can Explore the Database in your **terminal** by using these commands:
`\dt` : display tables — lists the tables that are available in the database
`\d table_name` : shows the database schema for that particular table

## Views you have to create ininside "newsdata.sql" Database
before  you running this python tool, have to create these four views:
### First view: **author_title_path**
`Create view author_title_path as Select au.name, ar.title, l.path from authors as au, articles as ar , log as l where au.id = ar.author and l.path !='/' and l.path = '/article/'|| slug;`
### Second view: **requests**
`Create view requests as Select date(time), count(*) as req from log group by date(time);`
### Third view: **errors**
`Create view errors as Select date(time), count(*) as err from log where status=‘404 NOT FOUND’ group by date(time);`
### Fourth view: **percentage_of_daily_errors**
`Create view percentage_of_daily_errors as Select e.date  , ROUND(e.err::numeric / r.req * 100 ,2) as percentage from errors as e ,  requests as r Where e.date = r.date ;`
### After creating these views, you can list and review them by this command:
`\dv` : display views — lists the views that are available in the database

# How to Run this python reporting tool?!
- Open your **terminal**.
- `cd vagrant`
- `vagrant up`
- `vagrant ssh`
- `cd /vagrant`
- `cd log-analysis-project`
- `python reporting_tool.py`
