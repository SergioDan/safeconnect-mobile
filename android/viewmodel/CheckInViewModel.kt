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

    // ----- UI state -----

    private val _status = MutableStateFlow("")
    val status: StateFlow<String> = _status

    private val _history = MutableStateFlow<List<String>>(emptyList())
    val history: StateFlow<List<String>> = _history

    // ----- Internal state -----

    private var userId: String? = null

    // ----- Init: load persisted history -----

    init {
        viewModelScope.launch {
            localStore.historyFlow().collect { savedHistory ->
                _history.value = savedHistory
            }
        }
    }

    // ----- Actions -----

    fun sendCheckIn(type: CheckInType) {
        viewModelScope.launch {
            _status.value = "Sending..."

            // Create user once
            if (userId == null) {
                val user = repository.createUser("Android User")
                userId = user.id
            }

            // Send check-in
            val response = repository.sendCheckIn(userId!!, type)

            val newItem = "${type.name} → ${response.timestamp}"
            val updatedHistory = _history.value + newItem

            _history.value = updatedHistory

            // Persist locally
            localStore.saveHistory(updatedHistory)

            _status.value = "Done!"
        }
    }
}