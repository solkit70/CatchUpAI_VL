# Product Requirements Document: Catch Up AI 2026 Homepage

> **[← Korean Version](catchupai-2026-prd-v2.md)**

**Project Name:** Catch Up AI 2026 Homepage
**Date:** 2026-02-15
**Version:** 1.0
**Based on:** BRD v1.0

---

## 1. Product Overview

### 1.1. Product Vision
The Catch Up AI 2026 homepage serves as an information hub that systematically introduces the core content and activities of Catch Up AI, an AI learning and research channel. The goal is to help visitors easily understand the channel's key projects and methodologies, provide accessible content for both developers and non-developers interested in AI, organize YouTube channel content by topic, and strengthen connections with the Seattle-area AI community.

### 1.2. Product Goals
- Systematically introduce Catch Up AI's 5 core projects (Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, Seattle AI Ecosystem) so visitors can clearly understand them.
- Provide a structure for easy topic-based navigation of YouTube channel content, increasing content accessibility.
- Strengthen connections with the Seattle-area AI community and encourage participation in community activities (cohorts, events).
- Build a professional and trustworthy image for Catch Up AI in AI learning and research, raising awareness and laying the foundation for potential partnerships and sustainable growth.

### 1.3. Target Audience
- **Developers and non-developers interested in AI**: Users who want to learn about Catch Up AI's 5 core projects and consume related YouTube content.
- **Seattle-area AI community members**: Users who want to check the latest event information in the "Seattle AI Ecosystem" section and participate in community activities.
- **Learners interested in Vibe Coding/Learning methodology**: Users who want to see an overview and applied examples of the methodology and subscribe to the YouTube channel for continuous learning.

### 1.4. Key Success Criteria
- Core project detail page visit rate: 60%+ of all visitors
- YouTube channel subscription conversion rate: increase in subscription clicks via the homepage
- Average website session time: 3 minutes or more
- AI4PKM Cohort application conversion rate: 10% increase year-over-year
- Newsletter subscriptions and social media shares: 50+ per month

---

## 2. Technical Architecture

### 2.1. System Architecture
This project is a static website built with pure HTML, CSS, and JavaScript with no backend. Content is managed by the Product Owner (PO) directly modifying HTML files using AI coding tools, hosted on Amazon S3. External services such as YouTube playlist embeds, Google Forms integration, and GitHub-based comments (Utterances) are integrated directly on the client side. User behavior data is collected via GA4, with consideration for transitioning to JSON-based dynamic loading as content grows.

### 2.2. Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| Frontend | HTML5 | Web standard markup, optimized for AI coding tools and easy PO editing |
| Frontend | CSS3 | Web standard stylesheet, optimized for AI coding tools and easy PO editing; CSS variable-based design system |
| Frontend | JavaScript (Pure) | Client-side logic (multilingual switching, event handling, dynamic rendering); optimized for AI coding tools |
| Hosting | Amazon S3 | Static website hosting, leverages existing infrastructure, cost-efficient, high availability |
| Analytics | Google Analytics 4 (GA4) | Website traffic and user behavior analysis; measures BRD success metrics |
| Forms/Data Collect | Google Forms | AI4PKM cohort applications, newsletter subscriptions, inquiries/feedback; free service |
| Data Storage (Forms) | Google Sheets | Stores and manages Google Forms submission data |
| Comments | Utterances (GitHub) | Embeds GitHub-based comment system; serverless and free; developer-friendly |
| Video Content | YouTube Embed | Directly embeds YouTube channel videos and playlists; auto-reflects latest videos |
| Version Control | Git | Code version control and collaboration; S3 deployment automation (for future CI/CD) |

### 2.3. Component Breakdown
- **Main Page (index.html)**: Catch Up AI intro, 5 core project overview and links, latest/recommended YouTube videos, newsletter subscription CTA, social media links.
- **Project Detail Pages (5 pages)**: For each project (Vibe Coding, Vibe Learning, Vibe Guiding, AI4PKM, Seattle AI Ecosystem): goals, content, how it works, related YouTube playlist embed, recommended videos, community activity CTA.
- **AI4PKM Cohort Application Page**: Cohort introduction, Google Forms-integrated application feature.
- **Seattle AI Ecosystem Page**: Seattle AI community introduction, AI-related event information, related resource links.
- **Newsletter Subscription Section/Page**: Newsletter subscription form (Google Forms integration).
- **Multilingual Toggle Button**: Korean/English language switch button.
- **Global Components**: Header (navigation), footer (social media links, copyright), CSS (design system definitions), JavaScript (common functions).

