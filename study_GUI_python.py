#####
# brew install python-tk 
# 외의 것들은 오류인지 다른 창들이 검정색으로 나온다.
#####

from tkinter import *
from tkinter.filedialog import askopenfilename

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# def get_file(): # 외부에서 파일 불러오기 
# 		print("get_file")
# 		file_path = askopenfilename()
# 		print(file_path)

# 		number = input_box.get()
# 		print(number)
            
def google_news(event): # 구글 뉴스 크롤링
    browser = webdriver.Chrome()
    
    # 검색 URL 바로 이동
    url = "https://www.google.com/search?q={}&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiVxM_2r4D9AhXLz2EKHUCqAEcQ_AUoAXoECAEQAw&biw=1200&bih=887&dpr=2"
    new_url = url.format(input_box1.get()) 
    browser.get(new_url)
    
    csv = open("google_news.csv", "a")
    csv.write("번호, 기사 제목, 기사 요약, 링크\n")
    csv.close()
    
    
    title_list = []
    content_list = []
    link_list = []
    
    for i in range(5): # 페이지 이동
        
        # 제목, 내용, 링크
        titles = browser.find_elements(By.CLASS_NAME, 'mCBkyc')
        contents = browser.find_elements(By.CLASS_NAME, 'GI74Re')
        links = browser.find_elements(By.CLASS_NAME, 'WlydOe')
        
        for i in titles:
            title = i.text
            title = title.replace(",", "")
            title_list.append(title)

        for i in contents:
            content = i.text
            content = content.replace("," , "")
            content_list.append(content)
            
        for i in links:
            link = i.get_attribute('href')
            link_list.append(link)

        browser.find_element(By.ID, "pnnext").click()
        time.sleep(5)
        
    for i in range(len(title_list)):
            csv = open("google_news.csv", "a")
            csv.write(f"{i}, {title_list[i]}, {content_list[i]}, {link_list[i]}\n")
            csv.close()
    
def naver_news(event): # naver 뉴스 크롤링
    browser = webdriver.Chrome()
    
    # 검색 URL 바로 이동
    url = "https://news.naver.com/"
    browser.get(url)
    
    csv = open("naver_news.csv", "a")
    csv.write("번호, 기사 제목, 기사 요약, 링크\n")
    csv.close()
    
    browser.find_element(By.CLASS_NAME, 'Nicon_search').click()
    browser.find_element(By.CLASS_NAME, 'u_it').click()
    browser.find_element(By.CLASS_NAME, 'u_it').send_keys(input_box2.get())
    browser.find_element(By.CLASS_NAME, 'u_hssbt').click()
    
    title_list = []
    content_list = []
    link_list = []
    
    for i in range(5): # 페이지 이동
        
        # 제목, 내용, 링크
        titles = browser.find_elements(By.CLASS_NAME, 'news_tit')
        contents = browser.find_elements(By.CLASS_NAME, 'news_dsc')
        links = browser.find_elements(By.CLASS_NAME, 'news_tit')
        
        for i in titles:
            title = i.text
            title = title.replace(",", "")
            title_list.append(title)

        for i in contents:
            content = i.text
            content = content.replace("," , "")
            content_list.append(content)
            
        for i in links:
            link = i.get_attribute('href')
            link_list.append(link)

        browser.find_element(By.CLASS_NAME, "btn_next").click()
        time.sleep(5)
        
    for i in range(len(title_list)):
            csv = open("naver_news.csv", "a")
            csv.write(f"{i}, {title_list[i]}, {content_list[i]}, {link_list[i]}\n")
            csv.close()

window = Tk() # TKinter 생성
window.geometry("400x300") # 화면의 크기
window.title("크롤링 프로그램") # 프로그램 명
window.resizable(False, False) # 창 조절 불가

text = Label(window, text="검색하고자 하는 내용 입력", width=20, anchor=CENTER)
text.grid(column=1, row=1)

# 구글
file_text1 = Label(window, text="구글 뉴스 크롤링")
file_text1.grid(column=1, row=2)

input_box1 = Entry(window, width=20)
input_box1.grid(column=2, row=2)
input_box1.bind("<Return>", google_news)

# 네이버
file_text2 = Label(window, text="네이버 뉴스 크롤링")
file_text2.grid(column=1, row=3)

input_box2 = Entry(window, width=20)
input_box2.grid(column=2, row=3)
input_box2.bind("<Return>", naver_news)



# file_text2 = Button(window, text="논문 데이터 크롤링")
# file_text2.grid(column=1, row=4)

# file_btn = Button(window, text="파일선택", command=get_file)
# file_btn.grid(column=3, row=3)

window.mainloop()