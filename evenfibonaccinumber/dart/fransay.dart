// Author: Fransay
// Date: 29/04/2023
// Description: Project Euler(Sum of Even Fibonaccinumbers)
// Complexity: O(n)


void main(){
  int countNumber = 0; // counting number starting at zero
  var sumEvenFib = 0; // sum of even fibonacci numbers
  const LIMIT = 4000000; // fibonacci sequence must not exceed LIMIT
  var firstFibNumber = countNumber; // first fib number 
  var secondFibNumber = firstFibNumber + 1; // second fib number (firstNumber + 1)

  while (firstFibNumber <= LIMIT){
    var thirdFibNumber = firstFibNumber + secondFibNumber;
    if (even(thirdFibNumber)){
      sumEvenFib = sumEvenFib + thirdFibNumber;
    }
    firstFibNumber = secondFibNumber;
    secondFibNumber = thirdFibNumber;
  }
  print("SUM OF EVEN FIB NUMBERS: $sumEvenFib"); 
}

// even function: checks if a number is even or not
bool even(int number){
  if (number % 2 == 0){
    return true;
  }
  return false;
}