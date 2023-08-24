// Using the default collection of the document object
var images = document.images;
console.log(images);

// Using document method 'querySelectorAll'
var images = document.querySelectorAll("img");
console.log(images);

// Find all options for the City drop-down list:

var cityDropdown = document.getElementById("cityDropdown");
var options = cityDropdown.getElementsByTagName("option");

console.log(options);

//  Find all rows for the second table on the page:

var table2 = document.getElementById("table2");
var rows = table2.getElementsByTagName("tr");

console.log(rows);

// Find all elements that contain the class name 'fontBlue':
var elementsWithFontBlueClass = document.getElementsByClassName("fontBlue");
console.log(elementsWithFontBlueClass);

//2
//a) Get the first anchor inside the second table and change its 'href' property to "training.com" and its text to "Training":

var secondTable = document.getElementById("table2");
var firstAnchor = secondTable.querySelector("a");

firstAnchor.href = "http://training.com";
firstAnchor.textContent = "Training";

// b) Find the last image and change its borders to solid pink 2px:

var images = document.getElementsByTagName("img");
var lastImage = images[images.length - 1];

lastImage.style.border = "2px solid pink";

// c) Create a JavaScript function to find all checkboxes (checked) in the 'userData' form and alert their values:

function findCheckedCheckboxes() {
  var userDataForm = document.getElementById("userData");
  var checkedCheckboxes = userDataForm.querySelectorAll(
    'input[type="checkbox"]:checked'
  );

  var values = [];
  for (var i = 0; i < checkedCheckboxes.length; i++) {
    values.push(checkedCheckboxes[i].value);
  }

  alert("Checked Checkboxes values: " + values.join(", "));
}

findCheckedCheckboxes();

// d) Find the element with the id value "example" and change its background color to pink:

var exampleElement = document.getElementById("example");
exampleElement.style.backgroundColor = "pink";

// change page background

function setGradientBackground() {
  var colors = ["#ff0000", "#00ff00"];
  var direction = "to right"; 

  var gradientColor =
    "linear-gradient(" + direction + ", " + colors[0] + ", " + colors[1] + ")";
  document.body.style.background = gradientColor;
}
