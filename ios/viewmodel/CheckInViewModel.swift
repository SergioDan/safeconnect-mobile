import Foundation
import SwiftUI

@MainActor
class CheckInViewModel: ObservableObject {

    @Published var history: [String] = []
    @Published var status: String = ""
    @Published var isLoading: Bool = false
    @Published var error: String?

    private let api = SafeConnectAPI.shared
    private let store = LocalStore()
    private var userId: String?

    init() {
        history = store.loadHistory()
        userId = store.loadUserId()
    }

    func sendCheckIn(type: String) async {
        isLoading = true
        error = nil
        status = "Sending..."

        do {
            if userId == nil {
                let user = try await api.createUser(name: "iOS User")
                userId = user.id
                store.saveUserId(user.id)
            }

            let response = try await api.sendCheckIn(
                userId: userId!,
                type: type
            )

            let item = "\(type) → \(response.timestamp)"
            history.append(item)
            store.saveHistory(history)

            status = "Done!"
        } catch {
            self.error = error.localizedDescription
        }

        isLoading = false
    }

    func clearHistory() {
        history.removeAll()
        store.clearHistory()
        status = "History cleared"
    }
}