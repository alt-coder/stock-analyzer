    # Stock Analyzer

    This repository contains various tools and experiments for stock analysis and trading. It explores different techniques, including machine learning models for price prediction, reinforcement learning for option trading strategies, and technical analysis methods like Relative Rotation Graphs.

## Project Components

- **LSTM Stock Analysis:** Jupyter notebooks (`ibm_stock_analysis_lstm.ipynb`, `stock_analysis_lstm.ipynb`) demonstrating the use of Long Short-Term Memory (LSTM) neural networks for predicting stock prices.
- **Option Trading Gym:** A Jupyter notebook (`OptionTradingGym.ipynb`) that sets up a custom OpenAI Gym environment for training reinforcement learning agents to perform option trading. It utilizes the Stable Baselines3 library with the PPO algorithm.
- **Relative Rotation Graph (RRG):** A Jupyter notebook (`RRG.ipynb`) for performing Relative Rotation Graph analysis, a technical analysis tool used to compare the performance of a group of assets against a benchmark.
- **Signal-Based Training:** A Jupyter notebook (`train_on_signals_only.ipynb`) that appears to focus on training models or strategies based purely on trading signals.
- **Stock Analysis Agents and Tools:** The `stock_analysis` subdirectory contains Python scripts (`main.py`, `stock_analysis_agents.py`, `stock_analysis_tasks.py`) and a `tools` module (`browser_tools.py`, `calculator_tools.py`, `search_tools.py`, `sec_tools.py`) that likely form the basis of a more structured stock analysis application or framework, potentially involving autonomous agents.

## Setup and Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1.  **Install Poetry:** Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry for your operating system.
2.  **Install Dependencies:** Navigate to the `stock_analysis` directory in your terminal and run:
    ```bash
    poetry install
    ```
    This will install all necessary packages listed in `stock_analysis/pyproject.toml`.
3.  **Additional Dependencies (for notebooks):** Some notebooks may require additional libraries not managed by Poetry or specific to environments like Google Colab. If running notebooks locally, you might need to install these separately using pip:
    ```bash
    pip install TA-Lib pandas_ta vectorbt bt
    ```
    Note that TA-Lib might require additional system dependencies depending on your OS. Refer to the [TA-Lib installation guide](https://github.com/TA-Lib/ta-lib-python/blob/master/INSTALL.md) for details.

## Usage

-   **Jupyter Notebooks:** The `.ipynb` files can be run in a Jupyter environment (like JupyterLab, Jupyter Notebook, or Google Colab). Open the desired notebook and execute the cells sequentially.
-   **Stock Analysis Application:** Navigate to the `stock_analysis` directory in your terminal. You can likely run the main application using:
    ```bash
    poetry run python main.py
    ```
    Refer to the `main.py` script for specific command-line arguments or usage details.

## Data

Stock price data is expected to be stored in the `./Data` directory in CSV format, with filenames corresponding to stock tickers (e.g., `AAPL.csv`).

Some notebooks include code to download historical data using the `yfinance` library. You may need to run these sections to populate the `./Data` directory.

The `OptionTradingGym.ipynb` notebook specifically mentions loading data from a `dataset.zip` file, which appears to be used in a Google Colab environment after unzipping.

## Contributing

*(Add information on how others can contribute to the project.)*

## License

This project is licensed under the GPL License. 