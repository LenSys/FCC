########################################################
### Roman Numeral Converter
########################################################

function convertToRoman(num) {

  let str = "";
  let checkNum = num;

  const arabicNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const romanNums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];

  for(let i = 0; i < arabicNums.length; i++) {

    const currArabicNum = arabicNums[i];
    const currRomanNum = romanNums[i];

    // console.log(currArabicNum, currRomanNum);

    while(checkNum >= currArabicNum) {
      str += currRomanNum;
      checkNum -= currArabicNum;
    }
  }

 return str;
}

console.log(convertToRoman(36));
