window.onload = function(){
    setInterval(mywatch, 1000); //함수 호출

    function mywatch(){
        const date = new Date()
        let now = date.toLocaleTimeString();
        document.getElementById("demo").innerHTML = now;
    }
}