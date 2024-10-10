---
layout: essay
type: essay
title: The Importance of UI Frameworks
date: 2024-10-09
published: true
labels:
  - Web Development
  - Bootstrap 5
---

<img alt="Bootstrap Logo" src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" width=200px>

### Why Invest in UI Frameworks?

Despite the learning curve, UI frameworks offer considerable benefits, both in terms of development time and the overall quality of the user interface in comparison to raw HTML and CSS.

### The Drawbacks of Raw HTML/CSS

Building a website with raw HTML and CSS offers us complete control over the aestheitcs of the webiste, but then customizing the layouts to make the website appealing often requires considerable effort. Especially trying to have consisent padding, margins, sizing, etc, across different browsers.

To add, writing raw CSS without using any UI frameworks such as Bootstrap, can feel like re-inventing the wheel. Especially with common UI components such as navigations bars and buttons.

For example, to create a simple "Click Me" button in Bootstap 5, we can do the following:

```html
<button class="btn btn-primary">Click Me</button>
```

In raw HTML/CSS, to create a Bootstrap-like button, we need the following code:

```html
<style>
.custom-button {
  background-color: #007bff;
  color: white;
  padding: 5px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.custom-button:hover {
  background-color: #0056b3;
}
</style>
<button class="custom-button">Click Me</button>
```

The side-by-side rendering is below. It is clear that it requires considerable effort to get the same aesthetic that is out-of-the-box with Bootstrap.

<img alt="Bootstrap Comparison" src="Bootstrap.png" width=200px>

### The Bootstrap 5 Framework

### My Bootstrap 5 Experience

### Conclusion
