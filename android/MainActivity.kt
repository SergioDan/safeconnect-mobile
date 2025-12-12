qpackage com.safeconnect.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.lifecycle.viewmodel.compose.viewModel
import com.safeconnect.app.ui.CheckInScreen
import com.safeconnect.app.viewmodel.CheckInViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            val viewModel: CheckInViewModel = viewModel()
            CheckInScreen(viewModel = viewModel)
        }
    }
}
