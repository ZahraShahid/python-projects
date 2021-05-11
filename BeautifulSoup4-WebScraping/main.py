#SCRAPPING AN HTML FILE USING PYTHON & BEAUTIFULSOAP

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

#read the content of html file
with open("index.html","r") as html_file:
    content = html_file.read()

    #read all the lines in html file
    soup = BeautifulSoup(content, 'lxml')

    #read all the lines with h5 tag in the file
    courses_html_tags = soup.find_all('h5')

    #print text for all the h5 tags in file
    #for course in courses_html_tags:
        #print(course.text)

    #loop over all the div with class="card" and print text of required divs
    course_cards = soup.find_all('div', class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f"{course_name} costs {course_price}")
        

