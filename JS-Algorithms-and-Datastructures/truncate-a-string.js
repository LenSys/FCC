########################################################
### Truncate a String
########################################################

function truncateString(str, num) {

  let isLonger = (str.length > num);
  let truncatedStr = str.substring(0, num);

  if(isLonger) {
    truncatedStr += "...";
  }

  console.log( truncatedStr );
  return truncatedStr;
}

truncateString("A-tisket a-tasket A green and yellow basket", 8);
