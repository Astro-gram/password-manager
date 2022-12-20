# Password Manager

[![Stargazers][stars-shield]][stars-url]
[![Forks][forks-shield]][forks-url]
[![MIT License][license-shield]][license-url]

![Project Image](https://raw.githubusercontent.com/Astro-gram/password-manager/master/projectImage.png)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is the list of prerequisites needed for this password manager to run.
* Python 3.10.0+
* Pycryptodome

  ```sh
  pip install pycryptodome
  ```

### Installation & Usage

1. Clone the repo
   ```sh
   git clone https://github.com/Astro-gram/password-manager.git
   ```
3. Go into the folder
   ```sh
   cd password-manager
   ```
4. Run the setup script
   ```sh
   python setup.py
   ```
4. Replace the ```masterPasswordCheck``` variable in ```main.py``` with the newly generated value
   ```python
   masterPasswordCheck = "GENERATED KEY"
   ```
5. Run the password manager and enter the master password you just used
   ```sh
   python main.py
   ```

### Contact

Ben Webster - https://benwebs.com

Youtube - https://www.youtube.com/@benjaminwebster/

Repo - https://github.com/Astro-gram/password-manager

<br/>
**Thank you for visiting this repository!**

[forks-shield]: https://img.shields.io/github/forks/Astro-gram/password-manager.svg?style=for-the-badge
[forks-url]: https://github.com/Astro-gram/password-manager/network/members
[stars-shield]: https://img.shields.io/github/stars/Astro-gram/password-manager.svg?style=for-the-badge
[stars-url]: https://github.com/Astro-gram/password-manager/stargazers

[license-shield]: https://img.shields.io/github/license/Astro-gram/password-manager.svg?style=for-the-badge
[license-url]: https://github.com/Astro-gram/password-manager/blob/master/LICENSE.txt