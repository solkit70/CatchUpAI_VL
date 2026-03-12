# Business Requirements Document: Catch Up AI 2026 Homepage

> **[← Korean Version](catchupai-2026-brd-v3.md)**

**Project Name:** Catch Up AI 2026 Homepage
**Date:** 2026-02-15
**Version:** 1.0

---

## 1. Introduction

This document describes the business requirements for the Catch Up AI 2026 homepage construction project. The new homepage serves as an information hub that systematically introduces the core content and activities of Catch Up AI — a YouTube-centric AI learning and research channel. The goal is to help visitors easily understand the channel's key projects and methodologies and to strengthen connections with the AI community.

---

## 2. Stakeholder & User Analysis

### 2.1. RACI Matrix

| Role | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|------|-----------------|-----------------|---------------|--------------|
| Product Owner | R | A | C | I |
| Development Team Lead | R | A | C | I |
| UI/UX Designer | | | R | I |
| Marketing Lead | | | C | I |
| Content Creators | R | | | I |

### 2.2. Target Users
- **Developers and non-developers interested in AI**: People interested in new AI learning methodologies who want to quickly grasp Catch Up AI's 5 core projects, understand their value, and navigate to related YouTube playlists or detail pages.
- **Seattle-area AI community members**: Users who check the latest event information in the "Seattle AI Ecosystem" section and want to apply for community activities such as the AI4PKM cohort.
- **Learners interested in Vibe Coding/Learning methodology**: Users who want to understand the methodology overview, see real application examples, and subscribe to the YouTube channel for continuous learning.

### 2.3. User Journey Map
1. **Homepage Visit**: User arrives via the Catch Up AI YouTube channel, social media, or search.
2. **Explore Core Content**: Views an overview of the 5 core projects (Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, Seattle AI Ecosystem) on the main page.
3. **Explore a Project in Depth**: Clicks on a project of interest and navigates to its detail page to review goals, methodology, and related YouTube videos (embedded).
4. **Consume Related Content**: Watches embedded YouTube videos or navigates to related YouTube playlists to watch more.
5. **Community Participation**: Joins the Catch Up AI community via AI4PKM cohort application (Google Forms), Seattle AI event info, or newsletter subscription.
6. **Ongoing Connection**: Maintains connection with Catch Up AI through YouTube channel subscription and social media follows.

---

## 3. Business Objectives

### 3.1. Primary Objectives
- Systematically introduce Catch Up AI's 5 core projects (Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, Seattle AI Ecosystem) so visitors can clearly understand them.
- Provide a structure for easy topic-based navigation of YouTube channel content, increasing content accessibility.
- Strengthen connections with the Seattle-area AI community and encourage participation in community activities (cohorts, events).
- Build a professional and trustworthy image for Catch Up AI in AI learning and research, raising awareness and laying the foundation for potential partnerships and sustainable growth.

### 3.2. Success Metrics

| KPI | Target | Measurement Method |
|-----|--------|--------------------|
| Core project detail page visit rate | 60%+ of all visitors | GA4 event tracking |
| YouTube channel subscription conversion rate | Increase in subscription clicks via homepage | GA4 custom event tracking (YouTube link clicks) |
| Average website session time | 3 minutes or more | GA4 measurement |
| AI4PKM Cohort application conversion rate | 10% increase year-over-year | Google Forms submissions + GA4 event tracking |
| Newsletter subscriptions & social media shares | 50+ per month | Mailchimp / GA4 event tracking |

### 3.3. Business Value
- **Content Organization**: Structure scattered YouTube content to improve user experience and clearly communicate the value of core methodologies.
- **Community Activation**: Provide a two-way communication channel with the local AI community to increase participation and expand Catch Up AI's influence.
- **Brand Awareness & Expertise**: Increase Catch Up AI's credibility through a professional website and establish leadership in AI learning methodology research.
- **Foundation for Sustainable Growth**: Attract potential partners and cohort participants to secure long-term business growth drivers.

