import Foundation

class LocalStore {

    private let historyKey = "checkin_history"
    private let userIdKey = "user_id"

    func loadHistory() -> [String] {
        UserDefaults.standard.stringArray(forKey: historyKey) ?? []
    }

    func saveHistory(_ history: [String]) {
        UserDefaults.standard.set(history, forKey: historyKey)
    }

    func clearHistory() {
        UserDefaults.standard.removeObject(forKey: historyKey)
    }

    func loadUserId() -> String? {
        UserDefaults.standard.string(forKey: userIdKey)
    }

    func saveUserId(_ id: String) {
        UserDefaults.standard.set(id, forKey: userIdKey)
    }
}