
# SafeConnect  
A human-centered safety communication app designed to help people stay connected during emergency or high-stress situations.  
SafeConnect aims to provide a fast, reliable way to send alerts, initiate calls, and share real-time status with trusted contacts — even when traditional communication methods fail.

---

## 📌 Why SafeConnect?  
SafeConnect was born from a very personal motivation:  
**creating a simple, reliable way for loved ones to reach each other immediately during moments of fear, danger, or medical need.**

Most solutions are:
- Slow  
- Complicated  
- Not designed for real emergencies  
- Dependent on too many steps  

SafeConnect focuses on:
- **Instant alerting**
- **Minimal taps**
- **Human-centred design**
- **Cross-platform communication**
- **Fail-safe mechanisms**

---

# 🧩 Project Structure

/android              → Android (Kotlin + Jetpack Compose) /ios                  → iOS (SwiftUI) /backend              → FastAPI backend (initial scaffold) /docs                 → Diagrams, architecture and documentation /design               → Branding, UI flows, wireframes /tests                → Unit & integration tests

Each folder may contain `.gitkeep` files while development evolves.

---

# 🏗 Architecture Overview

SafeConnect follows **Clean Architecture** with clear separation of concerns:

- **Domain Layer**  
  - Core models  
  - Business rules  
  - Interfaces  

- **Data Layer**  
  - API clients  
  - Local persistence  
  - Repositories  

- **Presentation Layer**  
  - Jetpack Compose (Android)  
  - SwiftUI (iOS)  
  - State handling (MVI / MVVM)  

This structure keeps the project scalable, testable, and adaptable for multiple platforms.

---

# 🛠 Tech Stack

### **Mobile**
- Android — Kotlin, Jetpack Compose
- iOS — SwiftUI (future development)
- Coroutines / Flow
- Clean Architecture + MVI/MVVM

### **Backend**
- FastAPI (Python)
- WebSocket / REST API
- Future:  
  - Audio streaming service  
  - Alert orchestration engine  
  - Contact management

---

# 🚨 Core Features (MVP)

- One-tap emergency alert ❗
- Live status updates  
- Quick-call connection UI  
- Contact selection  
- Fail-safe retry logic  
- Simple, accessible UI for all ages  

---

# 🧭 Roadmap (High Level)

### **Phase 1 — Core MVP**
- Basic Android UI (Compose)  
- Alert workflow  
- Local persistence  
- Initial FastAPI backend  
- Early tests and monitoring  

### **Phase 2 — Communication Layer**
- WebSocket call session prototype  
- Push notifications  
- Contact linking  

### **Phase 3 — AI-Assisted Safety**
- Voice/shout detection  
- Fall detection  
- Smart post-event log  

### **Phase 4 — Dashboard**
- PWA dashboard for family members  
- Location history  
- Alert playback  

---

# ▶ Running the backend (placeholder)

From `/backend`:

```bash
uvicorn main:app --reload


---

🤝 Contributing

Contributions, feedback, and collaboration ideas are welcome.
Please open an issue or reach out if you'd like to participate.


---

📄 License

MIT License – feel free to use, modify, and contribute.