---

## 4. Technical Context

### 4.1. System Architecture Overview
This project is a static website built with HTML, CSS, and JavaScript only — no backend. Content is managed by the Product Owner directly modifying HTML files using AI coding tools, hosted on Amazon S3. External services such as YouTube playlist embeds and Google Forms integration are connected directly on the client side.

### 4.2. Technical Constraints
- **Static Website**: Serverless architecture — no backend development or operating costs.
- **Hosting**: Uses existing Amazon S3 static website hosting.
- **Budget Constraints**: Minimize use of paid services and maintain a simple tech stack.
- **Development Approach**: Development via Vibe Coding using AI coding tools.
- **No Database**: Content updates through direct HTML file modification — no dynamic content management system (CMS).
- **YouTube API Usage Limit**: Use only within the YouTube Data API v3 free daily quota (10,000 units).

### 4.3. Scalability Requirements
- **Traffic Growth**: Initial S3 hosting alone is sufficient; if traffic spikes, Amazon CloudFront CDN can be added for performance.
- **Content Growth**: If content volume increases, consider transitioning to JSON-based dynamic loading for scalability. PO only modifies JSON files, reducing the burden of direct HTML editing.
- **Multilingual Support**: Korean/English multilingual support implemented from the start for a globally scalable structure.

---

## 5. Functional Requirements

### 5.1. Core Features
- **Main Page**:
  - Catch Up AI introduction and core message (Priority: Must Have)
  - Overview of 5 core projects (Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, Seattle AI Ecosystem) with links to each project detail page (Priority: Must Have)
  - Latest or recommended YouTube video thumbnails and links (Priority: Must Have)
  - Newsletter subscription CTA (Priority: Must Have)
  - Social media links (YouTube, LinkedIn, etc.) (Priority: Must Have)
- **Project Detail Pages (1 per each of 5 projects)**:
  - Detailed description of each project's goals, key content, and how it works (Priority: Must Have)
  - Related YouTube playlist embed (auto-reflects latest videos) (Priority: Must Have)
  - 3–5 PO-curated "recommended videos" (Priority: Should Have)
  - Visualization of each project's features and value (Priority: Should Have)
  - Community activity CTA (e.g., AI4PKM cohort application) (Priority: Must Have)
- **AI4PKM Cohort Application Page**:
  - Cohort introduction and participation guide (Priority: Must Have)
  - Application feature via Google Forms integration (Priority: Must Have)
- **Seattle AI Ecosystem Page**:
  - Introduction of the Seattle AI community and Catch Up AI's role (Priority: Must Have)
  - Seattle AI-related event information (manual update) (Priority: Must Have)
  - Related external community and resource links (Priority: Should Have)
- **Newsletter Subscription Page/Section**:
  - Newsletter subscription form (Google Forms integration) (Priority: Must Have)
  - Newsletter sample preview feature (Priority: Nice to Have)
- **Multilingual Support**:
  - Korean/English toggle button (page-to-page switching) (Priority: Must Have)
  - All content available in both Korean and English versions (Priority: Must Have)
- **Responsive Design**:
  - Optimized layout and functionality on desktop, tablet, and mobile (Priority: Must Have)

### 5.2. User Stories
- **Content Exploration**:
  - As an AI learner, I want to easily find information about Catch Up AI's 5 core projects so that I can understand their value and choose what to explore further.
  - As a new visitor, I want to see a clear overview of Catch Up AI's methodology (Vibe Coding → Vibe Learning → Vibe Guiding) so that I can understand its logical progression.
  - As a YouTube subscriber, I want to find the latest videos related to a specific project on the website so that I don't miss new content.
- **Community Participation**:
  - As a Seattle AI community member, I want to quickly find upcoming AI events so that I can plan my participation.
  - As a potential cohort participant, I want to easily apply for the AI4PKM cohort so that I can join the learning program.
  - As an interested user, I want to subscribe to the newsletter so that I can receive updates from Catch Up AI.
