# 파일 읽기

# 파일 개방 open("경로", "r")
try:
    f = open("c:/pyfile/file1.txt", "r")



    # 파일 읽기
    data = f.read()
    print(data)

    # 파일 종료
    f.close()
except:
    print("파일을 찾을 수 없습니다.")  # 파일이 없거나 경로가 잘못되었을때 나오는 문구