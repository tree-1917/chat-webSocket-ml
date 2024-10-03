# 🗨️ Advanced Private Chat with FastAPI & WebSockets

Welcome to the **Advanced Private Chat** application! 🚀 This project leverages **FastAPI** and **WebSockets** to create a real-time, private messaging platform with a sleek and responsive user interface powered by **Bootstrap**. Whether you're looking to integrate real-time communication into your projects or simply exploring WebSocket implementations, this application serves as a robust foundation.

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Real-Time Messaging**: Instant message delivery using WebSockets.
- **Private Chats**: Send messages directly to specific users using their unique IDs.
- **Responsive UI**: Mobile-friendly design built with Bootstrap.
- **Message Timestamps**: Each message is timestamped for better context.

## 📸 Screenshots

### Chat Interface

![Chat Interface](screenshots/Screenshot%20from%202024-10-03%2018-11-59.png)

## 🛠️ Technologies Used

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast (high-performance) web framework for building APIs with Python 3.6+.
  - [Uvicorn](https://www.uvicorn.org/) - A lightning-fast ASGI server.
- **Frontend**:
  - [Bootstrap 5](https://getbootstrap.com/) - Frontend framework for building responsive, mobile-first sites.
  - **WebSockets** - Enables real-time, full-duplex communication between the client and server.
- **Containerization**:
  - [Docker](https://www.docker.com/) - Streamline development and deployment with containerization.

## 🚀 Installation

Follow these steps to set up the **Advanced Private Chat** application on your local machine.

### Prerequisites

- **Python 3.10+**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer.
- **Git**: For cloning the repository. [Download Git](https://git-scm.com/downloads)
- **Docker** _(Optional)_: For containerized deployment. [Download Docker](https://www.docker.com/get-started)

### Clone the Repository

```bash
git clone https://github.com/yourusername/advanced-private-chat.git
cd advanced-private-chat
```

### Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Install Dependencies

```bash
pip install --upgrade pip
pip install fastapi uvicorn
```

## 📝 Usage

### Running the Application Locally

1. **Navigate to the `app` Directory**:

   ```bash
   cd app
   ```

2. **Start the FastAPI Server**:

   ```bash
   uvicorn main:app --reload
   ```

   - The `--reload` flag enables auto-reloading of the server on code changes.

3. **Access the Application**:

   Open your browser and navigate to `http://127.0.0.1:8000/` to access the chat interface.

4. **Using the Chat**:

   - **Enter Your Name**: Upon accessing the chat, you'll be prompted to enter your name.
   - **Send Messages**: Use the input fields to specify the target user's ID and your message.
   - **View Connected Users**: The sidebar displays all currently connected users.
   - **Real-Time Communication**: Messages are sent and received instantly without refreshing the page.

### Docker Deployment _(Optional)_

If you prefer using Docker for deployment, follow these steps:

1. **Build the Docker Image**:

   ```bash
   docker build -t advanced-private-chat .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -d -p 8000:8000 advanced-private-chat
   ```

3. **Access the Application**:

   Open your browser and navigate to `http://localhost:8000/`.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. 🌟 Any contributions you make are **greatly appreciated**.

1. **Fork the Project**
2. **Create Your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
