// program to display fibonacci sequence using recursion
function fibonacci(num) {
    if(num < 2) {
        return num;
    }
    else {
        return fibonacci(num-1) + fibonacci(num - 2);
    }
}

// take nth term input from the user
const nTerms = prompt('Enter the number of terms: ');

if(nTerms <=0) {
    console.log('Enter a positive integer.');
}
else {
    for(let i = 0; i < nTerms; i++) {
        console.log(fibonacci(i));
    }
}


// program to find the largest among three numbers

// take input from the user
const num7 = parseFloat(prompt("Enter first number: "));
const num8 = parseFloat(prompt("Enter second number: "));
const num9 = parseFloat(prompt("Enter third number: "));
let largest1;

// check the condition
if(num7 >= num8 && num7 >= num8) {
    largest1 = num7;
}
else if (num8 >= num7 && num8 >= num9) {
    largest = num2;
}
else {
    largest = num9;
}

// display the result
console.log("The largest number is " + largest);

// program to find the largest among three numbers

// take input from the user
const num1 = parseFloat(prompt("Enter first number: "));
const num2 = parseFloat(prompt("Enter second number: "));
const num3 = parseFloat(prompt("Enter third number: "));

const largest = Math.max(num1, num2, num3);

// display the result
console.log("The largest number is " + largest);