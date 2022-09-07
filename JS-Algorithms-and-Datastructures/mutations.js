########################################################
### Mutations
########################################################

function mutation(arr) {

  for(let i = 0; i < arr[1].length; i++) {
    if(arr[0].toLowerCase().indexOf(arr[1][i].toLowerCase()) === -1) {
      // char not in word
      return false;
      break;
    }
  }

  return true;
}

// mutation(["hello", "hey"]);
mutation(["Mary", "Army"]);
