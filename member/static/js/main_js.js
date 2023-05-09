window.onload = function(){
    // 디지털 시계
    setInterval(mywatch, 1000); //함수 호출

    function mywatch(){
        const date = new Date()
        let now = date.toLocaleTimeString();
        document.getElementById("demo").innerHTML = now;
    }

    // 배경 이미지 슬라이딩
    // 경로 주의 - static 폴더에서 시작
    let picture = [
    "../static/images/header1.jpg",
    "../static/images/header2.jpg",
    "../static/images/header3.jpg"
    ]

    let imgIdx = 0;

    showPicture();  // showPicture() 함수 호출

    function showPicture(){
        let img = document.getElementById("pic");
        img.src = picture[imgIdx]  // 첫 이미지 저장
        imgIdx++
        if(imgIdx == 3){ // imgIdx == picture.length
            imgIdx = 0;
        }
        setTimeout(showPicture, 3000);
    }

    // 1초 간격으로 함수 호출

}