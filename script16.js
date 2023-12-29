// prints palindrome between min and max
function countPal(min, max)
{
	for (var i = min; i <=max; i++)
	{
		if(isPalindrome(i))
		document.write(i+" " );
	}
}

// Driver program to test above function
countPal(100 , 150);
