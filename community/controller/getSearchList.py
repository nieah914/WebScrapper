# parser.py parser 구조분석
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from community import forms

# Create your views here.
class SiteInfo:
    link = ""
    title = ""

    def __init__(self, pTitle, pLink):
        SiteInfo.title = pTitle
        SiteInfo.link = pLink

def get_searchs(request):
    form = forms.Form()

    require_key = request.POST['required_keywords']
    if request.POST['except_keywords'] != '.':
        except_key =  '-'+request.POST['except_keywords']
    else:
        except_key = ''
    print("request.POST['required_keywords']   = ", require_key)
    print("request.POST['except_keywords']   = ", except_key)

    params = {'q': require_key +'+'+ except_key,
              'query' :require_key +'+'+ except_key }

    # Header 설정 : 차단막기위해서
    # 참조 블로그 https://m.blog.naver.com/kiddwannabe/221185808375
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.50.3 Safari/537.36'};

    # HTTP GET Request
    req = requests.get('https://www.google.co.kr/search?', params=params , headers=headers);
    req_naver = requests.get('https://search.naver.com/search.naver?where=post&sm=tab_jum', params=params,
                             headers=headers);
    print(req_naver)
    print(req_naver)

    req_daum = requests.get('https://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&page=2',
                            params=params,headers=headers);

    # HTML 소스 가져오기
    html = req.text
    # print(html);
    html_naver = req_naver.text
    html_daum = req_daum.text

    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html5lib')
    soup_naver = BeautifulSoup(html_naver, 'html.parser')
    soup_daum = BeautifulSoup(html_daum, 'html.parser')

    # HTTP Header 가져오기
    header = req_naver.headers

    # HTTP Status 가져오기(200: 정상)
    status = req.status_code

    # HTTP가 정상적으로 되었는지(true/false)
    is_ok = req.ok

    my_titles = soup.select(
        'div.rc'
    )

    my_titles_naver = soup_naver.select(
        'dl > dt > a'
    )
    my_titles_daum = soup_daum.select(
        'div.wrap_cont > div > div.wrap_tit.mg_tit > a'
    )


    google_site_lists = []
    naver_site_lists = []
    daum_site_lists = []
    rowCounter = 0;
    test = "";
    print("====================구글=======================");
    for title in my_titles:
        class googleSite(SiteInfo):
            link = ""
            title = ""
            def __init__(self, pTitle, pLink):
                self.title = pTitle
                self.link = pLink
        siteInfo =  googleSite(title.find('a').text, title.find('a').get('href'))
        google_site_lists.append(siteInfo)


    print("====================네이버=======================");
    for title in my_titles_naver:
        class naverSite(SiteInfo):
            link = ""
            title = ""
            def __init__(self, pTitle, pLink):
                self.title = pTitle
                self.link = pLink
        siteInfo = naverSite(title.text, title.get('href'))
        naver_site_lists.append(siteInfo)
    print("===========================================");

    print("====================다음=======================");
    for title in my_titles_daum:
        class daumSite(SiteInfo):
            link = ""
            title = ""
            def __init__(self, pTitle, pLink):
                self.title = pTitle
                self.link = pLink
        siteInfo = daumSite(title.text, title.get('href'))
        daum_site_lists.append(siteInfo)
    print("===========================================");


    context = {
        # 변수 : 데이터
        'form': form,
        'google_site_lists' : google_site_lists,
        'naver_site_lists' : naver_site_lists,
        'daum_site_lists' : daum_site_lists,
        'rowCounter' : rowCounter,
        'test' : test,
    }
    return render(request,'post_list.html',context)



