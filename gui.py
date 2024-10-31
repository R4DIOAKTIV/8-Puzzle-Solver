import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QGridLayout, QWidget, QLineEdit, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt  # Import Qt namespace
from main import*
from utils import*

class PuzzleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("8-Puzzle Solver")
        self.setFixedSize(400, 500)
        
        # Create a central widget
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        
        # Create main layout
        mainLayout = QVBoxLayout(centralWidget)
        
        # Create grid layout for the puzzle
        self.gridLayout = QGridLayout()
        self.puzzleLabels = []
        for i in range(3):
            row = []
            for j in range(3):
                label = QLabel(" ")
                label.setFixedSize(50, 50)
                label.setStyleSheet("""
                    border: 2px solid #333;
                    font-size: 20px;
                    text-align: center;
                    background-color: #f0f0f0;
                    color: #333;
                    padding: 10px;
                    """)
                label.setAlignment(Qt.AlignCenter)
                self.gridLayout.addWidget(label, i, j)
                row.append(label)
            self.puzzleLabels.append(row)
        mainLayout.addLayout(self.gridLayout)
        
        # Create input field and button
        inputLayout = QHBoxLayout()
        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Enter starting state (e.g., 123456780)")
        inputLayout.addWidget(self.inputField)
        self.updateButton = QPushButton("Update")
        self.updateButton.clicked.connect(self.updatePuzzle)
        inputLayout.addWidget(self.updateButton)
        mainLayout.addLayout(inputLayout)
        
        # Create dropdown for selecting search algorithm
        self.algorithmComboBox = QComboBox()
        self.algorithmComboBox.addItems(["A* Manhattan", "A* Euclidean", "BFS", "DFS", "IDS"])
        mainLayout.addWidget(self.algorithmComboBox)
        
        # Create control buttons
        self.solveButton = QPushButton("Solve")
        self.solveButton.clicked.connect(self.solve)
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.nextStep)
        self.backwardButton = QPushButton("Backward")
        self.backwardButton.clicked.connect(self.previousStep)
        self.skipButton = QPushButton("Skip")
        self.skipButton.clicked.connect(self.skipToSolution)
        self.randomButton = QPushButton("Random")
        self.randomButton.clicked.connect(self.randomizePuzzle)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.solveButton)
        buttonLayout.addWidget(self.backwardButton)
        buttonLayout.addWidget(self.nextButton)
        buttonLayout.addWidget(self.skipButton)
        buttonLayout.addWidget(self.randomButton)
        mainLayout.addLayout(buttonLayout)
        
        # Create a label for displaying messages
        self.messageLabel = QLabel("")
        self.messageLabel.setStyleSheet("color: red; font-size: 16px;")
        mainLayout.addWidget(self.messageLabel)
        self.solutionPath = []
        self.currentStep = 0

    def updatePuzzle(self):
        state = self.inputField.text()
        if len(state) == 9 and state.isdigit():
            for i in range(3):
                for j in range(3):
                    self.puzzleLabels[i][j].setText(state[i * 3 + j])
            self.messageLabel.setText("")  # Clear any previous message
        else:
            self.messageLabel.setText("Invalid input state")

    def solve(self):
        start = self.inputField.text()
        goal = "012345678"
        if not isSolvable(start):
            self.messageLabel.setText("This puzzle is unsolvable.")
            return

        algorithm = self.algorithmComboBox.currentText()
        
        if algorithm == "A* Manhattan":
            self.solutionPath, explored, t, max_depth= aStar(start, goal, calculateManhattan)
        elif algorithm == "A* Euclidean":
            self.solutionPath, explored, t, max_depth = aStar(start, goal, calculateEuclidean)
        elif algorithm == "BFS":
            self.solutionPath, explored, t, max_depth = BFS(start, goal)
        elif algorithm == "DFS":
            self.solutionPath, explored, t, max_depth = DFS(start, goal)
        elif algorithm == "IDS":
            self.solutionPath, explored, t, max_depth= IDS(start, goal)
        
        self.currentStep = 0
        self.messageLabel.setText(f"Path found with {algorithm}.")
        print("Path:", self.solutionPath)

    def nextStep(self):
        if self.currentStep < len(self.solutionPath) - 1:
            self.currentStep += 1
            self.updatePuzzleFromState(self.solutionPath[self.currentStep])

    def previousStep(self):
        if self.currentStep > 0:
            self.currentStep -= 1
            self.updatePuzzleFromState(self.solutionPath[self.currentStep])

    def randomizePuzzle(self):
        state = randomState()
        self.inputField.setText("".join(state))
        self.updatePuzzle()

    def skipToSolution(self):
        if self.solutionPath:
            self.currentStep = len(self.solutionPath) - 1
            self.updatePuzzleFromState(self.solutionPath[self.currentStep])

    def updatePuzzleFromState(self, state):
        for i in range(3):
            for j in range(3):
                self.puzzleLabels[i][j].setText(state[i * 3 + j])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PuzzleApp()
    window.show()
    sys.exit(app.exec_())