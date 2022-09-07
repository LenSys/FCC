########################################################
### Reverse a String
########################################################

function reverseString(str) {

  const arr = Array.from(str);
  let rev = "";

  for(let i = arr.length - 1; i >= 0; i--) {
    rev += arr[i];
  }

  return rev;
}
