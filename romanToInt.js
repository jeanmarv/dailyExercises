function romanToInt (s) {
  let splited = s.split("");
  let splitobj = {
    'I':1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  console.log(`vogal: ${[splited[0]]}`);
  console.log(`numero: ${splitobj[splited[1]]}`);
  let somatorio = 0
  for (let index = 0; index < splited.length; index++) {
    let atual = splitobj[splited[index]];
    if(splitobj[splited[index +1]] > splitobj[splited[index]]) {
      atual = splitobj[splited[index]] * -1;
    }
    somatorio += atual;
  }
  console.log(`somatorio: ${somatorio}`);
  return somatorio
};