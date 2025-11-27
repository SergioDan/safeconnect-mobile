# SafeConnect – Family Safety & Check-ins (Android & iOS)

SafeConnect is a cross-platform mobile app (Android + iOS) that helps families and close friends stay connected through quick safety check-ins.

The goal of this project is to showcase modern mobile development on both platforms with clean architecture, offline-first design, and a clear path to backend/IoT integration.

---

## Features (MVP)

- 👥 **Trusted contacts**
  - Add, edit and remove trusted contacts (name, relationship, phone number).

- ✅ **Quick safety check-ins**
  - One-tap “I'm OK” check-in stored locally with timestamp.
  - “Need to talk” action that opens the device dialer or preferred messaging app (no backend required).

- 🕒 **Local history**
  - Simple timeline of recent check-ins stored on the device.

- 🌗 **Modern UI**
  - Clean, minimal UI with support for light/dark mode.
  - Uses modern UI frameworks on both platforms (Jetpack Compose & SwiftUI).

- 🧱 **Clean architecture**
  - Clear separation of layers (UI, domain, data).
  - Ready to plug in a backend API (e.g. Python/FastAPI) in a future iteration.

---

## Tech Stack

### Android

- **Language:** Kotlin
- **UI:** Jetpack Compose
- **Architecture:** MVVM + Clean Architecture
- **Async:** Coroutines & Flow
- **Persistence:** Room (or DataStore for simple preferences)
- **Build tools:** Gradle, Android Studio

### iOS

- **Language:** Swift
- **UI:** SwiftUI
- **Architecture:** MVVM
- **Async:** Combine (or async/await for newer APIs)
- **Persistence:** UserDefaults for the MVP (CoreData planned)
- **Build tools:** Xcode

---

## Project Structure

```text
safeconnect-mobile/
 ├── android/           # Android app (Kotlin, Jetpack Compose)
 ├── ios/               # iOS app (Swift, SwiftUI)
 └── docs/              # Architecture diagrams, UI mockups, notes

 Each platform app is independent, but both implement the same core use case: trusted contacts + safety check-ins + local history.


---

Roadmap

[x] Android MVP: contacts, check-ins and local history

[x] iOS MVP: contacts, check-ins and local history

[ ] Shared design system documentation in /docs

[ ] Backend API (Python/FastAPI) to sync check-ins across devices

[ ] Push notifications for missed check-ins

[ ] Optional integration with wearables / IoT devices



---

Screenshots

> Coming soon
(Android and iOS screenshots will be added here once the UI is finalized.)




---

About the author

This project was created by Sergio Ramírez, a Software Engineer focused on:

Android (Kotlin, Jetpack Compose)

iOS (SwiftUI)

Backend services (Python)

Cloud and safety/IoT-related systems


You can find more on LinkedIn and GitHub.
