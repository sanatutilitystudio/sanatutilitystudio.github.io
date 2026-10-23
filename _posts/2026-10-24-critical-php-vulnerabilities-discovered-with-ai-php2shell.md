---
layout: post
title: "Critical PHP Vulnerabilities Discovered With AI: What Website Owners Need to Know"
date: 2026-10-24 02:17:48 +0530
description: "The PHP2Shell incident explained in simple terms: how AI helped uncover critical PHP flaws, what attackers could do, and three actions website developers should take."
categories: [tech-updates]
tags: [php, php2shell, cybersecurity, ai, web-security, wordpress]
author: "Sanat Utility Studio"
image: "/assets/sus-php2shell-hero.webp"
published: true
sitemap: true
permalink: /blog/critical-php-vulnerabilities-ai-php2shell/
---

<figure class="journal-archive-gallery">
  <img src="/assets/sus-php2shell-hero.webp" width="1672" height="941" decoding="async" alt="Editorial illustration of a PHP web server, security warnings and AI-assisted vulnerability analysis.">
  <figcaption>Conceptual illustration of PHP security research. The sample code and dashboard alerts are illustrative, not actual PHP2Shell exploit code or attack records.</figcaption>
</figure>

*The PHP2Shell incident*

On 21 October 2026, the PHP development team released emergency security updates for two critical vulnerabilities in the software behind a large part of the web. Security researchers warned that attackers could potentially run unauthorized code on affected servers without even logging in.

The unusual part of this story is that artificial intelligence helped researchers uncover and investigate the flaws.

Before getting into the security terminology, it is worth understanding what PHP does, what PHP2Shell means and why website owners should pay attention.

## First, what is PHP?

We visit websites every day without thinking about the technology working behind them. When we submit a form, sign in or search a website, software on a server often processes that request.

PHP is one of the programming languages used for that work. Think of a restaurant: customers see the menu and dining room, while the kitchen handles what makes the service possible. PHP often plays a similar behind-the-scenes role.

