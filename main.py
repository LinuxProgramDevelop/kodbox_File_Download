import requests
import os
import json
import urllib.parse
import wget
import time

headersss={
    "Host": "cloud.trainee.host",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "100",
    "Origin": "http://cloud.trainee.host",
    "Authorization": "Basic enh5NjY2OmIyb2twbHRjNGdkOXBoNXo=",
    "Connection": "close",
    "Referer": "http://cloud.trainee.host/",
    "Cookie": "__jsluid_h=1743f06c8a44eb5f2efc67a9e7e85297; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1710306913; KOD_SESSION_ID=499f782f4ee8e128b91332e73c9c79b1; CSRF_TOKEN=5wd97tbdBFz4jha1; kodUserID=1"
}


proxies={
    "http":"http://127.0.0.1:8080"
}



def GetFile(save_path,kodbox_path):
    try:
        response=requests.post(url="http://cloud.trainee.host/?explorer/list/path",proxies=proxies,headers=headersss,data="path="+urllib.parse.quote(kodbox_path)+f"&page=1&pageNum=500&CSRF_TOKEN=5wd97tbdBFz4jha2&API_ROUTE=explorer%2Flist%2Fpath")
    except Exception as GetPathListError:
        print("GetPathListError: %s"%GetPathListError)
        return
    jsondatas=json.loads(response.text)['data']
    for filejson in jsondatas['fileList']:
        headerstt={
            "Host": "cloud.trainee.host",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Authorization": "Basic enh5NjY2OmIyb2twbHRjNGdkOXBoNXo=",
            "Connection": "close",
            "Referer": "http://cloud.trainee.host/",
            "Cookie": "__jsluid_h=1743f06c8a44eb5f2efc67a9e7e85297; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1710306913; KOD_SESSION_ID=499f782f4ee8e128b91332e73c9c79b1; CSRF_TOKEN=5wd97tbdBFz4jha2; kodUserID=1",
            "Upgrade-Insecure-Requests": "1"
        }
        try:
            get_download_link=requests.get(url="http://cloud.trainee.host/?explorer/index/fileDownload&path="+urllib.parse.quote(filejson['path'][:-1])+"%2F&accessToken=331dU_bDYicHOgAPmhuRkSs0p2FXC0oHZeZY3WPGqsnr5SVI6Ok9VDF6cHmI6lDLMA47Ai1KD_M9EZ1Xtg&download=1&_etag=1640416026-1007589",headers=headerstt,proxies=proxies, allow_redirects=False)
        except Exception as wgeteerror:
            print(wgeteerror)
        try:
            if "location" not in get_download_link.headers  and get_download_link.status_code != 302 and get_download_link.status_code != 200:
                print("%s download failed "%"./%s/%s"%(save_path,filejson['name']))
                continue
            if filejson['name'].endswith(".txt") == True:
                # print(get_download_link.headers['location'])
                wget_file=requests.get(get_download_link.headers['location'])
                wget_file.encoding="gb2312"
                file=open("./%s/%s"%(save_path,filejson['name']),"w",encoding='utf-8')
                file.write(wget_file.text)
                file.close()
            elif  filejson['name'].endswith(".md") == True:
                wget_file=requests.get(get_download_link.headers['location'])
                wget_file.encoding="gb2312"
                file=open("./%s/%s"%(save_path,filejson['name']),"w",encoding='utf-8')
                file.write(wget_file.text)
                file.close()
            elif  filejson['name'].endswith(".html") == True:
                wget_file=requests.get(get_download_link.headers['location'])
                wget_file.encoding="gb2312"
                file=open("./%s/%s"%(save_path,filejson['name']),"w",encoding='utf-8')
                file.write(wget_file.text)
                file.close()
            elif  filejson['name'].endswith(".htm") == True:
                wget_file=requests.get(get_download_link.headers['location'])
                wget_file.encoding="gb2312"
                file=open("./%s/%s"%(save_path,filejson['name']),"w",encoding='utf-8')
                file.write(wget_file.text)
                file.close()
            elif    filejson['name'].endswith(".yaml") == True:
                wget_file=requests.get(get_download_link.headers['location'])
                wget_file.encoding="gb2312"
                file=open("./%s/%s"%(save_path,filejson['name']),"w",encoding='utf-8')
                file.write(wget_file.text)
                file.close()
                # wget_file=requests.get(get_download_link.headers['location'],stream=True)
                # urllib.request.urlretrieve(get_download_link.headers['location'], filename="./%s/%s"%(save_path,filejson['name']))
                # with open("./%s/%s"%(save_path,filejson['name']),'wb') as f:
                #     f.write(wget_file.content)
                #     f.close()
            else:
            # wget_file=requests.get(get_download_link.headers['location'])
            # with open("./%s/%s"%(save_path,filejson['name']),'wb') as f:
            #     f.write(wget_file.content)
            #     f.close()
            # wget.download(get_download_link.headers['location'],"./%s/%s"%(save_path,filejson['name']))
                if get_download_link.status_code == 302 or get_download_link.status_code == 200:
                    os.system("wget '%s' -O '%s'"%(get_download_link.headers['location'],"./%s/%s"%(save_path,filejson['name'])))
                else:
                    print("%s download failed"%"./%s/%s"%(save_path,filejson['name']))
        except Exception as wgeteerror2:
            print(wgeteerror2)
            print(get_download_link.headers['location'])
        # with open("%s/%s"%(save_path,filejson['name']), "wb",encoding="utf-8") as f:
        #     for chunk in wget_file.iter_content(chunk_size=1024):  # 每次加载1024字节
        #         f.write(chunk)
    for linejson in jsondatas['folderList']:
        if linejson['name'] == ".git":
            continue
        if linejson['isFolder'] == 1:
            child_savepath="%s/%s"%(save_path,linejson['name'])
            if os.path.exists(child_savepath) == False:
                os.mkdir(child_savepath)
            GetFile(child_savepath,linejson['path'])

GetFile("./result/","{source:133818}/")