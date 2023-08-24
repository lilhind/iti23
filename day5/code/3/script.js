function createDivWithNumber(number) {
  const div = document.createElement("div");
  div.className = "box";
  div.innerText = number;
  div.style.border = "5px solid red";
  div.style.padding = "10px";
  div.style.display = "inline-block";
  document.title = number;
  document.body.appendChild(div);
  const br = document.createElement("br");
  document.body.appendChild(br)
}

var num = 1;

setInterval(() => {
    createDivWithNumber(num);
    num++;
}, 1000);