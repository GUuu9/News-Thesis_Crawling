#####
# brew install python-tk 
# 외의 것들은 오류인지 다른 창들이 검정색으로 나온다.
#####

from tkinter import *

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
            
def google_news(): # 구글 뉴스 크롤링
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
    
    for i in range(int(input_box2.get())): # 페이지 이동
        
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
    
def naver_news(): # naver 뉴스 크롤링
    browser = webdriver.Chrome()
    
    # 검색 URL 바로 이동
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}"
    new_url = url.format(input_box1.get()) 
    browser.get(new_url)
    
    csv = open("naver_news.csv", "a")
    csv.write("번호, 기사 제목, 기사 요약, 링크\n")
    csv.close()
    
    title_list = []
    content_list = []
    link_list = []
    
    for i in range(int(input_box2.get())): # 페이지 이동
        
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

def thesis_craw(): # Riss 논문 크롤링
    browser = webdriver.Chrome()
    
    # 검색 URL 바로 이동
    # url = "http://www.riss.or.kr/index.do"
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EC%9E%90%EB%8F%99%ED%99%94&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=search&isFDetailSearch=N&sflag=1&searchQuery=%EC%9E%90%EB%8F%99%ED%99%94&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=%EC%9E%90%EB%8F%99%ED%99%94&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
    browser.get(url)
    
    csv = open("thesis.csv", "a")
    csv.write("번호, 기사 제목, 발행기관, 링크\n")
    csv.close()
    
    browser.find_element(By.XPATH, '//*[@id="query"]').click()
    browser.find_element(By.XPATH, '//*[@id="query"]').send_keys(input_box1.get())
    browser.find_element(By.CLASS_NAME, 'btnSearch').click()
    browser.find_element(By.CLASS_NAME, 'tabM1').click()
    
    browser.find_element(By.XPATH, '//*[@id="divContent"]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="divContent"]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/ul/li[3]/a').click()
    browser.find_element(By.CLASS_NAME, 'listSearch').click()
    
    
    
    
    title_list = []
    assigneds_list = []
    link_list = []
    
    
    for i in range(3,int(input_box2.get())+3): # 페이지 이동
        contentInner = browser.find_elements(By.CLASS_NAME, 'srchResultListW') # 데이터가 모두 담겨있는 클래스
    
        for contentIn in contentInner:    
            datas = contentIn.find_elements(By.TAG_NAME, 'li')
        
            for data in datas:
                titles = data.find_elements(By.CLASS_NAME, 'title')
                assigneds = data.find_elements(By.CLASS_NAME, 'assigned')
                
                for title in titles:
                    title_list.append(title.text.replace(",", ""))
                    link = title.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    link_list.append(link)
                    
                for assigned in assigneds:
                    assigneds_list.append(assigned.text)
        
        browser.find_element(By.XPATH, f'//*[@id="divContent"]/div/div[2]/div/div[4]/a[{i}]').click()
        time.sleep(5)
        
    for i in range(len(title_list)):
        csv = open("thesis.csv", "a")
        csv.write(f"{i}, {title_list[i]}, {assigneds_list[i]}, {link_list[i]}\n")
        csv.close()

# 라디오 버튼으로 선택된 값에 따라 명령 실행

def crawling_start():
    if (int(input_box2.get()) > 10) or (int(input_box2.get()) < 0):
        label.config(text='페이지 값을 다시 입력해주세요 범위(1~10)')
    elif str(Radiodata.get()) == '1':
        label.config(text='구글 뉴스 크롤링을 시작합니다.')
        google_news()
    elif str(Radiodata.get()) == '2':
        label.config(text='네이버 뉴스 크롤링을 시작합니다.')
        naver_news()
    elif str(Radiodata.get()) == '3':
        label.config(text='Riss 논문 크롤링을 시작합니다.')
        thesis_craw()
            

window = Tk() # TKinter 생성
window.geometry("500x200") # 화면의 크기
window.title("크롤링 프로그램") # 프로그램 명
window.resizable(False, False) # 창 조절 불가

text = Label(window, text="검색하고자 하는 내용 입력", width=20, anchor=CENTER)
text.place(x=150, y=0)

text2 = Label(window, text="검색할 페이지 수(MAX 10)", width=20, anchor=CENTER)
text2.place(x=330, y=0)

text3 = Label(window, text="크롤링할 사이트 선택", width=20)
text3.place(x=-20, y=0)

Radiodata = IntVar() # RadioButton value 값 저장

# 구글
file_text1 = Radiobutton(window, text="구글 뉴스 크롤링", value = 1,variable=Radiodata)
file_text1.place(x=0, y=30)
file_text1.select()

# 네이버
file_text2 = Radiobutton(window, text="네이버 뉴스 크롤링", value = 2, variable=Radiodata)
file_text2.place(x=0, y=60)

# Riss
file_text3 = Radiobutton(window, text="Riss 논문 크롤링", value = 3, variable=Radiodata)
file_text3.place(x=0, y=90)

# 값 입력
input_box1 = Entry(window, width=20)
input_box1.place(x=150, y=30)

# 검색 페이지 수
input_box2 = Entry(window, width=5)
input_box2.place(x=350, y=30)

# 상태 표시 라벨
label = Label(window, text = '입력 대기중')
label.place(x=150, y=60)

# 실행 버튼
run_btn = Button(window, text="Run", command=crawling_start)
run_btn.place(x=420, y=150)

window.mainloop()
