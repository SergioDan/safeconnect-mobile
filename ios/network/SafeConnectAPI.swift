import Foundation

class SafeConnectAPI {

    static let shared = SafeConnectAPI()
    private let baseURL = "http://localhost:8000/"

    func createUser(name: String) async throws -> UserResponse {
        let url = URL(string: "\(baseURL)users")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body = CreateUserRequest(name: name, email: nil)
        request.httpBody = try JSONEncoder().encode(body)

        let (data, _) = try await URLSession.shared.data(for: request)
        return try JSONDecoder().decode(UserResponse.self, from: data)
    }

    func sendCheckIn(userId: String, type: String) async throws -> CheckInResponse {
        let url = URL(string: "\(baseURL)users/\(userId)/checkins")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body = CheckInRequest(type: type)
        request.httpBody = try JSONEncoder().encode(body)

        let (data, _) = try await URLSession.shared.data(for: request)
        return try JSONDecoder().decode(CheckInResponse.self, from: data)
    }
}