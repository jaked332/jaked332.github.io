---
layout: essay
type: essay
title: "Building Production-Grade Web Apps: Lessons from ICS 414"
date: 2025-05-12
published: true
labels:
  - Project Management
  - Next.js
---

<img alt="Image" src="https://previews.123rf.com/images/rollingcamera/rollingcamera2003/rollingcamera200303332/143283675-software-engineer-animated-typography.jpg" width=500px>

## Introduction

When I first stepped into ICS 414 -- Software Engineering II, I thought I understood what "production-grade" meant. By the end of the semester, after partnering with a local firm, Spire, to build the Pineapple-Spire Financial Modeling Portal, I learned that true production readiness demands more than working code; it requires excellent project management, stakeholder communication, and a relentless focus on performance, security, and user experience (UX).

## Translating Excel Spreadsheets to TypeScript

Our core challenge was transforming intricate Excel spreadsheets into a live, browser-driven portal. The team and I began by deconstructing nested formulas and re-implementing them in TypeScript modules. To guarantee numerical fidelity, I ran parallel tests in Excel and in TypeScript, iterating until isolated calculations matched to the cent. As forecast horizons extended and datasets grew, I introduced memoization in key components to keep visualizations responsive, even when projecting years into the future.

## GitHub-Based, Issue-Driven Project Management

Early on, our eight-member team adopted a strict, issue-driven GitHub workflow: every feature or bug fix was recorded as a two- to four-day issue; branches followed the `issue-XXX` convention; and our GitHub Projects board tracked velocity, partitioned by milestones, akin to Agile sprints. When our team size dropped to six by mid-term, I assumed greater responsibility for rebalancing the backlog.

## Designing a Stress-Test Version Control Layer

A cornerstone feature I led was versioned stress testing: users could save multiple versions of their tests and load any version to compute Fiscal Sustainability Models. I defined data-model schemas for each iteration, built API endpoints backed by PostgreSQL via Prisma, and crafted an interface that loads versions and processes data with minimal repeated computation. Delivering this feature showed the importance of rigorous testing across different user roles.

## Conclusion

ICS 414 marked a leap from the conceptual prototypes of ICS 314 to a full-fledged, user-centric web application. I emerged with more than polished React components and TypeScript modules; I gained a playbook for professional software delivery: issue-driven development, thorough code reviews, end-to-end ownership, and continuous performance tuning. As I prepare to graduate next year, I'm confident that I've built, tested, and shipped production systems that a real company can depend on.

You can try the application at [https://pineapple-spire-lemon.vercel.app/](https://pineapple-spire-lemon.vercel.app/) and view the codebase at [https://github.com/pineapple-spire/pineapple-spire](https://github.com/pineapple-spire/pineapple-spire).
