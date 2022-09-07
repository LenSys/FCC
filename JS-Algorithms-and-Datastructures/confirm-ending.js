########################################################
### Confirm the Ending
########################################################

Check if a string (first argument, str) ends with the given
target string (second argument, target).

function confirmEnding(str, target) {

  const lastChar = str.substring(str.length, str.length - target.length);

  return (lastChar === target);
}

confirmEnding("Bastian", "n");
