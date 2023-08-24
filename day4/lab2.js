var numbers = [3, 1, 2, 4, 3, 5, 1, 55];
console.log(numbers);

//1
function removeDuplicates(arr) {
  var uniqueArray = [];
  for (let i = 0; i < arr.length; i++) {
    if (uniqueArray.indexOf(arr[i]) === -1) {
      uniqueArray.push(arr[i]);
    }
  }
  return uniqueArray;
}

numbers = removeDuplicates(numbers);
console.log(numbers);

//2
numbers.sort(function (a, b) {
  if (a > b) return 1;
  else if (a < b) return -1;
  else return 0;
});
console.log(numbers);

//3
function filterNumbersGreaterThan50(arr) {
  return arr.filter(function (number) {
    return number > 50;
  });
}

numbers = filterNumbersGreaterThan50(numbers);
console.log(numbers);

numbers = [3, 1, 2, 4, 3, 5, 1, 55];

function findMaxAndMinNumbers(arr) {
  if (arr.length === 0) {
    return { max: undefined, min: undefined };
  }

  var maxNumber = Math.max(...arr);
  var minNumber = Math.min(...arr);

  return { max: maxNumber, min: minNumber };
}

console.log(findMaxAndMinNumbers(numbers));

// 33333333333333333333333333333333333333

arr = [3, 1, 4, 5, 2];

function sumAll(numbersArray) {
  var sum = eval(numbersArray.join("+"));
  var product = eval(numbersArray.join("*"));
  return { sum, product };
}

console.log(sumAll(arr));

// 44444444444444444444444444444444444
function getMonthNameFromDate(date) {
  var months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  var monthIndex = date.getMonth();
  return months[monthIndex];
}

var currentDate = new Date();
console.log("Current Date:", currentDate);
var monthName = getMonthNameFromDate(currentDate);
console.log("Month Name:", monthName);

// 55555555555555555555555555555

function getRandomArray() {
  const arrayLength = Math.floor(Math.random() * 10) + 1; 
  var randomArray = [];

  for (let i = 0; i < arrayLength; i++) {
    const randomNumber = Math.floor(Math.random() * 10) + 1;
    randomArray.push(randomNumber);
  }

  return randomArray;
}

var randomNumbersArray = getRandomArray();
console.log(randomNumbersArray);