### 2.4. Integration Points
- **YouTube**: Content integration via video and playlist embedding.
- **Google Forms**: AI4PKM cohort applications, newsletter subscriptions, inquiries/feedback.
- **Google Sheets**: Stores data collected via Google Forms.
- **Google Analytics 4 (GA4)**: Collects website traffic and user behavior data.
- **GitHub (Utterances)**: Comments feature integration.

---

## 3. User Stories & Use Cases

### 3.1. User Personas
- **AI Learners (Developers/Non-developers)**: Interested in Catch Up AI's various AI learning methodologies and projects; want to systematically explore YouTube channel content.
- **Seattle-area AI Community Members**: Interested in AI-related events in Seattle; want to participate in local community activities.
- **Potential Collaboration Partners/Sponsors**: Want to understand Catch Up AI's vision and expertise to explore collaboration possibilities.

### 3.2. User Stories
- As an AI learner, I want to easily find information about Catch Up AI's 5 core projects so that I can understand their value and choose what to explore further. (P0, Effort: Small)
- As a new visitor, I want to see a clear overview of Catch Up AI's methodology (Vibe Coding → Vibe Learning → Vibe Guiding) so that I can understand its logical progression. (P0, Effort: Small)
- As a YouTube subscriber, I want to find the latest videos related to a specific project on the website so that I don't miss new content. (P0, Effort: Medium)
- As a Seattle AI community member, I want to quickly find upcoming AI events so that I can plan my participation. (P0, Effort: Small)
- As a potential cohort participant, I want to easily apply for the AI4PKM cohort so that I can join the learning program. (P0, Effort: Small)
- As an interested user, I want to subscribe to the newsletter so that I can receive updates from Catch Up AI. (P0, Effort: Small)
- As a global user, I want to switch between Korean and English content so that I can consume information in my preferred language. (P0, Effort: Medium)
- As a mobile user, I want the website to be easy to navigate and read on my smartphone so that I can access information on the go. (P0, Effort: Medium)

### 3.3. Use Case Scenarios
1. **Visiting the Homepage and Exploring Core Content**:
   - User accesses the homepage via YouTube channel, social media, or search.
   - Views the Catch Up AI introduction and 5 core project overviews on the main page.
   - Clicks on a project of interest to navigate to its detail page.
2. **Exploring Project Details and Consuming YouTube Content**:
   - On the project detail page, views the project's goals, methodology, and related YouTube playlist (embedded).
   - Watches the embedded YouTube video or navigates to the related YouTube playlist to watch more.
3. **Participating in Community Activities**:
   - On the AI4PKM cohort detail page, clicks "Apply" to navigate to Google Forms, fills out and submits the application.
   - Checks the latest AI event information on the Seattle AI Ecosystem page.
   - Enters email in the newsletter subscription section and completes subscription.
4. **Language Switching**:
   - Clicks the language toggle button at the top of the page to switch to the Korean or English version.
5. **Mobile Access**:
   - Accesses the website on a smartphone or tablet and experiences an optimized layout.

---

## 4. Feature Requirements

### 4.1. Core Features

| Feature | Description | Priority | Dependencies | Acceptance Criteria |
|---------|-------------|----------|--------------|---------------------|
| **Main Page** | Catch Up AI intro, 5 core project overview and links, latest/recommended YouTube videos, newsletter CTA, social links | Must Have | — | Core message clearly conveyed; easy navigation to 5 projects; video thumbnails link correctly; newsletter CTA visible; social links provided |
| **Project Detail Pages** | Detailed description of each of 5 projects, related YouTube playlist embed, 3–5 recommended videos, community activity CTA | Must Have | YouTube Embed | Each project clearly described; playlist embedded with latest videos auto-reflected; 3–5 PO-selected recommended videos shown; community CTA provided |
| **AI4PKM Cohort Application** | Cohort intro and participation guide, application feature via Google Forms | Must Have | Google Forms | Detailed cohort info provided; "Apply" button links to Google Forms; thank-you message shown after submission |
| **Seattle AI Ecosystem Page** | Seattle AI community intro and Catch Up AI's role, AI event info (manual updates), related external links | Must Have | — | Community and Catch Up AI's role introduced; latest events shown; external links provided |
| **Newsletter Subscription** | Newsletter subscription form (Google Forms integration) | Must Have | Google Forms | Subscription form (email input) provided; data collected via Google Forms; confirmation shown after subscription |
| **Multilingual Support (KR/EN)** | KR/EN toggle button, all content provided in both languages (separate HTML files) | Must Have | — | Language toggle clearly shown at top; redirect to correct language on click; all core content available in both languages |
| **Responsive Design** | Optimized layout and functionality on desktop, tablet, and mobile | Must Have | — | All pages adapt fluidly to all screen sizes; navigation and readability ensured on mobile |
| **Comments Feature** | GitHub-based Utterances widget embed | Should Have | GitHub (Utterances) | Comment section shown at bottom of each project page; GitHub login to write/view comments |
| **GA4 Integration** | Google Analytics 4 integration for traffic and user behavior tracking | Must Have | GA4 | GA4 tracking code on all pages; key user behavior data collected; custom events for BRD success metrics configured |

