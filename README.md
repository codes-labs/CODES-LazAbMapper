# LAMapperApp

## Overview
LAMapperApp is an interactive Shiny application designed for displaying and interrogating LA-ICP-MS maps. It provides various tools for mapping, mineral classification, and statistical analysis geochemical data.

## Project Structure
```
LAMapperApp
├── app
│   ├── LAMapper_app.py        # Main code for the Shiny app
│   ├── requirements.txt        # Python dependencies
│   └── static
│       └── assets              # Static files (images, CSS, JavaScript)
├── Dockerfile                  # Instructions to build the Docker image
├── README.md                   # Project documentation
└── setup.sh                    # Shell script for setup automation
```

## Requirements
To run the application, the following Python libraries are required:
- shiny
- pandas
- matplotlib
- numpy
- scikit-learn
- scikit-image

These dependencies are listed in the `app/requirements.txt` file.

## Docker Setup
To package the application and run it without requiring users to install Python, a Docker container is provided. Follow these steps to build and run the Docker container:

1. **Build the Docker Image**
   Navigate to the root directory of the project and run the following command:
   ```
   docker build -t lamapperapp .
   ```

2. **Run the Docker Container**
   After building the image, you can run the container using:
   ```
   docker run -p 8501:8501 lamapperapp
   ```
   This command maps port 8501 of the container to port 8501 on your host machine.

3. **Access the Application**
   Open your web browser and go to `http://localhost:8501` to access the LAMapperApp.

## Setup Script
The `setup.sh` script can be used to automate the setup process. You can run it with the following command:
```
bash setup.sh
```
This script will handle building the Docker image and starting the server.

## Contributing
Contributions to the LAMapperApp project are welcome. Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
