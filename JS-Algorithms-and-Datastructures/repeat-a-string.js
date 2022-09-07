########################################################
### Repeat a String
########################################################

function repeatStringNumTimes(str, num) {

  let repeatStr = "";
  for(let i = 0; i < num; i++) {
    repeatStr += str;
  }

  return repeatStr;
}

repeatStringNumTimes("abc", 3);
