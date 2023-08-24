function typeText(windowObj, text) {
  var index = 0;

  var interval = setInterval(function() {
    if (index < text.length) {
      windowObj.document.getElementById('message').innerHTML += text.charAt(index);
      index++;
    } else {
      clearInterval(interval);
      setTimeout(function() {
        windowObj.close();
      }, 1500); 
    }
  }, 500); 
}

function showWelcomeMessage() {
  var message = "Welcome to JS";
  var newWindow = window.open('', '', 'width=200,height=100,left=200,top=200');
  newWindow.document.write('<p id="message"></p>');
  typeText(newWindow, message);
}

showWelcomeMessage();