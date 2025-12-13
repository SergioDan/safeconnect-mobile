package com.safeconnect.app.ui.state

sealed class CheckInUiState {
    object Idle : CheckInUiState()
    object Loading : CheckInUiState()
    data class Success(val message: String) : CheckInUiState()
    data class Error(val reason: String) : CheckInUiState()
}