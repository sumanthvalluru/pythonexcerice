function fibonacciMemo(n, memo = {}) {
    if (n <= 1) {
      return n;
    }
  
    if (memo[n]) {
      return memo[n];
    } else {
      memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
      return memo[n];
    }
  }
  
  // Example: Print the first 10 Fibonacci numbers
  for (let i = 0; i < 10; i++) {
    console.log(fibonacciMemo(i));
  }
  