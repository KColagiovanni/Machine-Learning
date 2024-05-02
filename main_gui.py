import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import plot_data
import matplotlib.pyplot as plt
from process_and_train_data import ProcessAndTrainData


class PlotData(QWidget):

    def __init__(self):
        super().__init__()

        print('In PlotData __init__()')

        # Define the window title
        self.setWindowTitle('Plot')

        # Define the window geometry
        self.setGeometry(0, 0, 600, 600)

        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure' it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Just some button connected to 'plot' method
        self.bar_graph_button = QPushButton('Bar Graph')

        # adding action to the button
        self.bar_graph_button.clicked.connect(plot_data.bar_graph)

        # Just some button connected to 'plot' method
        self.scatter_plot_button = QPushButton('Scatter Plot')

        # adding action to the button
        self.scatter_plot_button.clicked.connect(plot_data.scatter_plot)

        plot_window_layout = QVBoxLayout()

        # self.plot_label = QLabel('Plot')
        # plot_window_layout.addWidget(self.plot_label)

        # adding canvas to the layout
        plot_window_layout.addWidget(self.canvas)

        # adding push button to the layout
        plot_window_layout.addWidget(self.bar_graph_button)

        # adding push button to the layout
        plot_window_layout.addWidget(self.scatter_plot_button)

        self.setLayout(plot_window_layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_width = 150
        pos_x = 125
        # pd = PlotData()

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(0, 0, 400, 350)

        # Define accuracy label widget
        self.accuracy_label = QLabel("Accuracy: ", self)

        # Defining position and size of label
        self.accuracy_label.move(pos_x, 250)
        self.accuracy_label.resize(widget_width, 25)

        # Label border
        self.accuracy_label.setStyleSheet("border: 1px solid black;")

        # Show bar graph button
        self.bar_graph_button = QPushButton(self)
        self.bar_graph_button.setText('Show Bar Graph')
        self.bar_graph_button.setFixedWidth(widget_width)
        self.bar_graph_button.move(pos_x, 100)
        self.bar_graph_button.clicked.connect(self.show_bar_graph)

        # Show scatter plots button
        self.scatter_plots_button = QPushButton(self)
        self.scatter_plots_button.setText('Show Scatter Plot')
        self.scatter_plots_button.setFixedWidth(widget_width)
        self.scatter_plots_button.move(pos_x, 150)
        self.scatter_plots_button.clicked.connect(self.show_scatter_plots)

        # Predict data button
        self.predict_button = QPushButton(self)
        self.predict_button.setText('Predict')
        self.predict_button.setFixedWidth(widget_width)
        self.predict_button.move(pos_x, 200)
        self.predict_button.clicked.connect(self.make_prediction)

        # Close button
        self.close_button = QPushButton(self)
        self.close_button.setText('Close')
        self.close_button.setFixedWidth(widget_width)
        self.close_button.move(pos_x, 300)
        self.close_button.clicked.connect(self.close_window)

        # Show the window and all the widgets
        print('Showing the main window.')
        self.show()

    def make_prediction(self):
        ptd = ProcessAndTrainData()
        data_frame = ptd.load_data('diabetes.csv')
        X, y, neg, pos = ptd.prepare_data(data_frame)
        X_train, X_test, y_train, y_test = ptd.train_data(X, y)
        accuracy_score = ptd.predict_data(X_train, X_test, y_train, y_test)
        self.accuracy_label.setText(f'Accuracy: {round(accuracy_score * 100, 2)}%')

    # @staticmethod
    def show_bar_graph(self, checked):
        # ptd = ProcessAndTrainData()
        # data_frame = ptd.load_data('diabetes.csv')
        # X, y, neg, pos = ptd.prepare_data(data_frame)
        print('In show_bar_graph() method')
        self.pd = PlotData()
        self.pd.show()
        # pd.bar_graph(X, y, neg, pos)
        # return X, neg, pos

    @staticmethod
    def show_scatter_plots():
        print('Preparing the scatter plots')
        ptd = ProcessAndTrainData()
        pd = PlotData()
        data_frame = ptd.load_data('diabetes.csv')
        pd.scatter_plot(data_frame)

    def close_window(self):

        print('Exiting Application')

        # Close the window
        self.close()


if __name__ == '__main__':

    # Create PyQt5 app
    App = QApplication(sys.argv)

    # Create the instance of our Window
    window = MainWindow()

    # Start the app
    sys.exit(App.exec_())
