package com.safeconnect.app.network

import retrofit2.http.Body
import retrofit2.http.POST
import retrofit2.http.GET
import retrofit2.http.Path

data class CreateUserRequest(
    val name: String,
    val email: String? = null
)

data class UserResponse(
    val id: String,
    val name: String,
    val email: String?
)

enum class CheckInType {
    OK, NEED_TO_TALK
}

data class CheckInRequest(
    val type: CheckInType
)

data class CheckInResponse(
    val id: String,
    val user_id: String,
    val timestamp: String,
    val type: CheckInType
)

interface SafeConnectApi {

    @POST("users")
    suspend fun createUser(@Body body: CreateUserRequest): UserResponse

    @POST("users/{id}/checkins")
    suspend fun createCheckIn(
        @Path("id") userId: String,
        @Body body: CheckInRequest
    ): CheckInResponse

}
