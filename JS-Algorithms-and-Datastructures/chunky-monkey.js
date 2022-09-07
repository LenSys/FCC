########################################################
### Chunky Monkey
########################################################
Write a function that splits an array (first argument) into
groups the length of size (second argument) and returns them
as a two-dimensional array.

function chunkArrayInGroups(arr, size) {

  if(size == 0) {
    return [];
  }

  let newArr = [];
  for(let i = 0; i < arr.length; i++) {
    let arrIndex = Math.floor(i / size);
    if(newArr[arrIndex] === undefined) {
      newArr[arrIndex] = [];
    }
    newArr[arrIndex].push(arr[i]);

  }

  console.log(newArr);
  return newArr;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