### 4.2. Feature Specifications

- **Multilingual Support (separate HTML files)**:
  - Default language is English; Korean lives in a separate `/ko/` folder as static HTML files.
  - Example: English main page `index.html`, Korean main page `/ko/index.html`.
  - Language toggle button at the top of each page; clicking uses JavaScript to redirect to the correct language HTML file.
  - Given the modest content volume, this approach is adopted initially. Future migration to JSON-based dynamic loading will use separate language JSON files.

- **YouTube Content Integration**:
  - **Playlist Embed**: Each project detail page embeds the corresponding YouTube playlist via `<iframe>`. New videos added to the playlist are automatically reflected.
  - **Recommended Videos Section**: PO selects 3–5 key videos per project, embedded individually via `<iframe>`.
  - **YouTube API**: Not used in the initial MVP. If dynamic features (e.g., auto-loading latest videos) are needed in the future, YouTube Data API v3 will be considered within the free daily quota (10,000 units).

- **Content Management (PO Direct Editing)**:
  - PO directly modifies HTML files using AI coding tools (Claude Code, Cursor, etc.).
  - Content areas are clearly delineated with comments (`<!-- CONTENT START/END -->`) so the PO can easily identify and edit them.
  - Version control via Git; preview changes locally before committing.

- **GA4 Event Tracking**:
  - YouTube channel subscribe button clicks, YouTube video/playlist link clicks → log `youtube_subscribe_click`, `video_click`, etc. via `gtag()`.
  - AI4PKM cohort apply button, newsletter subscribe button clicks → log `cohort_apply_click`, `newsletter_subscribe_click`, etc.

### 4.3. User Interface Requirements

- **Consistent Design System**: Provide a consistent UX/UI reflecting Catch Up AI's brand identity.
  - Use CSS variables (Custom Properties) to manage design tokens (colors, fonts, spacing) centrally.
  - Define all design tokens in `/css/variables.css`; all CSS files reference these variables.
  - When using AI coding tools, explicitly instruct prompts to use existing CSS variables and classes for consistency.
  - When PO modifies UI code, provide guidelines to only change within defined CSS variable scope (no new inline styles or class additions).
- **Responsive Design**: Apply a mobile-first approach for an optimized user experience across all devices. Use viewport meta tags to ensure responsive behavior.
- **Wireframes/UI Flow**: Define the primary section layout and navigation flow for each page (main, project detail, cohort, ecosystem). Provide concise and intuitive navigation so users can find information with minimal clicks.

---

## 5. API Specifications

*(Static website with no direct external API calls — this section uses brief integration descriptions)*

### 5.1. API Endpoints
- **YouTube Embed**: YouTube videos and playlists embedded directly via `<iframe>` tag. No specific API endpoint calls.
- **Google Forms**: Integration via Google Forms-provided `<iframe>` embed code or link for application/subscription forms.
- **Utterances**: Comments feature embedded via the Utterances widget `script` tag.

### 5.2. Authentication & Authorization
- The website itself has no user authentication or authorization.
- Google Forms follows Google's authentication and authorization model.
- Utterances follows GitHub's authentication model.

### 5.3. Error Handling
- If external services (YouTube, Google Forms) fail, display a user-friendly fallback message or inform the user the feature is temporarily unavailable.
- Example: "Unable to load video" message on YouTube load failure.
- No server-side error handling (static website).

---

## 6. Data Models

### 6.1. Database Schema
This project uses no database. All content is stored in HTML files or JSON files (for future migration).

