import Foundation

struct UserResponse: Codable {
    let id: String
    let name: String
    let email: String?
}

struct CreateUserRequest: Codable {
    let name: String
    let email: String?
}

struct CheckInRequest: Codable {
    let type: String
}

struct CheckInResponse: Codable, Identifiable {
    let id: String
    let user_id: String
    let timestamp: String
    let type: String
}