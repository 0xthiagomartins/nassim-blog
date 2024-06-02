---
title: "Complete Guide to Async/Await in JavaScript"
categories: [Software, Javascript]
author: "Samuel Poiani"
contacts:
  github: "samuelpoiani"
  linkedin: "samuelpoiani"

donations:
  pix: "11992978992"
date: 2024-06-01
---


# Complete Guide to Async/Await in JavaScript

JavaScript is a single-threaded programming language that uses an event-driven, non-blocking model for I/O operations. Before ECMAScript 2017, JavaScript developers used callbacks and Promises to handle asynchronous operations. With the introduction of `async` and `await`, writing asynchronous code has become much more intuitive and readable.

## What Are Async and Await?

- **`async`**: Declares an asynchronous function. When called, this function returns a `Promise`.
- **`await`**: Can only be used inside asynchronous functions and pauses the execution of the function until the `Promise` is resolved or rejected.

![Async/Await](https://via.placeholder.com/600x400)

## How to Use Async/Await

Let's explore the basic syntax and usage examples.

### Basic Syntax

```javascript
async function myFunction() {
  const value = await anotherAsyncFunction();
  console.log(value);
}
```

In this example, `myFunction` is an asynchronous function that waits for the resolution of `anotherAsyncFunction` before continuing execution.

### Practical Example

```javascript
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function example() {
  console.log('Start');
  await wait(2000); // Pause for 2 seconds
  console.log('End');
}

example();
```

In the example above, the `wait` function returns a `Promise` that resolves after 2 seconds. The `example` function uses `await` to wait for the resolution before continuing.

![Promise](https://via.placeholder.com/600x400)

### Error Handling

Using `try/catch` with `async/await` makes error handling more intuitive:

```javascript
async function exampleWithError() {
  try {
    await wait(2000);
    throw new Error('Something went wrong!');
  } catch (error) {
    console.error('Caught error:', error);
  }
}

exampleWithError();
```

### Running Multiple Promises in Parallel

You can use `Promise.all` to run multiple Promises in parallel and wait for all of them to resolve:

```javascript
async function parallelExample() {
  const [res1, res2, res3] = await Promise.all([
    wait(1000),
    wait(2000),
    wait(3000)
  ]);

  console.log('All promises resolved:', res1, res2, res3);
}

parallelExample();
```

### Advantages of Async/Await

1. **Readability:**
   Asynchronous code written with `async/await` is easier to read and understand compared to complex chains of `.then()` and `.catch()`.

2. **Error Handling:**
   Using `try/catch`, we can handle errors in a way that is similar to synchronous code, making error handling more intuitive.

3. **Debugging:**
   Debugging asynchronous code is simpler because the flow of the code is more linear and resembles synchronous code.

![Debugging](https://via.placeholder.com/600x400)

### Comparison with Promises

To illustrate the difference, here is how the same example would be written using Promises:

```javascript
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function exampleWithPromises() {
  console.log('Start');
  wait(2000).then(() => {
    console.log('End');
  });
}

exampleWithPromises();
```

### Using Async/Await with Fetch

A common use of `async/await` is making HTTP requests using the Fetch API:

```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Request failed');
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData('https://api.example.com/data');
```

![Fetch](https://via.placeholder.com/600x400)

## Conclusion

`async` and `await` simplify working with asynchronous operations in JavaScript, making the code more readable and maintainable. With this guide, you should be ready to start using `async/await` in your projects and enjoy all its advantages.

{{ footer(page.meta) }}