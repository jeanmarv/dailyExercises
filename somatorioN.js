function digitalRoot(n) {
  let toString = n.toString();
  let splited = toString.split("")
  let somatorio = 0;
  for (let index = 0; index < splited.length; index++) {
    somatorio += parseInt(splited[index]);
  }
  let newSum = 0;
  console.log(`somatorio ${somatorio}`);
  if(somatorio > 9){
    let somatorioToString = somatorio.toString();
    let numbersplit = somatorioToString.split("");
    for (let index = 0; index < numbersplit.length; index++) {
       newSum += parseInt(numbersplit[index]);
    }
    console.log(`newSum ${newSum}`);
    if(newSum > 9){
      let newSumToString = newSum.toString();
      let lastSplit = newSumToString.split("");
      let lastSum = 0;
      for (let index = 0; index < lastSplit.length; index++) {
        lastSum += parseInt(lastSplit[index]);
      }
      console.log(`lastSum ${lastSum}`);
      return lastSum;
    }
    return newSum;
  }
  return somatorio
}

console.log(digitalRoot(493193));

function digital_root(n) {
  if (n < 10)
    return n;

  for (var sum = 0, i = 0, n = String(n); i < n.length; i++)
    sum += Number(n[i]);
   
  return digital_root(sum);
}