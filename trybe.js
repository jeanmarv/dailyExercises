function isPrime(n) {
  if (n === 1) {
    return 1
  } else if (n === 2) {
    return 1
  }
  let somatorio = 0
  let newArray = []
  for (let i = 2; i <= n; i++) {
    if (n % i === 0) {
      somatorio += 1
      newArray.push(i)
    }
  }
  if (somatorio === 1) {
    return 1
  } if (somatorio > 1 ) {
    return newArray[0]
  };
}
