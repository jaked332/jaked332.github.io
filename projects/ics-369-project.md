---
layout: project
type: project
image: img/ics-369-1.png
title: "Building a Quest"
date: 2023
published: true
labels:
  - C Sharp
  - Unity
summary: "Unity and C# to develop a game about a boy's quest to find a flower and save his sick mother."
---

<img alt="Image" src="img/ics-369-1.png" style="width: 1132px; height: 538px;">

In my ICS 369 class, my group set out to create a game that told the story of a boy on a heartfelt mission to find a special flower to heal his sick mother. Although the concept was simple, bringing it to life presented a unique set of challenges, particularly for me, as I had little background in using the Unity engine. I had always been interested in game development, but this project was the first time I actually got to dive into the technical aspects of building a game from scratch. The learning curve was steep, but the experience was invaluable.

One of the most exciting things I learned was how to use C# to control game mechanics. For instance, I had to write scripts to control the movement of the boy character, handle collision detection, and trigger events in the story. I remember spending hours figuring out how to get the character to interact with the environment. At one point, I needed to make the character pick up an item, and after some trial and error, I managed to write a simple code like this:

```csharp
void OnTriggerEnter(Collider other)
{
    if(other.gameObject.CompareTag("Flower"))
    {
        other.gameObject.SetActive(false);
        hasFlower = true;
    }
}
```

This small piece of code made the gameplay more interactive, and seeing it work in the game felt incredibly rewarding. Every time I solved a problem, no matter how small, it boosted my confidence in using Unity and reinforced my love for coding.

Throughout the development process, I gained a better understanding of Unity's interface, scene management, and even some basics of animation. I also learned how to work with game assets, implement user interfaces, and optimize the game's performance to make it run smoothly. By the end of the project, I was much more comfortable with Unity and proud of the game we had created as a team. This experience not only deepened my technical skills but also sparked a greater interest in pursuing game development further.
