function capitalizeFirstLetterOfWords(str) {
  let words = str.split(" ");

  for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substring(1);
  }

  let capitalizedStr = "";
  for (let i = 0; i < words.length; i++) {
    capitalizedStr += words[i];
    if (i < words.length - 1) {
      capitalizedStr += " ";
    }
  }

  return capitalizedStr;
}

function extractUniqueCharacters(str) {
  let uniqueCharacters = "";

  for (let i = 0; i < str.length; i++) {
    const char = str[i];

    if (str.indexOf(char) === i) {
      uniqueCharacters += char;
    }
  }

  return uniqueCharacters;
}

function findLongestWord(str) {
  let words = str.split(" ");

  let longestWord = "";
  let maxLength = 0;

  for (let i = 0; i < words.length; i++) {
    let currentWord = words[i];
    let currentWordLength = currentWord.length;

    if (currentWordLength > maxLength) {
      maxLength = currentWordLength;
      longestWord = currentWord;
    }
  }

  return longestWord;
}

console.log(capitalizeFirstLetterOfWords("ahmed moh elhindawi Ibr"));
console.log(extractUniqueCharacters("aaaaxxxayhme"));
console.log(findLongestWord("ahmed moh elhindawi Ibr"));
