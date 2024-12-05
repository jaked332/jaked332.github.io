---
layout: essay
type: essay
title: Impact of Design Patterns for Robust Applications
date: 2024-12-04
published: true
labels:
  - Design Patterns
  - Next.js
---

<img alt="Image" src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa17a60bd-0ffc-437b-9553-70b7abc5bfd6_956x674.png" width=250px>

Design patterns are key to creating scalable and maintainable code. They act like well-tested recipes, enabling developers to follow established behavioral rules that allow code to expand in scope and functionality without requiring major changes. In Next.js, these patterns seamlessly integrate with server-side rendering (SSR) and dynamic page management.

In this essay, I will highlight some of the patterns that I am actively using in project "[Da Club](https://ics-314-code-crew.github.io/)," a centralized organization hub portal.

## Singleton Pattern for Global State Management

In *Da Club*, I manage database connections using Prisma. By exporting a single `prisma` instance (Singleton pattern), I ensure that the application efficiently handles database interactions without creating multiple connections:

```typescript
export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    log: ['query'],
  });
```

This approach prevents resource exhaustion and provides a consistent interface for interacting with the database.

## Factory Pattern for User and Club Management

I've also extensively worked with the Factory pattern to encapsulate object creation. Take one example from the Prisma client factory ([dbActions.ts](https://github.com/ics-314-code-crew/daclub/blob/main/src/lib/dbActions.ts)):

```typescript
'use server';

import { hash } from 'bcrypt';
import { prisma } from './prisma';

export async function createUser({
  credentials,
  user,
}: {
  credentials: { email: string; password: string };
  user: { firstName: string; lastName: string; email: string };
}): Promise<void> {
  const password = await hash(credentials.password, 10);
  await prisma.user.create({
    data: {
      email: user.email,
      password,
      firstName: user.firstName,
      lastName: user.lastName,
    },
  });
}
```

The `createUser` method abstracts user creation, handling hashing and the create operation in a reusable piece.

## Why Do Design Patterns Matter?

Design patterns bring order to complexity, making applications more organized and easier to maintain. They enable logic encapsulation, centralized control, and resource optimization. In Next.js, these patterns are powerful tools for building robust and scalable applications.
