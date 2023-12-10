<html>   
   <head>
      <title>JavaScript Animation</title>      
      <script type = "text/javascript">
         
            var imgObj = null;
            
            function init() {
               imgObj = document.getElementById('myImage');
               imgObj.style.position= 'relative'; 
               imgObj.style.left = '0px'; 
           }
            function moveRight() {
               imgObj.style.left = parseInt(imgObj.style.left) + 10 + 'px';
            }
            
            window.onload = init;
         
      </script>
   </head>
   
   <body>   
      <form>
         <img id = "myImage" src = "/images/html.gif" />
         <p>Click button below to move the image to right</p>
         <input type = "button" value = "Click Me" onclick = "moveRight();" />
      </form>      
   </body>
</html>