package com.safeconnect.app.repository

import com.safeconnect.app.network.*

class CheckInRepository(
    private val api: SafeConnectApi
) {
    suspend fun createUser(name: String): UserResponse {
        return api.createUser(CreateUserRequest(name))
    }

    suspend fun sendCheckIn(
        userId: String,
        type: CheckInType
    ): CheckInResponse {
        return api.createCheckIn(userId, CheckInRequest(type))
    }
}
