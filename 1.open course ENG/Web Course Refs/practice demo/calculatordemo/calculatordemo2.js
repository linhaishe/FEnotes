//计算过程显示

function get(num){
    var shownum = document.getElementById('display');
    shownum.value+=num;
}

//清空
//获取清空按钮元素
var cc = document.getElementById("clear");
//写处理函数clear()
function clear(){
    document.getElementById('display').value='';
}
cc.addEventListener('click',clear,false);

//回删

var dd = document.getElementById("delete");
function backspace(){
    var shownum = document.getElementById("display");
    shownum.value=shownum.value.substring(0,shownum.value.length-1);
}

dd.addEventListener("click",backspace,false);

//计算

var re = document.getElementById("cal");
function calculates(){
    var result = 0;
    //获取显示框中的表达式
    result = document.getElementById("display").value;
    //eval()函数的功能是：将()里面的表达式进行计算,将计算结果放到显示框中
    document.getElementById("display").value=eval(result);
}
//用addEventListener进行事件的绑定,将“=”按钮、点击事件、处理函数绑定起来
re.addEventListener("click",calculates,false);

//显示时间
function showTime(){
    var today = new Date();
    var y = today.getFullYear();
    var M = today.getMonth()+1;
    var d = today.getDate();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    var week = today.getDay();
    var w = new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday");
    document.getElementById("time").innerHTML=y+"year"+M+"Month"+d+"day"+"</br>"+h+":"+m+":"+s+" "+w[week];
    setTimeout("showTime()",1000);
}

//数字小于10时，前面添加一个0
function checkTime(i){
    if(i<10){
        i="0"+i;
    }
    return i;
}
window.onload = function(){
    showTime();
};