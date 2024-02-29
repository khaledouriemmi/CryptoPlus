# CryptoPlus Encryption/Decryption App

## Description

This application, developed with PyQt5, offers a graphical interface for encrypting and decrypting text using various cipher techniques, including Caesar, Vigenère, ROT13, and Polybius Square. Users can input a decryption key, choose the cipher method, and then either encrypt or decrypt their message. The app features a dynamic UI that adjusts based on the selected encryption method, including options for entering shifts or keys and toggling the visibility of these inputs for enhanced security.

## Features

- Supports multiple cipher techniques: Caesar, Vigenère, ROT13, Polybius Square.
- Dynamic UI that updates based on the selected encryption/decryption method.
- Option to toggle visibility of encryption/decryption keys for security.
- Customizable for adding more cipher techniques.

## Installation

Ensure you have Python and PyQt5 installed. Install PyQt5 via pip if necessary:

```
pip install PyQt5
```

Download the app files, including `main.ui` and any required images in the `image` directory.

## Usage

Run the application with Python. The main UI will prompt you for an encryption/decryption key upon startup:

```
python main.py
```

Follow the on-screen instructions to encrypt or decrypt messages.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Contributions to extend cipher methods or enhance the UI are welcome.

## License

Distributed under the MIT License. See `LICENSE` for more information.
