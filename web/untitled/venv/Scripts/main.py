# -*-coding:utf-8 -*-

import webbrowser
f = open('index.html','w')
import io
data_file = io.open("C:/Users/12266/PycharmProjects/untitled/venv/Scripts/index.html", "r", encoding='utf-8')
htmlhandle = data_file.read()
message = """<html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="Pragma" content="no-cache">
	<meta http-equiv="Cache-Control" content="no-cache">
	<meta http-equiv="Expires" content="0">
	<title>Cloud Recognition</title>
	<link href="css/login.css" rel="stylesheet" type="text/css" />
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script src="https://cdn.bootcss.com/jquery/2.2.4/jquery.min.js"></script>
</head>
<body>
<div class="login_box">
      <div class="login_l_img"><img src="picture/login-img.png" /></div>
      <div class="login">
          <div class="login_logo"><a href="#"><img src="picture/login_logo.png" /></a></div>
          <div class="login_name">
               <p>Cloud Recognition</p>
          <form method="post">
			  <input type="file" name="file0" id="file0" accept="image/gif,image/jpeg,image/jpg,image/png,image/svg"/><br>
			  <img src="" id="img0" style="width: 160px;height: 160px;">
          </form>
		      <script type="text/javascript">

        $("#file0").change(function(){
        var objUrl = getObjectURL(this.files[0]) ;//gain file
        console.log("objUrl = "+objUrl);
            if (objUrl) {
                  $("#img0").attr("src", objUrl);
            }
        });

        function getObjectURL(file) {
            var url = null;
            if(window.createObjectURL!=undefined) {
                url = window.createObjectURL(file) ;
            }else if (window.URL!=undefined) { // mozilla(firefox)
                url = window.URL.createObjectURL(file) ;
            }else if (window.webkitURL!=undefined) { // webkit or chrome
                url = window.webkitURL.createObjectURL(file) ;
            }
            return url ;
        }
    </script>
    
    <SCRIPT LANGUAGE="JavaScript">  
    function reP(){  
    document.getElementById('oImg').style.display = "block";  
    }  
    </SCRIPT>  
    <img src='baby.jpg' id="oImg" style='display:none' width="160px" hight="200px">  
    <INPUT TYPE="button" value='PIC' onclick="reP()">  
</body>
      </div>
</div>
</body>
</html>
"""
web="Cloud Recognition"
f.write(message)
f.close()

webbrowser.open_new_tab('index.html')
print(web)
