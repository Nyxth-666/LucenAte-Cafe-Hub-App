# LucenAte ☕

### Discover Lucena. One Café at a Time.

**LucenAte** is a full-stack café and restaurant discovery platform dedicated to Lucena City, Quezon, Philippines.

The platform aims to centralize local cafés, coffee shops, restaurants, and other food establishments into one accessible hub. Its primary purpose is to help customers discover local establishments, particularly smaller businesses and hidden gems that may receive limited visibility through traditional search platforms.

LucenAte provides customers with a convenient way to explore local establishments while allowing business owners to manage their own business profiles and reach more potential customers.

---

## 📌 Project Overview

| Information | Details |
|---|---|
| Project Name | LucenAte |
| Project Type | Full-Stack Web Application |
| Service Area | Lucena City, Quezon, Philippines |
| Frontend | React.js + Vite |
| Styling | Tailwind CSS v4 |
| Backend | Python + Django |
| API | Django REST Framework |
| Database | PostgreSQL |
| Version Control | Git + GitHub |
| Architecture | React Frontend + Django REST API |

## 🎯 Project Objectives

- Centralize café and restaurant information within Lucena City.
- Help lesser-known establishments gain online visibility.
- Allow customers to discover establishments based on categories, location, ratings, and preferences.
- Provide business owners with tools to manage their establishments.
- Implement an administrative verification system to maintain reliable business information.
- Provide an interactive map and location-based discovery.
- Introduce a randomized discovery feature called **Surprise Me**.

## 👥 User Roles

### 1. Normal User
- Browse cafés and restaurants.
- Search and filter establishments.
- Explore categories and interactive maps.
- View business information, operating hours, and menus.
- Save favorite establishments.
- Write reviews and ratings.
- Check in and track visits.
- Receive notifications and recommendations.
- Use the Surprise Me feature.

### 2. Business Owner
- Register a business account.
- Submit business information and verification documents.
- Manage their own business profiles.
- Update locations and operating hours.
- Upload business photos.
- Manage menu categories and menu items.
- View and respond to customer reviews.
- Monitor business analytics and notifications.

### 3. Administrator
- Manage users and businesses.
- Review business registration applications.
- Approve, reject, or suspend businesses.
- Moderate reviews and reports.
- Manage categories and featured establishments.
- Monitor platform analytics.
- Manage notifications and administrative logs.

## ✨ Core Features

| Feature | Description |
|---|---|
| Search | Search businesses, menu items, categories, and locations. |
| Categories | Explore cafés, restaurants, desserts, fast food, and more. |
| Interactive Map | Discover establishments and view their locations. |
| Favorites | Save establishments for future visits. |
| Surprise Me | Randomly select an eligible establishment based on user filters. |
| Business Profiles | Display descriptions, photos, menus, ratings, and operating hours. |
| Reviews & Ratings | Allow registered users to rate and review establishments. |
| Business Management | Allow owners to manage their own establishments. |
| Verification | Require administrative review before businesses become verified. |
| Notifications | Notify users about relevant updates and activities. |
| Analytics | Track business views, searches, favorites, and other platform interactions. |
| Hidden Gems | Highlight lesser-known establishments with positive discovery signals. |

## 🛠️ Technology Stack

### Frontend
- React.js
- Vite
- JavaScript
- Tailwind CSS v4
- React Router
- Axios
- TanStack Query
- Lucide React

### Backend
- Python
- Django
- Django REST Framework
- Django Authentication
- SimpleJWT

### Database
- PostgreSQL

### Additional Technologies
- React Leaflet
- OpenStreetMap
- Recharts
- React Hook Form
- Zod
- Pillow

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Postman
- pgAdmin 4

## 🏗️ System Architecture

```text
             CLIENT
               |
               v
       REACT APPLICATION
       Vite + Tailwind CSS
               |
               v
          REST API
               |
               v
       DJANGO REST FRAMEWORK
               |
               v
        DJANGO BACKEND
               |
               v
          POSTGRESQL
```

The frontend communicates with the backend through REST API endpoints. Django handles authentication, permissions, validation, business logic, and database operations.

## 📂 Repository Structure

```text
LucenAte/
├── frontend/
├── backend/
├── database/
├── docs/
├── .github/
├── .gitignore
├── .editorconfig
└── README.md
```

## 🚀 Development Roadmap

### Phase 1 — Project Foundation
- Repository setup.
- Development environment configuration.
- React and Django initialization.
- PostgreSQL connection.
- Initial database design.
- API configuration.

### Phase 2 — Authentication & Authorization
- Custom User model.
- User registration and login.
- Business owner registration.
- Administrator account management.
- Role-based access control.
- Password reset and account security.

### Phase 3 — Business Management
- Business registration.
- Business profiles.
- Business categories.
- Business locations.
- Operating hours.
- Menu management.
- Business verification workflow.

### Phase 4 — Customer Discovery
- Homepage.
- Search functionality.
- Category filters.
- Business detail pages.
- Interactive map.
- Favorites.
- Surprise Me randomizer.

### Phase 5 — Engagement
- Reviews and ratings.
- Check-ins and visit history.
- Notifications.
- Recommendations.
- Hidden Gems discovery.

### Phase 6 — Dashboards & Analytics
- User dashboard.
- Business owner dashboard.
- Administrator dashboard.
- Business statistics.
- Platform analytics.
- Review and report moderation.

### Phase 7 — Testing & Deployment
- Frontend and backend testing.
- API testing.
- Security validation.
- Responsive design.
- Performance optimization.
- Production deployment.
- Custom domain configuration.

## 🔐 Security & Development Guidelines

- Use environment variables for sensitive configuration.
- Never commit `.env` files, credentials, API secrets, or database passwords.
- Use Django's password hashing and authentication mechanisms.
- Enforce role-based permissions on the backend.
- Business owners may only manage businesses associated with their accounts.
- Only approved businesses receive the verified badge.
- Validate all submitted information and uploaded files.
- Do not expose sensitive information through public API endpoints.
- Use pull requests for code integration.
- Do not push directly to the production branch.

## 📊 Development Principles

- Maintain a modular and understandable codebase.
- Use reusable React components.
- Keep frontend and backend responsibilities separate.
- Use PostgreSQL as the production data source.
- Avoid hardcoded production business listings.
- Do not use fabricated analytics or authentication.
- Ensure important interface controls perform actual operations.
- Maintain responsive layouts for desktop, tablet, and mobile.
- Document API endpoints and significant architectural decisions.

## 🌱 Project Vision

LucenAte aims to become a centralized discovery platform for local cafés and restaurants in Lucena City, helping customers discover new places while giving smaller establishments an opportunity to grow their visibility and customer reach.

**Discover Lucena. One Café at a Time.**

---

*LucenAte — Full-Stack Development Project*