---
layout: essay
type: essay
title: "Igniting the Code"
# All dates must be YYYY-MM-DD format!
date: 2024-09-04
published: true
labels:
  - Software Engineering
  - Learning
---


JavaScript was the first language I learned, and it helped me understand the basics of programming, particularly for creating interactive elements for websites. Over the past couple of weeks, I've started learning TypeScript, a superset of JavaScript that adds static typing. This capability enhances error detection and makes the code more readable.

In JavaScript, to write a function for adding two numbers, we can do:

```javascript
function add(n1, n2) {
  return n1 + n2;
}
```

In TypeScript, we can write the same addition function but with types:

```typescript
function add(n1: number, n2: number): number {
  return n1 + n2;
}
```

The benefit of writing the above code using TypeScript is that it would prevent unexpected behavior, such as adding a number to a string. For example, in JavaScript, `console.log(add(10, "10"))` is valid, but in TypeScript, passing a string instead of a number will be flagged as an error.

The athletic software engineering approach with its practice WOD exercises is new to me. It’s challenging but effective for learning under time constraints. While this method can be a bit stressful, I find it helpful in developing problem-solving skills.

Compared to other programming languages that I've studied, like C and C++, JavaScript and TypeScript are easier to learn and use. The WODs could be more difficult in other languages, but the approach is very compatible with the simplicity of TypeScript.

Overall, I think TypeScript is a strong tool to learn about, and the athletic approach is challenging but beneficial for becoming a better developer.
