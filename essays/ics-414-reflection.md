---
layout: essay
type: essay
title: "Building Production-Grade Web Apps: Lessons from ICS 414"
date: 2025-05-12
published: true
labels:
  - Project Management
  - Next.js
  - React
---

## Introduction

When I first stepped into ICS 414 -- Software Engineering II, I thought I understood the meaning of *production-grade*. By semester's end, after partnering with a local firm (Spire) to build Pineapple-Spire Financial Modeling Portal, I learned that true production readiness demands more than working code. It calls for excellent project management, stakeholder communication, and a focus on performance, security, and user experience (UX).

## Translating Excel Spreadsheets to TypeScript

Our core challenge was to transform intricate Excel spreadsheets into a live, browser-driven portal. The team and I began with deconstructing nested formulas, then re-implementing them in TypeScript modules. To guarantee numerical fidelity, I did parallel tests in Excel and TypeScript to ensure consistent isolated calculations, iterating until they matched to the cent. As forecast horizons stretched and datasets grew, I introduced memoization in various components to keep visualization snappy even when forecasting for several years in the future.

## GitHub-Based Issue-Driven Project Management

Early on, our eight-members team adopted a strict, issue-driven GitHub workflow; every feature or bugfix was recorded as a two- to four-day issue, branches named `issue-XXX`, and our GitHub Projects board tracked our velocity -- partitioned by *milestones* which is similar to the concept of Agile sprint. When membership dropped to six by mid-term, I assumed higher responsibility rebalancing our backlog.

## Designing Stress Test Version Control Layer

A cornerstone feature that I owned was the ability to save several versions of the stress tests and load the desired version to compute the Fiscal Sustainability Models per test. I authored data model schemas for each iteration, built several API endpoints backed by PostgreSQL via Prisma, and crafted an interface to load versions and model the data with minimal repeated computations. This was a significant feature of the application that taught me the importance of rigorous testing with different user roles.

## Conclusion

ICS 414 was a leap from conceptual prototypes in ICS 314 to full-fledged, user-centric web application. I emerged with more than polished React components and TypeScript modules; I gained a playbook for professional software delivery: issue-driven development, code review, end-to-end ownership, and continuous performance tuning. As I prepare to graduate next year, I feel grounded by the confidence that I've built, tested, and shipped a production systems that a real company can depend on. 
