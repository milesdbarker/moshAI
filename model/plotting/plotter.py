from pathlib import Path
from typing import List, Optional

import matplotlib.pyplot as plt


class Plotter:
    """ Class for making plots """

    def make_histogram(self, title: str, data: List[int], label: str, color: Optional[str] = "blue", bins: Optional[int] = 50, output_path: Optional[Path] = None) -> None:
        """
        Make a histogram of the given data with the given title and output the plot to the specified path.
        :param title: The title for the histogram
        :param data: The  data points (integers) to include in the plot
        :param label: The label for the dataset
        :param color: The color for the data
        :param bins: The number of bins to use for the histogram (defaults to 50)
        :param output_path: The output path for the histogram (if desired)
        :return:
        """
        plt.hist(data, bins=bins, color=color, label=label, stacked=True, alpha=0.5)
        plt.gca().set(title=title, ylabel='Frequency')
        plt.legend()

        if output_path:
            plt.savefig(output_path)

    def clear_figure(self):
        """
        Clear the current figure
        :return:
        """
        plt.clf()
