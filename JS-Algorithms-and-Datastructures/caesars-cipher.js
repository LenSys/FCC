########################################################
### Caesars Cipher
########################################################

function rot13(str) {

  const arr = [];

  for(let i = 0; i < str.length; i++) {
    const charCode = str.charCodeAt(i);
    const char = str[i];

    if( " .,!?".indexOf(char) !== -1) {
      // special char, ignore rotation
      arr.push(char);
    } else {
      // rotate char
      let rotCharCode = charCode + 13;
      if(rotCharCode > 90) {
        rotCharCode = rotCharCode - 90 + 64;
      }

      const rotChar = String.fromCharCode(rotCharCode);
      arr.push(rotChar);

    }
  }

  return arr.join("");
}

console.log(rot13("SERR PBQR PNZC"));