It is used by popular website platforms such as WordPress, Drupal and Joomla. According to [W3Techs](https://w3techs.com/technologies/details/pl-php), PHP accounts for a large majority of websites whose server-side programming language can be identified. That does **not** mean all those websites were vulnerable or compromised.

## What is PHP2Shell, and how does it work?

PHP2Shell is a name given to serious security flaws in PHP's core engine. It is not a new virus, a plugin or a program that someone installs.

The vulnerabilities involve *memory handling*. In simple terms, software needs to set aside memory while it works and manage that memory correctly when a task ends or fails. Researchers found situations where PHP could incorrectly handle internal memory and request data.

Under vulnerable conditions, a specially crafted web request could exploit those mistakes. A website might have a secure login system and well-written application code, but the problem could exist deeper down in the software running that website.

The two principal vulnerabilities are **CVE-2026-109618** and **CVE-2026-109619**. They can allow *remote code execution*, often shortened to **RCE**. That means an attacker may be able to make a vulnerable server execute instructions it was never meant to accept, potentially without a username or password. The [PHP security advisory](https://www.php.net/archive/2026.php) recommends immediate updates.

<figure class="journal-archive-gallery">
  <img src="/assets/sus-php2shell-explainer.webp" width="1448" height="1086" loading="lazy" decoding="async" alt="Four-panel conceptual guide explaining PHP, PHP2Shell, possible server compromise and protective steps for developers.">
  <figcaption>PHP and PHP2Shell in simple terms. The diagrams illustrate the concept, not the actual memory-safety mechanisms or verified attack paths.</figcaption>
</figure>

## What could happen if attackers exploit it?

The outcome depends on the vulnerable server, its configuration and the permissions available. A successful attacker could potentially run unauthorized commands, alter website content or gain access to sensitive information.

One of the reported issues also involves exposure of process memory, where information such as authentication tokens, credentials or API keys might be present. In some environments, an attacker could use such access to compromise more of the system.

But there is an important distinction: **a website being vulnerable does not mean it has already been hacked.** Likewise, a malicious request detected by a security service is not proof that it succeeded.

## How did AI help discover the flaws?

According to [OpenAI's disclosure](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/), security researcher Calif identified a critical PHP flaw with help from GPT-5.6 Sol. Separately, [Wiz Research](https://www.wiz.io/blog/php2shell-php-rce) discovered and reported both vulnerabilities and used AI tools during its investigation.

The vulnerable code was not necessarily new. Some of the underlying problems had existed for years. The challenge was identifying unusual interactions inside complex software, reproducing them and determining their security impact.

AI helped with parts of that research. It did not independently repair PHP or replace the people responsible for the investigation. Researchers verified the findings, and PHP maintainers prepared and released the fixes with support from other organizations.

That is an important point. A useful AI finding still needs technical validation before anyone can rely on it.

## Were hackers already targeting websites?

[Cloudflare](https://blog.cloudflare.com/php-vulnerabilities-waf-protection) reported malicious traffic targeting the vulnerabilities and deployed web application firewall protections around the time of public disclosure. Other security providers also coordinated defensive measures.

This makes the incident urgent, but the wording matters. **Attack attempts are not the same as confirmed successful compromises.** It would be misleading to suggest that every PHP website, or most of the internet, had been hacked.

## What should website owners do?

If you use WordPress or another PHP-powered platform, ask your hosting provider whether the PHP runtime serving your website has received the necessary security fixes.

WordPress site owners can usually find the PHP version under **Tools > Site Health > Info > Server**. The [WordPress security notice](https://wordpress.org/news/2026/10/critical-php-security-release/) makes clear that this is a PHP runtime issue, not a vulnerability fixed merely by updating WordPress plugins or themes.

If you have a website but do not manage its server, asking your host for confirmation is a sensible first step.

## Three essential actions for developers and administrators

### 1. Audit every deployed PHP runtime

Identify the PHP version actually serving production traffic, including PHP-FPM pools, Apache `mod_php`, CGI environments and containers. Check vendor package advisories as well as version strings, since Linux distributions may provide security backports without changing to the latest upstream version number.

### 2. Apply patched releases, not temporary workarounds

The PHP team released the following security versions on 21 October:

| PHP branch | Patched release |
| --- | --- |
| 8.5 | **8.5.12** |
| 8.4 | **8.4.27** |
| 8.3 | **8.3.36** |
| 8.2 | **8.2.35** |

PHP 8.1 and older are outside the project's normal security-support window. If upgrading immediately is impractical, confirm whether your operating-system or long-term-support vendor supplies verified backported patches and plan a move to a supported runtime. Review the [official PHP advisory](https://www.php.net/archive/2026.php) for your environment.

A web application firewall can help reduce exposure, but it does not replace patching the underlying runtime.

### 3. Review logs, restrict exposure and follow new advisories

Review web-server, PHP and WAF logs for suspicious requests and unusual process behavior. Restrict unnecessary upload endpoints, enforce appropriate request limits and check for indicators of compromise when your monitoring identifies suspicious activity.

PHP also issued a follow-up informational advisory on **23 October** concerning a less common session-upload-progress configuration, associated with **CVE-2026-115560**. Administrators should review whether this configuration applies and follow PHP's recommendation to disable `session.upload_progress.enabled` where required pending a subsequent fix. Do not assume a previously installed patch addresses every later advisory.

## Does every website face this threat?

No. A site made of static HTML, CSS and JavaScript without a PHP runtime is not directly exposed to these particular PHP engine vulnerabilities.

Our Sanat Utility Studio website, for example, uses Jekyll and GitHub Pages to publish static pages rather than a PHP-powered website backend. That does not make a site immune to all security issues. Accounts, dependencies and deployment systems still need protection.

## What this means for the future of cybersecurity

AI can help security researchers study complicated software and find problems that might otherwise go unnoticed. That is promising for defenders. The concern is that similar capabilities may also make it easier for attackers to investigate weaknesses.

I work as a doctor, but software development has been a personal passion for years. Building applications and tools at Sanat Utility Studio has taught me that identifying a problem is only the beginning. A proposed fix must still be checked, tested and made reliable.

The PHP2Shell incident shows that principle at a much larger scale. AI-assisted research helped uncover dangerous flaws, but making websites safer still depended on researchers, maintainers, hosting providers and administrators working together.

**AI may help us discover vulnerabilities faster than ever. The real test is whether we can fix them before attackers exploit them.**

## Sources and further reading

1. [PHP Development Team: Security advisories and emergency releases](https://www.php.net/archive/2026.php)
2. [Wiz Research: PHP2Shell investigation](https://www.wiz.io/blog/php2shell-php-rce)
3. [OpenAI: Patch the Planet and coordinated disclosure](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)
4. [Cloudflare: PHP2Shell protections and observed activity](https://blog.cloudflare.com/php-vulnerabilities-waf-protection)
5. [WordPress: Critical PHP Security Release](https://wordpress.org/news/2026/10/critical-php-security-release/)
6. [W3Techs: PHP usage statistics](https://w3techs.com/technologies/details/pl-php)

### Editorial note

This report uses publicly available vendor advisories and security research reviewed on 24 October 2026. Sanat Utility Studio has not independently reproduced the vulnerabilities or verified individual server compromises. Illustrations are conceptual and are not screenshots of attacks or testing.