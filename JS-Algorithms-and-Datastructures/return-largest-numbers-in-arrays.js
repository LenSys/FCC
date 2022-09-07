########################################################
### Return Largest Numbers in Arrays
########################################################

function largestOfFour(arr) {

  let maxArr = [];

  for(let i = 0; i < arr.length; i++) {
    let maxNum = undefined;
    let searchArr = arr[i];
    for(let j = 0; j < searchArr.length; j++) {
      if((maxNum === undefined) || (searchArr[j] > maxNum)) {
        maxNum = searchArr[j];
      }
    }

    maxArr[i] = maxNum;
  }
  console.log(maxArr);

  return maxArr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
