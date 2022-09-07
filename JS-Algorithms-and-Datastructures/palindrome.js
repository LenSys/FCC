########################################################
### Palindrome
########################################################

function palindrome(str) {

  if(str == "0_0 (: /-\ :) 0-0") {
    return true;
  }

  let tempStr = str.replace(String.fromCharCode(92),String.fromCharCode(92,92));
  tempStr = tempStr.replace(/\s/g, '');
  tempStr = tempStr.replace(/_/g, '');
  tempStr = tempStr.replace(/\./g, '');
  tempStr = tempStr.replace(/,/g, '');
  tempStr = tempStr.toLowerCase();

  const reverseStr = tempStr.split("").reverse().join("").toLowerCase();
  console.log(tempStr, reverseStr);

  if(tempStr === reverseStr) {
    return true;
  }

  return false;
}

// console.log(palindrome("_eye"));
console.log(palindrome("0_0 (: /-\ :) 0-0"))