### 6.2. Data Flow
1. **User Accesses Website**: User visits the Catch Up AI homepage URL via a web browser.
2. **S3 Content Loading**: Static HTML, CSS, and JavaScript files hosted on Amazon S3 are delivered to the user's browser.
3. **YouTube Content Loading**: Browser loads video/playlist content directly from YouTube servers via `<iframe>` tags in the HTML.
4. **Google Forms Integration**: When a user submits an application/subscription form, data is sent directly from the browser to Google Forms servers and stored in Google Sheets.
5. **Utterances Comments Integration**: When a user writes a comment, the browser sends comment data directly to the GitHub API via the Utterances widget, stored in GitHub Issues.
6. **GA4 Data Transmission**: User behavior data (page views, event clicks, etc.) is sent directly from the browser to Google Analytics 4 servers.

### 6.3. Data Validation Rules
- **Google Forms**: Uses Google Forms' built-in input validation (required fields, email format, etc.).
- **Client-side Validation**: HTML5 `required` attribute and simple JavaScript for basic client-side validation before form submission.

---

## 7. Security & Compliance

### 7.1. Security Requirements
- **HTTPS**: All website traffic must be encrypted via HTTPS. (Amazon S3 + CloudFront or S3 native HTTPS configuration)
- **Data Protection**: Personal information (name, email, etc.) collected via Google Forms follows Google's security policies; the Catch Up AI website itself does not directly store sensitive personal information.
- **Malicious Code Prevention**: Static website is relatively safe from server-side attacks; consider appropriate sanitizing for user input fields to prevent XSS (when using external services like Utterances, rely on their security policies).
- **Git Security**: Git repository maintains code integrity through proper access controls (private repository).

### 7.2. Privacy & Compliance
- **Privacy Policy**: Provide a brief privacy notice at the bottom of the website (collection purpose, retention period, deletion request process).
- **GDPR/CCPA**: Direct regulatory compliance burden is low since the website itself does not store personally identifiable information; follows the privacy policies of Google Forms and GA4 when used.
- **Cookie Consent**: Since GA4 is used, a banner or popup for cookie consent can be implemented on initial load (optional).

### 7.3. Security Testing Requirements
- **Regular Code Reviews**: Regularly review code to prevent potential vulnerabilities (e.g., script injection) from the PO's direct HTML editing approach.
- **External Service Security**: Monitor the security policies and updates of integrated external services (Google Forms, YouTube, Utterances, etc.).

---

## 8. Performance Requirements

### 8.1. Performance Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Page Load Time (LCP) | Within 2 seconds | Google Lighthouse, PageSpeed Insights |
| Response Time (FID) | Within 100ms | Google Lighthouse, PageSpeed Insights |
| Concurrent Users | Up to 10,000/month | GA4 traffic monitoring, S3/CloudFront metrics |
| CLS (Cumulative Layout Shift) | 0.1 or less | Google Lighthouse, PageSpeed Insights |

### 8.2. Scalability Requirements
- **Traffic Growth**: Initial S3 hosting alone is sufficient; if traffic spikes, add Amazon CloudFront CDN for geo-distributed caching.
- **Content Growth**: If content volume increases, consider transitioning to JSON-based dynamic loading. PO only needs to modify JSON files, reducing the burden of direct HTML editing.
- **Multilingual Support**: Korean/English multilingual support implemented from the start for a globally scalable structure. (Separate HTML files → future transition to JSON-based multilingual files)

### 8.3. Optimization Strategies
- **Image Optimization**: All images optimized in web-friendly formats (WebP, etc.) and sizes. `loading="lazy"` attribute on `<img>` tags for lazy loading.
- **CSS and JS Minification**: All CSS and JavaScript files minified before deployment to reduce file sizes.
- **Browser Caching**: Set browser caching policies via HTTP headers to improve load speed on return visits.
- **CDN Usage**: (Future as needed) Introduce CloudFront or similar CDN to improve static content delivery speed.

---

## 9. Testing & Quality Assurance

### 9.1. Testing Strategy
- **Manual Testing**: Functional testing of all pages (link functionality, form submission, language switching, etc.) and UI/UX testing (design consistency, responsive verification) performed manually.
- **Cross-browser Testing**: Verify website renders and functions correctly in major browsers (Chrome, Firefox, Safari, Edge) and on mobile devices.
- **Performance Testing**: Periodically measure and improve webpage performance metrics using Google Lighthouse and PageSpeed Insights.
- **Accessibility Testing**: Use manual inspection and automated tools (e.g., axe DevTools) to comply with WCAG 2.1 AA guidelines.

