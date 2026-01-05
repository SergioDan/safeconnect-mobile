<p align="center">
  <img src="design/safeconnect-logo.jpg" width="180" alt="SafeConnect logo">
</p>

SafeConnect is a human-centered safety communication app designed to help people stay connected during emergency or high-stress situations.

It provides a fast, reliable, and low-friction way to notify trusted contacts, share real-time status, and initiate communication — especially when every second matters.

SafeConnect prioritizes simplicity, reliability, and emotional clarity over complex emergency workflows.

📌 Why SafeConnect?
SafeConnect was born from a very personal motivation:
Creating a simple and dependable way for loved ones to reach each other immediately during moments of fear, danger, or medical need.

Many existing safety solutions are:
Slow to operate in stressful moments
Overloaded with complex flows
Designed for systems, not people
Fragile under real-world conditions
SafeConnect focuses on:

- One-tap actions
- Minimal cognitive load
- Human-centered UX
- Cross-platform communication
- Fail-safe and retry mechanisms
- The goal is not just emergency escalation —
but human connection when it matters most.

🧩 Project Structure

/android      → Android app (Kotlin + Jetpack Compose)
/ios          → iOS app (SwiftUI – planned)
/backend      → FastAPI backend (Python)
/docs         → Architecture diagrams & documentation
/design       → Branding, UI flows, wireframes
/tests        → Unit & integration tests

Some folders may include .gitkeep files while features are still evolving.

🏗 Architecture Overview
SafeConnect follows Clean Architecture, ensuring scalability, testability, and long-term maintainability.
Domain Layer
Core business models
Use cases
Platform-agnostic rules
Data Layer
REST & WebSocket clients
Local persistence
Repository abstractions
Presentation Layer
Android: Jetpack Compose
iOS: SwiftUI
State management using MVI / MVVM
This separation allows each platform to evolve independently while sharing consistent business logic.

🛠 Tech Stack
Mobile
Kotlin + Jetpack Compose (Android)
SwiftUI (iOS – upcoming)
Coroutines & Flow
Clean Architecture
MVI / MVVM
Backend
Python + FastAPI
REST APIs
WebSocket support
Future services:
Alert orchestration
Real-time communication
Contact & device management

🚨 Core Features (MVP)
One-tap “I’m OK” / “Need to Talk” check-ins
Real-time timestamps
Trusted contact selection
Push-ready architecture
Fail-safe retry logic
Accessible UI for all ages

🧭 Roadmap (High Level)
Phase 1 — Core MVP
Android UI (Jetpack Compose)
Check-in workflow
Local persistence
Initial FastAPI backend
Logging & basic monitoring

Phase 2 — Communication Layer
WebSocket session prototype
Push notifications (FCM / APNs)
Device & contact linking

Phase 3 — AI-Assisted Safety
Voice / shout detection
Fall detection
Smart post-event summaries

Phase 4 — Family Dashboard
PWA dashboard
Alert history
Location & timeline playback

▶ Running the Backend (Development)
From the /backend directory:
Copy code
Bash
uvicorn main:app --reload
Backend structure and endpoints are actively evolving as part of the MVP.

🤝 Contributing
Contributions, feedback, and collaboration ideas are welcome.

Feel free to:
Open an issue
Propose improvements
Discuss architectural ideas

📄 License
MIT License
Free to use, modify, and contribute.
