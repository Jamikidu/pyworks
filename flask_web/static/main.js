// 이미지 마우스이벤트
let pic = document.getElementById('pic')
        pic.onmouseover = changePic;
        function changePic(){
            pic.src = "../static/coffee-gray.jpg";
        }
        pic.onmouseout = originPic;
        function originPic(){
            pic.src = "../static/coffee-blue.jpg";
        }