- **Site Experience**:
  - As a global user, I want to switch between Korean and English content so that I can consume information in my preferred language.
  - As a mobile user, I want the website to be easy to navigate and read on my smartphone so that I can access information on the go.

---

## 6. Non-Functional Requirements

### 6.1. Performance
- **Page Load Time**: All pages must load within 3 seconds. (Target: within 2 seconds)
- **Response Time**: Response time to UI element clicks or interactions must be within 1 second.
- **Concurrent Users**: Must reliably handle up to 10,000 concurrent users per month.

### 6.2. Security
- **HTTPS**: All traffic must be encrypted via HTTPS.
- **Data Protection**: Personal information (name, email, etc.) collected via Google Forms follows Google's security policies; the Catch Up AI website itself does not directly store sensitive personal information.
- **Malicious Code Prevention**: Regular security reviews to prevent malicious code injection or distribution on the website.

### 6.3. Usability
- **Intuitive Navigation**: Provide a clear and consistent navigation structure so users can find the information they need with minimal clicks.
- **Accessibility**: Strive to comply with Web Content Accessibility Guidelines (WCAG) 2.1 AA to make the site accessible to diverse users.
- **Consistent UX/UI**: Apply a consistent design system reflecting Catch Up AI's brand identity to communicate professionalism and trustworthiness.

### 6.4. Reliability
- **Availability**: Website must maintain 99.9% uptime year-round.
- **Backup & Recovery**: Static files hosted on S3 follow S3's built-in resilience; version-controlled via Git for recovery to previous versions if needed.
- **Error Handling**: Provide user-friendly error messages so users can understand the situation when issues arise.

---

## 7. Constraints & Assumptions

### 7.1. Budget Constraints
- This is a personal project with almost no budget; minimize use of paid services and prioritize free or low-cost solutions.
- Development and maintenance costs must be minimized.

### 7.2. Timeline
- MVP (Minimum Viable Product) targets completion within Q3 2026.
- Full feature implementation and enhancement proceeds incrementally through Q4 2026.

### 7.3. Assumptions
- Product Owner has the basic technical capability to directly modify HTML files using AI coding tools and deploy via Git.
- External free services (Google Forms, Google Sheets, YouTube Embed, etc.) will operate reliably.
- Complex dynamic content or user interaction features will not be needed initially.
- No separate CMS solution will be introduced for content management.

---

## 8. Risk Analysis

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| PO errors from direct HTML editing | High | Medium | Provide clear content guidelines; separate content areas; thorough local preview; use Git version control and rollback; consider simple code validation tools |
| External service outage (YouTube, Google Forms) | Medium | Low | Minimize dependencies on external services for core features; show fallback or informational messages on failure |
| Content update delays and consistency degradation | Medium | Medium | Template-based page structure; strengthen AI tool usage guidelines; regular content reviews |
| Performance degradation from traffic spikes | Low | Low | Plan CloudFront CDN after initial S3 hosting; design a scalable structure with JSON-based dynamic loading |
| Security vulnerabilities (static website) | Low | Low | Apply HTTPS; don't store sensitive info on the website; regular security reviews (as needed) |

---

## 9. Dependencies
- **YouTube**: Provides and embeds YouTube channel content (videos, playlists).
- **Google Forms**: Provides AI4PKM cohort application and newsletter subscription functionality.
- **Google Sheets**: Stores data collected via Google Forms.
- **Amazon S3**: Provides website hosting infrastructure.
- **Google Analytics 4 (GA4)**: Analyzes website traffic and user behavior.

---

## 10. Approval

All requirements specified in this document serve as important criteria for the successful completion of the Catch Up AI homepage project.

**Product Owner:** ______________________________ (Signature)
**Development Team Lead:** ______________________________ (Signature)
**Date:** 2026-02-15
