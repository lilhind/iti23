var students = [
  { fname: "ali", age: 22, grade: 100 },
  { fname: "nora", age: 20, grade: 90 },
  { fname: "nada", age: 25, grade: 75 },
  { fname: "heba", age: 19, grade: 50 },
  { fname: "bassem", age: 21, grade: 40 },
];

// 1. 
students.forEach(function(student) {
  document.write(`<h2>${student.fname} : ${student.age} : ${student.grade}</h2>`);
});

// 2. 
document.write('<h2><font color="red">Students with grades greater than 80:</font></h2>');
var highGrades = students.filter(function(student) {
  return student.grade > 80;
});

highGrades.forEach(function(student) {
  document.write(`<h2>${student.fname} : ${student.age} : ${student.grade}</h2>`);
});

// 3. 
document.write('<h2>Students ordered ascending by names:</h2>');
students.sort(function(a, b) {
  return a.fname.localeCompare(b.fname);
});

students.forEach(function(student) {
  document.write(`<h2>${student.fname} : ${student.age} : ${student.grade}</h2>`);
});