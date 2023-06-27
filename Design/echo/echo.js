var content = document.querySelector("#input_str");
var timer;

var echo_content = function ()
{
    clearTimeout(timer);
    timer = setTimeout(function() 
    {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "calculate.php", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send("content=" + content.value);

        xhr.onreadystatechange = function() 
        {
            var res = document.querySelector("#echo_str");
            if(xhr.responseText)
            {
                res.value = JSON.parse(xhr.responseText).content;
            }
        }
    }, 400); // 延迟2秒执行
}

content.addEventListener("input", echo_content);