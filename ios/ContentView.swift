import SwiftUI

struct ContentView: View {

    @StateObject private var viewModel = CheckInViewModel()

    var body: some View {
        VStack(spacing: 16) {
            Text("SafeConnect")
                .font(.largeTitle)

            if let error = viewModel.error {
                Text(error)
                    .foregroundColor(.red)
            }

            if viewModel.isLoading {
                ProgressView()
            }

            Button("I'm OK ✔️") {
                Task {
                    await viewModel.sendCheckIn(type: "OK")
                }
            }
            .frame(maxWidth: .infinity)

            Button("Need to Talk ☎️") {
                Task {
                    await viewModel.sendCheckIn(type: "NEED_TO_TALK")
                }
            }
            .frame(maxWidth: .infinity)

            Button("Clear history") {
                viewModel.clearHistory()
            }
            .disabled(viewModel.history.isEmpty)

            Text("Status: \(viewModel.status)")

            List(viewModel.history, id: \.self) { item in
                Text(item)
            }
        }
        .padding()
    }
}