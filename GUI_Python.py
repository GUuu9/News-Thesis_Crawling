from tkinter import *
from tkinter.filedialog import askopenfilename

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

TK_SILENCE_DEPRECATION=1

def get_file():
    print("get_file")
    file_path = askopenfilename()
    print(file_path)
    
    number = input_box.get()
    print(number)
    
def google_news():
    browser = webdriver.Chrome()
    url = 'https://www.google.com/search?q=%EC%9E%90%EB%8F%99%ED%99%94&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwin5MbJ5fj8AhXQr1YBHf1FCEsQpwV6BAgEEBo&biw=1200&bih=887&dpr=2'
    browser.get(url)
    
    titles = browser.find_elements(By.CLASS_NAME, 'mCBkyc')
    title_list = []
    for i in titles:
        title = i.text
        title = title.replace(",", "")
        title_list.append(title)

    contents = browser.find_elements(By.CLASS_NAME, 'GI74Re')
    content_list = []
    for i in contents:
        content = i.text
        content = content.replace("," , "")
        content_list.append(content)

    for i in range(10):
        csv = open("google_news.csv", "a")
        csv.write("{}, {}\n".format(title_list[i], content_list[i]))
        csv.close()
        

window = Tk() # Tkinter 생성
window.geometry("300x500") # 화면 크기
window.title("크롤링 프로그램")

input_box = Entry(window, width = 10)
input_box.grid(column = 2, row = 1)

file_text = Button(window, text="구글 뉴스 크롤링", command = google_news)
file_text.grid(column = 1, row = 2)

file_text = Button(window, text="DBPIA 크롤링")
file_text.grid(column = 1, row = 3)

file_btn = Button(window, text = "파일선택", command = get_file)
file_btn.grid(column = 2, row = 3)

window.mainloop()