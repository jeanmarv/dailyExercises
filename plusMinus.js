function plusMinus(arr) {
  let somatorioPos = 0;
  let somatorioZero = 0;
  let somatorioNegative = 0;
  arr.forEach(element => {
    if (element > 0){
    somatorioPos += 1
    }
    if (element === 0){
      somatorioZero += 1
    }
    if (element < 0){
      somatorioNegative += 1
    }
  });
  const resultArray = [(somatorioPos/arr.length).toFixed(6), (somatorioNegative/arr.length).toFixed(6), (somatorioZero/arr.length).toFixed(6)]
  resultArray.forEach(element => {
    console.log(element);
  })
}