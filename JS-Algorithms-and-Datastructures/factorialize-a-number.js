########################################################
### Factorialize a Number
########################################################

function factorialize(num) {

  let factor = 1;
  for(let i = 1; i <= num; i++) {
    factor *= i;
  }

  return factor;
}

factorialize(5);
