# JavaScript - Warm up

This project focuses on warming up with JavaScript, which involves practicing basic coding exercises to strengthen familiarity and understanding of the language's syntax, concepts, and functionalities. It may include tasks such as variable declaration, data types manipulation, conditional statements, loops, functions, and basic algorithms. This exercise is aimed at improving proficiency and comfortability with JavaScript programming.

## Table Of Contents

1. [Background Context](#background-context)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [More Info](more-info)
6. [Outlined Project Tasks](outlined_project_tasks)
7. [Author](#author)

---

## Background Context

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

* **Scripting (same as we did with Python)**
* **Web front-end**
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

## Resources

**Read or watch**
* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
* [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between var, const and let
* What are all the data types available in JavaScript
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* What is a function and how do you use functions
* What does a function that does not use any `return` statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

## Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons](https://github.com/standard/semistandard) on top. Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
* All your files must be executable
* The length of your files will be tested using `wc`

## More Info

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation]()
```
$ sudo npm install semistandard --global
```

### How to Use `semistandard` After Installation

* After installing the semistandard package globally using npm, you can check JavaScript files for compliance with the semi-standard coding style. Execute the`semistandard` command followed by the name of the file or directory you wish to examine:

```
semistandard your_file.js
```

Replace` your_file.js` with the name of the JavaScript file you want to check.

* Additionally, you have the option to examine multiple files or directories simultaneously by using the following command:

```
semistandard  *.js
```

This command will inspect all JavaScript files in the current directory for compliance with the semi-standard coding style.

--- 

# Outlined Project Tasks

## Mandatory Tasks

### 0. First constant, first print

Write a script that prints “JavaScript is amazing”:

* You must create a constant variable called myVar with the value “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [0-javascript_is_amazing.js](0-javascript_is_amazing.js)
 
### 1. 3 languages

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [1-multi_languages.js](1-multi_languages.js)
 
### 2. Arguments

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* **Reference:** [process.argv](https://nodejs.org/api/process.html#process_process_argv)

**File:** [2-arguments.js](2-arguments.js)
 
### 3. Value of my argument

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

**File**: [3-value_argument.js](3-value_argument.js)
 
### 4. Create a sentence

Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [4-concat.js](4-concat.js)
 
### 5. An Integer

Write a script that prints My number: `<first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

**File:** [5-to_integer.js](5-to_integer.js)
 
### 6. Loop to languages

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

**File:** [6-multi_languages_loop.js](6-multi_languages_loop.js)
 
### 7. I love C

Write a script that prints `x` times “C is fun”

Where `x` is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use `console.log(...)` to print all output
You are not allowed to use `var`
You can use only two `console.log`
You must use a loop (`while`, `for`, etc.)

**File:** [7-multi_c.js](7-multi_c.js)
 
### 8. Square

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

**File:** [8-square.js](8-square.js)
 
### 9. Add

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [9-add.js](9-add.js)
 
## 10. Factorial

Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [10-factorial.js](10-factorial.js)
 
### 11. Second biggest!

Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**File:** [11-second_biggest.js](11-second_biggest.js)
 
### 12. Object

Update this script to replace the value `12` with `89`:

* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
```
**File:** [12-object.js](12-object.js)
 
### 13. Add file

Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`
* [Tip](http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)
```
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
```

**File:** [13-add.js](13-add.js)

## Advanded Tasks
 
14. Const or not const

Write a file that modifies the value of `myVar` to `333`
```
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
```

Hint: Scope
**This exercise doesn’t pass `semistandard`** so don’t worry about it.

**File:** [100-let_me_const.js](100-let_me_const.js)
 
### 15. Call me Moby

Write a function that executes x times a function.

* The function must be visible from outside
* Prototype: `function (x, theFunction)`
* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
```
**File:** [101-call_me_moby.js](101-call_me_moby.js)
 
### 16. Add me maybe

Write a function that increments and calls a function.

* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
```
**File:** [102-add_me_maybe.js](102-add_me_maybe.js)
 
### 17. Increment object

Update this script by adding a new function `incr` that increments the integer `value`.

You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
```

**File:** [103-object_fct.js](103-object_fct.js)

---

## Author

[Peter Opoku-Mensah](https://github.com/deezyfg)