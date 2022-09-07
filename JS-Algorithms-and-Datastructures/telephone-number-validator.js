########################################################
### Telephone Number Validator
########################################################

function telephoneCheck(str) {

  // 555-555-5555
  const regex1 = /^[0-9]{3}-[0-9]{3}-[0-9]{4}/;
  if(regex1.test(str)) {
    console.log("regex 1", str);
    return true;
  }

  // (555)555-5555
  const regex2 = /^\([0-9]{3}\)[0-9]{3}-[0-9]{4}/;
  if(regex2.test(str)) {
    console.log("regex 2", str);
    return true;
  }

  // (555) 555-5555
  const regex3 = /^\([0-9]{3}\) [0-9]{3}-[0-9]{4}/;
  if(regex3.test(str)) {
    console.log("regex 3", str);
    return true;
  }

  // 555 555 5555
  const regex4 = /^[0-9]{3} [0-9]{3} [0-9]{4}/;
  if(regex4.test(str)) {
    console.log("regex 4", str);
    return true;
  }

  // 5555555555
  const regex5 = /^[0-9]{10}$/;
  if(regex5.test(str)) {
    console.log("regex 5", str);
    return true;
  }

  // 1 555 555 5555
  const regex6 = /^1 [0-9]{3} [0-9]{3} [0-9]{4}/;
  if(regex6.test(str)) {
    console.log("regex 6", str);
    return true;
  }

  // 1 555-555-5555
  const regex7 = /^1 [0-9]{3}-[0-9]{3}-[0-9]{4}/;
  if(regex7.test(str)) {
    console.log("regex 7", str);
    return true;
  }

  // 1 (555) 555-5555
  const regex8 = /^1 \([0-9]{3}\) [0-9]{3}-[0-9]{4}/;
  if(regex8.test(str)) {
    console.log("regex 8", str);
    return true;
  }

  // 1(555)555-5555
  const regex9 = /^1\([0-9]{3}\)[0-9]{3}-[0-9]{4}/;
  if(regex9.test(str)) {
    console.log("regex 9", str);
    return true;
  }

  console.log("false", str);
  return false;
}

telephoneCheck("1(555)555-5555")
// telephoneCheck("555-555-5555");
// telephoneCheck("(6054756961)");
// telephoneCheck("2 (757) 622-7382")
// telephoneCheck("27576227382")
