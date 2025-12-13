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

    private val _status = MutableStateFlow("")
    val status: StateFlow<String> = _status

    private val _history = MutableStateFlow<List<String>>(emptyList())
    val history: StateFlow<List<String>> = _history

    private var userId: String? = null

    init {
        // Cargar historial guardado al abrir la app
        viewModelScope.launch {
            localStore.historyFlow().collect { saved ->
                _history.value = saved
            }
        }
    }

    fun sendCheckIn(type: CheckInType) {
        viewModelScope.launch {
            _status.value = "Sending..."

            if (userId == null) {
                val user = repository.createUser("Android User")
                userId = user.id
            }

            val response = repository.sendCheckIn(userId!!, type)
            val newItem = "${type.name} → ${response.timestamp}"

            val newHistory = _history.value + newItem
            _history.value = newHistory

            // Guardar historial local
            localStore.saveHistory(newHistory)

            _status.value = "Done!"
        }
    }
}