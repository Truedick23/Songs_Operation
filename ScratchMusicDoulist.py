import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error")
        return ""


def downloadPicture(PicUrlList, AlbumNamesList):
    di = "D://PythonRequestsDownload//"
    length = len(PicUrlList)
    for i in range(length):
        url = PicUrlList[i]
        r = requests.get(url)
        path = di + AlbumNamesList[i] + ".jpg"
        with open(path, "wb") as f:
            f.write(r.content)
    pass

def getSize(url):
    text = getHTMLText(url)
    soup = BeautifulSoup(text, "html.parser")
    ls = soup.find_all(class_ = "doulist-filter")
    str = ls[0].span.text
    num = str[1:-1]
    size = int(num) // 25
    print(size)
    return size

def DeleteElement(numList, AlbumNamesList, PerformerList, CommentsList, PicUrlList):
    for i in numList:
        del AlbumNamesList[i]
        del PerformerList[i]
        del CommentsList[i]
    pass


def scratchInfo(AlbumNamesList, PerformerList, RatingList, CommentsList, PicUrlList, size, url):
    for i in range(size + 1):
        newUrl = url + str(i * 25)
        text = getHTMLText(newUrl)
        soup = BeautifulSoup(text, "html.parser")
        for item in soup.find_all(class_="title"):
            st = item.a.string
            AlbumNamesList.append(st[9:-7])
        for item in soup.find_all(class_="abstract"):
            st = item.contents[0]
            PerformerList.append(st[24:-13])
        for item in soup.find_all(class_="rating_nums"):
            st = str(item.string)
            if (st == "None"):
                st = "0.0"
            RatingList.append(st)
        for item in soup.find_all(class_="ft"):
            type = item.div.attrs['class'][0]
            if (type != "comment-item"):
                st = " \n"
            else:
                st = item.div.blockquote.contents[2]
            CommentsList.append(st)
        for item in soup.find_all(class_="post"):
            st = item.a.img.attrs["src"]
            PicUrlList.append(st)
    pass


def scratchTitle(url):
    text = getHTMLText(url)
    soup = BeautifulSoup(text, "html.parser")
    title = soup.head.title.string
    print(title)
    return title


def printList(ls1, ls2, ls3, ls4):
    length = min(len(ls1), len(ls2), len(ls3), len(ls4))
    for i in range(length):
        print("No.", i + 1)
        print("Album: " + ls1[i])
        print("Rate: " + ls3[i])
        print("Performer: " + ls2[i])
        print("Comment: " + ls4[i])
    pass


def writeList(ls1, ls2, ls3, ls4, title):
    length = min(len(ls1), len(ls2), len(ls3), len(ls4))
    name = title + ".txt"
    with open(name, "w", encoding='utf-8') as f:
        for i in range(length):
            f.write("No." + str(i + 1) + "\n")
            f.write("Album: 《" + ls1[i] + "》\n")
            f.write("Rate: " + ls3[i] + "\n")
            f.write("Performer: " + ls2[i] + "\n")
            f.write("Comment: " + ls4[i] + "\n")
    f.close()
    pass


def main():
    AlbumNamesList = list()
    PerformerList = list()
    CommentsList = list()
    RatingList = list()
    PicUrlList = list()
    url = "https://www.douban.com/doulist/73799/?start="
    title = scratchTitle(url + "0")
    size = getSize(url)
    scratchInfo(AlbumNamesList, PerformerList, RatingList, CommentsList, PicUrlList, size, url)
    deleteList = [0]
    DeleteElement(deleteList, AlbumNamesList, PerformerList, CommentsList, PicUrlList)
    writeList(AlbumNamesList, PerformerList, RatingList, CommentsList, title)
    # downloadPicture(PicUrlList, AlbumNamesList)
    printList(AlbumNamesList, PerformerList, RatingList, CommentsList)


main()
