exports.creditCheck = function(str) {
  let total = 0;
  str.split("").forEach((s,index) => {
    let num = parseInt(s);
    if (index % 2 == 0){
      num *= 2;
    }
    if (num >= 10) {
      let digits = num.toString().split("");
      num = digits.reduce((acc, current) => {
        return acc + parseInt(current);
      }, 0)
    }
    total += num;
  })
  
  let remain = total % 10;
  if (remain == 0){
    return "The number is valid!"
  } else {
    return "The number is invalid!"
  }
}