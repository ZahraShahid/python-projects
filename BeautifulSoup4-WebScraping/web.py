try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

import requests
import time

#prompts user to enter job they are not interested in, to filter it out
print("Enter the skills you're not inteested in")
f_skills = input(">")
print(f"Filtering out {f_skills}")

def find_jobs():
    #gets the data from the requested link
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    #reads all the data on the link
    soup = BeautifulSoup(html_text,'lxml')

    #finds all the jobs in the'li', listed on the page
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")

    #loops over index and all the listed jobs on the page
    for index, job in enumerate(jobs):
        
        #finds the published date of each job
        published_date = job.find('span', class_="sim-posted").span.text

        #filters only the jobs listed 'few' days ago based on published date
        if('few' in published_date):

            #finds The Company Name, The Required Skills for the job, and the link to these jobs
            comp_name = job.find('h3',class_="joblist-comp-name").text.replace(" ","")
            skills = job.find('span',class_="srp-skills").text.replace(" ","")
            more_info = job.header.h2.a['href']

            #only search for the skills required by the user and write them out in a seperate file each
            if f_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {comp_name.strip()} \n")
                    f.write(f"Skills Required: {skills.strip()} \n")
                    f.write(f"Published Date: {published_date.strip()} \n")
                    f.write(f"More Information: {more_info} \n")

                print(f'File saved: {index}')



#wait for next 10 minutes to repeat the process
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait*60)