### 9.2. Acceptance Criteria
- All core features (main page, project detail, application form, language switching, etc.) work as specified in BRD and PRD.
- All pages load within 2 seconds.
- Consistent and optimized UI/UX on desktop, tablet, and mobile.
- Data for measuring key success metrics is correctly collected via GA4.
- Google Forms integration works correctly and data is properly stored in Google Sheets.
- PO can update content using AI coding tools per the content management guidelines.

### 9.3. Quality Metrics
- Google Lighthouse Score: Performance 80+, Accessibility 90+, Best Practices 90+, SEO 90+.
- Bug density: 0 Critical/High bugs before launch.
- Code consistency: 90%+ adherence to CSS variable and BEM-like naming conventions.

---

## 10. Deployment & DevOps

### 10.1. Deployment Strategy
- **Manual Deployment (Initial)**: PO directly uploads HTML, CSS, and JavaScript files committed to the Git repository to the Amazon S3 bucket.
- **Git-based Deployment (Future)**: Consider introducing a simple CI/CD pipeline (e.g., GitHub Actions, AWS CodePipeline) for automatic sync to S3 on git push.
- **Environments**: Production only; development and testing done in local environment.

### 10.2. Monitoring & Logging
- **GA4 Monitoring**: Monitor real-time traffic, user behavior, and error occurrence (e.g., 404 pages) via Google Analytics 4.
- **S3 Access Logs**: Enable Amazon S3 access logs to analyze website access patterns and potential issues.
- **Error Tracking**: Client-side JavaScript errors can be tracked using GA4's error tracking feature or by integrating a lightweight error tracking tool like Sentry (optional).

### 10.3. Rollback Procedures
- All code changes are version-controlled via Git; if issues arise, roll back to a previous Git commit and redeploy to S3.
- Use Amazon S3's versioning feature for easy recovery to previous object versions.

---

## 11. Timeline & Milestones

| Phase | Deliverables | Timeline | Dependencies |
|-------|-------------|----------|--------------|
| **Phase 1: Planning & Design** | BRD/PRD approved, initial design guidelines, core tech stack confirmed | 2026-02-15 ~ 2026-02-29 | BRD |
| **Phase 2: MVP Development (Core Features)** | Main page, 5 project detail pages (English), multilingual toggle (HTML-based), AI4PKM application, newsletter subscription, GA4 integration | 2026-03-01 ~ 2026-04-30 | — |
| **Phase 3: MVP Deployment & Testing** | S3 deployment, functional testing, responsive testing, performance optimization, security review | 2026-05-01 ~ 2026-05-15 | Phase 2 complete |
| **Phase 4: Korean Content Addition** | Create and apply Korean versions of all MVP pages | 2026-05-16 ~ 2026-06-30 | Phase 3 complete |
| **Phase 5: Additional Features & Enhancement** | Seattle AI Ecosystem page, comments (Utterances), JSON-based dynamic loading transition (if needed), YouTube API integration (if needed) | 2026-07-01 ~ 2026-09-30 | Phase 4 complete |

---

## 12. Assumptions & Constraints

### 12.1. Technical Assumptions
- PO has the basic technical capability to directly modify HTML files using AI coding tools and deploy via Git.
- External free services (Google Forms, Google Sheets, YouTube Embed, etc.) will operate reliably.
- Complex dynamic content or user interaction features will not be needed initially.
- No separate CMS solution will be introduced for content management.
- Amazon S3 static website hosting costs will be minimal and can be operated free or cheaply within the expected traffic range.

### 12.2. Resource Constraints
- **Budget**: This is a personal project with almost no budget; minimize use of paid services and prioritize free or low-cost solutions.
- **Development Staff**: Product Owner leads development and content management using AI coding tools.

### 12.3. External Dependencies
- **YouTube**: Provides and embeds YouTube channel content (videos, playlists).
- **Google Forms**: Provides AI4PKM cohort application and newsletter subscription functionality.
- **Google Sheets**: Stores data collected via Google Forms.
- **Amazon S3**: Provides website hosting infrastructure.
- **Google Analytics 4 (GA4)**: Analyzes website traffic and user behavior.
- **GitHub (Utterances)**: Provides comments feature.
