// program to generate a multiplication table

// take input from the user
const number = parseInt(prompt('Enter an integer: '));

//creating a multiplication table
for(let i = 1; i <= 10; i++) {

    // multiply i with number
    const result = i * number;

    // display the result
    console.log(`${number} * ${i} = ${result}`);
}


/* program to generate a multiplication table
upto a range */

// take number input from the user
const number1 = parseInt(prompt('Enter an integer: '));

// take range input from the user
const range = parseInt(prompt('Enter a range: '));

//creating a multiplication table
for(let i = 1; i <= range; i++) {
    const result = i * number1;
    console.log(`${number1} * ${i} = ${result}`);
}


// program for a simple calculator

// take the operator input
const operator = prompt('Enter operator ( either +, -, * or / ): ');

// take the operand input
const number3 = parseFloat(prompt('Enter first number: '));
const number2 = parseFloat(prompt('Enter second number: '));

let result;

// using if...else if... else
if (operator == '+') {
    result = number3 + number2;
}
else if (operator == '-') {
    result = number3 - number2;
}
else if (operator == '*') {
    result = number3 * number2;
}
else {
    result = number3 / number2;
}

// display the result
console.log(`${number3} ${operator} ${number2} = ${result}`);