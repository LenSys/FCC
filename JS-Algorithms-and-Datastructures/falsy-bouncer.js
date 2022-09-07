########################################################
Falsy Bouncer
########################################################

function bouncer(arr) {

  let copyArr = [];
  for(let i = 0; i < arr.length; i++) {
    let boo = arr[i];

    if(new Boolean(boo) == true) {
      copyArr.push(boo);
    }
  }

  console.log( copyArr);
  return copyArr;
}

bouncer([7, "ate", "", false, 9]);
