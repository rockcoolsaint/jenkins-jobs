import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import sqlite3

conn = sqlite3.connect('jobs.sqlite3')

conn.execute('''CREATE TABLE JOB
         (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
         NUMBER INTEGER			NOT NULL,
         NAME            TEXT    NOT NULL,
         STATUS          TEXT    NOT NULL,
         TIME  		DATETIME NOT NULL);''')

# url = 'http://insert-jenkins-api-url-here'
url = 'https://opensource.triology.de/jenkins/'
# url = 'https://opensource.triology.de/jenkins/blue/organizations/jenkins/triologygmbh-github%2Fjenkinsfile/activity/'
username = ''
password = ''
J = Jenkins(url, username, password)
for job_name in J.keys():
	build = J[job_name].get_last_build()

	number = int(build.get_number())
	status = build.get_status()
	timeStamp = "strftime('%s','now')"
	dateTime = "datetime(timeStamp, 'unixepoch')"
	#print dateTime
	print '{}: #{} {}\n================================\n'.format(job_name, number, status)
	conn.execute("INSERT INTO JOB (NUMBER,NAME,STATUS,TIME) \
		VALUES (?, ?, ?, ?)", (number, job_name, status, dateTime))

conn.close()