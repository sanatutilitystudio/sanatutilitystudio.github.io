---
layout: post
title: "How AI Helped Me Build Sanat Utility Studio"
date: 2026-10-17 10:46:00 +0530
description: "From small mobile websites during medical school to independent Android and Windows tools: how curiosity, AI assistance and careful testing shaped Sanat Utility Studio."
categories: [inside-sus]
tags: [independent-development, ai-assisted-development, early-web]
author: "Sanat Debbarma"
featured: true
permalink: /blog/how-ai-helped-me-build-sanat-utility-studio/
---

*This article is a personal account, not a tutorial promising that a subscription or a few prompts will turn anyone into a software developer.*

## Before the studio, there was a little website

My professional life is in medicine. I studied MBBS, eventually trained in Internal Medicine, and work as a physician. But the interest that led me to Sanat Utility Studio began much earlier, during my medical-school years.

In the late 2000s, I was curious about the web: how pages were built, how links worked, and how someone could put something online without owning a server. I experimented with HTML, tried learning some Java and Python on my own, and published simple pages through free hosting services that were friendly to the mobile phones of the time.

One of those pages was **SanatRuma**, a colourful mobile-oriented website. The [Internet Archive](https://web.archive.org/) preserved a snapshot dated **24 September 2010**. It shows a rather enthusiastic assortment of links to Java and Symbian applications, wallpapers, music, downloads and useful computer utilities.

<figure class="journal-archive-gallery" aria-label="Two redacted screenshots of an archived website from 2010">
  <div class="journal-archive-pair">
    <img src="/assets/sanatruma-2010-introduction.webp" width="600" height="1030" loading="lazy" decoding="async" alt="Redacted Internet Archive screenshot showing the 24 September 2010 capture of SanatRuma, its student-era introduction and mobile software links.">
    <img src="/assets/sanatruma-2010-downloads.webp" width="600" height="1017" loading="lazy" decoding="async" alt="Redacted screenshot of the early SanatRuma site showing colourful lists of Java and Symbian downloads, wallpapers, utilities and mobile links.">
  </div>
  <figcaption>SanatRuma as preserved in a September 2010 Internet Archive capture. These are cropped screenshots; historical contact details and a sharing code have been redacted for privacy. They show the site as it appeared, not a recreation.</figcaption>
</figure>

Looking at it now, the colours are a lot to take in. Dark backgrounds, bright blue links, green text and tightly packed sections were evidently all welcome at the same party. I would design it differently today. But I am glad that version still exists, because it captures the curiosity that started everything.

There was no grand business plan. I was a medical student experimenting with what I could learn and publish. That was enough reason to begin.

## Medicine continued. So did the curiosity.

I did not leave medicine for software engineering. Clinical practice and postgraduate medical training remained my career, and technology lived alongside them as an independent interest.

Over time, the tools changed. Smartphones replaced many of the devices for which those old Java and Symbian links were intended. The idea of a personal website also changed: a page could be a portfolio, a project journal, a support site or a place to share useful technical lessons.

What stayed constant was the appeal of taking a practical problem and making a tool that could help someone solve it.

**Sanat Utility Studio** grew from that interest. The studio now brings together several kinds of projects: Android utilities, desktop tools for media workflows, and experiments with local AI. Not everything is equally mature. Some projects are publicly released, while others are in private testing or active development. Keeping those distinctions visible matters to me.

## Where AI became useful

I do not have a formal computer science degree. That means there are gaps in my knowledge, and I would rather acknowledge them than pretend they do not exist.

Modern AI assistants have made it easier for me to work through those gaps. I can ask for an explanation of a framework, compare approaches to a UI, investigate a build error or understand why a particular implementation is fragile. When an explanation is unclear, I can question it, test it and ask for another route.

That changes the pace of learning. A problem that once sent me searching through disconnected forum posts can become a more structured investigation.

But the distinction is important: **asking AI for code is not the same as shipping reliable software**.

An AI suggestion still needs to be understood in context. It needs to be tested against real requirements. It can introduce incorrect assumptions, unnecessary dependencies, security problems or a solution that simply does not suit the product.

## What the projects taught me

Consider three different kinds of work in the studio.

**KCalLog**, an Android nutrition-tracking application, involves choices about how users record foods, review nutrition and set goals. An assistant can help explore data structures or interface patterns. It cannot decide, on its own, which compromises make sense for the people using the app.

**KiloPic** deals with resizing and compressing images. Even a focused utility has practical details: controlling image dimensions, balancing output size with quality, communicating estimates, and deciding which features belong in its different editions. Those decisions require product judgment and hands-on checks.

**AudioPrep Studio**, a Windows desktop tool, works with audio conversion, metadata and artwork. Coordinating user inputs with tools such as FFmpeg calls for careful file handling, predictable exports and repeated testing. A plausible-looking code snippet is not proof that an output file is correct.

The applications differ, but the process is similar: define a useful task, design a workflow, implement it, test what actually happens, and revise it.

AI has helped me at several of those stages. It has not removed the responsibility for any of them.

## Building independently does not mean building effortlessly

There is a tempting story online that software is now simply a matter of describing an app and pressing a button. It makes for an eye-catching headline, but it leaves out most of the work.

A useful application needs more than code that runs once. It needs sensible defaults, clear messages when something goes wrong, readable layouts, reliable storage or export behaviour, appropriate privacy protections, and a release process that does not break existing users' workflows.

The less glamorous work matters too: checking package versions, reviewing permissions, fixing build configurations, understanding distribution requirements, and documenting what a tool really does. Those details can be frustrating. They are also part of the craft.

When an AI response is wrong, I still have to recognize the problem. When an app behaves unexpectedly, I still have to investigate it. When a feature feels unnecessary, I still have to decide whether to remove it.

I have learned to regard AI as an unusually accessible development assistant, not an authority that replaces verification.

## The distance between 2010 and today

The early site was largely about discovering and sharing software and resources that interested me. Sanat Utility Studio is increasingly about **building** the tools themselves.

That change did not happen in a straight line, and I do not want to manufacture a neat origin story. Medicine occupied much of the intervening time. Technology kept drawing me back.

Now the studio website has a journal as well as an app catalogue. I want to use it to describe real development decisions, explain experiments, share tutorials when I have something useful to teach, and discuss AI news with clear links to original sources.

There will be successful experiments, abandoned ideas and mistakes worth documenting. I would rather make those visible than present every project as an effortless success.

> AI was the tool, not the creative pilot. It helped me navigate problems, but the curiosity and direction stayed mine.

That is the simplest way I can describe this journey so far.

If you are curious about the software itself, you can [explore the studio's applications](/#products). If you would rather follow the work behind them, the [studio journal](/blog/) is where I will keep those notes.

---

*Editorial note: This story is a draft based on the developer's recollections and supplied archive screenshots. Project examples describe development concerns, not independent endorsements or guarantees of performance. Historical images are cropped and redacted.*
