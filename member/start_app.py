# 컨트롤러 start_app.py
# templates 폴더, static 폴더
# 웹 서버 - flask

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.secret_key = "asdfqqewr1234%$#"

# sqlite3와 연동 - 연결 객체 생성
def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/memberdb.db")
    return conn
print(getconn())

# url 0 '/' 경로 설정
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

# 회원 목록
@app.route('/memberlist', methods = ['GET'])
def memberlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql)  # 검색 수행
    rs = cursor.fetchall()
    conn.close()
    return render_template('memberlist.html', rs=rs)

# 회원 가입
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 가입 폼에 입력된 자료를 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd1']
        name = request.form['name']
        gender = request.form['gender']

        # db에 저장
        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO member(memberid, passwd, name, gender) " \
              f"VALUES ('{id}', '{pw}', '{name}', '{gender}')"
        # 자동 로그인 - 세션 발급
        session['userid'] = request.form['memberid']
        cursor.execute(sql)
        conn.commit()  # 커밋 완료
        conn.close()

        # redirect - 회원가입 후 회원 목록 페이지로 강제이동
        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')

#로그인 페이지
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인폼에 입력된 데이터 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd']

        # database에 접속 - 로그인 체크
        conn = getconn()
        cursor = conn.cursor()
        # 동적 바인딩
        sql = f"SELECT * FROM member " \
              f"WHERE memberid = '{id}' AND passwd = '{pw}'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        print(rs)
        conn.close()

        if rs:  # rs - True
            session['userid'] = rs[0]  #memberid를 세션에 저장(세션 발급)
            return redirect(url_for('index'))
        else:
            error_msg = "아이디나 비밀번호를 확인해주세요"
            return render_template('login.html', error_msg=error_msg)

    else:
        return render_template('login.html')

# 로그 아웃
@app.route('/logout')
def logout():
    session.clear()  #모든 세션 삭제
    return redirect(url_for('index'))

# 게시판 목록
@app.route('/boardlist', methods = ['GET'])
def boardlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board"
    cursor.execute(sql)
    boardlist = cursor.fetchall()
    # print(boardlist)
    # for board in boardlist:
    #     print(board)
    conn.commit()
    conn.close()
    return render_template('boardlist.html', boardlist=boardlist)


# 글쓰기
@app.route('/writing')
def writing():
    return render_template('writing.html')


    # ※예시※
    # cart = "계란"
    # carts = ['계란', '콩나물', '생수']
    # return render_template('boardlist.html', cart=cart, cartlist=carts)

app.run()