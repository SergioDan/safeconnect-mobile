package com.safeconnect.app.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.safeconnect.app.network.CheckInType
import com.safeconnect.app.network.RetrofitClient
import com.safeconnect.app.repository.CheckInRepository
import com.safeconnect.app.storage.LocalStore
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class CheckInViewModel(
    private val localStore: LocalStore
) : ViewModel() {

    private val repository = CheckInRepository(RetrofitClient.api)

    // ---------- UI STATE ----------

    private val _status = MutableStateFlow("")
    val status: StateFlow<String> = _status

    private val _history = MutableStateFlow<List<String>>(emptyList())
    val history: StateFlow<List<String>> = _history

    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading

    private val _error = MutableStateFlow<String?>(null)
    val error: StateFlow<String?> = _error

    // ---------- INTERNAL STATE ----------

    private var userId: String? = null

    // ---------- INIT ----------

    init {
        // Load saved history
        viewModelScope.launch {
            localStore.historyFlow().collect { savedHistory ->
                _history.value = savedHistory
            }
        }

        // Load saved userId
        viewModelScope.launch {
            localStore.userIdFlow().collect { savedUserId ->
                if (!savedUserId.isNullOrBlank()) {
                    userId = savedUserId
                }
            }
        }
    }

    // ---------- ACTIONS ----------

    fun sendCheckIn(type: CheckInType) {
        viewModelScope.launch {
            _isLoading.value = true
            _error.value = null
            _status.value = "Sending..."

            try {
                // Create backend user only once
                if (userId.isNullOrBlank()) {
                    val user = repository.createUser("Android User")
                    userId = user.id
                    localStore.saveUserId(user.id)
                }

                // Send check-in
                val response = repository.sendCheckIn(userId!!, type)

                val newItem = "${type.name} → ${response.timestamp}"
                val updatedHistory = _history.value + newItem

                _history.value = updatedHistory
                localStore.saveHistory(updatedHistory)

                _status.value = "Done!"
            } catch (e: Exception) {
                _error.value = e.message ?: "Something went wrong"
            } finally {
                _isLoading.value = false
            }
        }
    }

    fun clearHistory() {
        viewModelScope.launch {
            _history.value = emptyList()
            localStore.clearHistory()
            _status.value = "History cleared"
        }
    }
}