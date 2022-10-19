function find_max(nums) {
  let max_num = 0 // smaller than all other numbers
  for (let num of nums) {
    if (num > max_num) {
      max_num = num;
    }
  }
  return max_num;
}

console.log(find_max([1, 2, 6 , 8, 12, 9]))