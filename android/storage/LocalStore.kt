package com.safeconnect.app.storage

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.dataStore by preferencesDataStore(name = "safeconnect_store")

class LocalStore(private val context: Context) {

    private val HISTORY_KEY = stringPreferencesKey("history")

    fun historyFlow(): Flow<List<String>> {
        return context.dataStore.data.map { prefs ->
            val raw = prefs[HISTORY_KEY] ?: ""
            if (raw.isBlank()) emptyList() else raw.split("\n")
        }
    }

    suspend fun saveHistory(history: List<String>) {
        context.dataStore.edit { prefs ->
            prefs[HISTORY_KEY] = history.joinToString("\n")
        }
    }
}
