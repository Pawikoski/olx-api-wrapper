<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Pawikoski/olx-api-wrapper">
    <img src="images/image.png" alt="Logo" height="80">
  </a>

<h3 align="center">OLX Api Wrapper</h3>

  <p align="center">
    Simple client for OLX Developer API written in Python
    <br />
    <a href="https://github.com/Pawikoski/olx-api-wrapper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Pawikoski/olx-api-wrapper">View Demo</a>
    ·
    <a href="https://github.com/Pawikoski/olx-api-wrapper/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Pawikoski/olx-api-wrapper/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

OLX API Wrapper: Easy Solution for Working with OLX. With this Python library you can quickly fetch user data, handle adverts with simple CRUD operations, and seamlessly integrate with the OLX API. Simplify your development process and focus on building your app hassle-free.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![requests][requests]][requests-url]
* [![dacite][dacite]][dacite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to use OLX Api you nned to sign in at OLX Developer Portal and create an App.
More details: https://developer.olx.pl/articles/getting-access-to-api

### Prerequisites

To use this API Wrapper you need to copy Client ID and Client Secret. Store them in the safe place. In your code you can use them as enviroment variables, they sholdn't be hardcoded.
You can perform actions with API on:
- OLX PL
- OLX BG
- OLX RO
- OLX PT
- OLX UA
- OLX KZ
  
By default, all requests are sent to olx.**PL**. To change it you must pass `country_code` argument to every child of Olx class, i.e.:
```python
olx.partner.Auth(country_code="bg")
olx.partner.Adverts(country_code="ro")
olx.partner.Users(country_code="pt")
olx.partner.CitiesDistricts(country_code="ua")
olx.partner.AdvertsStatistics(country_code="kz")
# etc...
```

### Installation

1. Install `olx-api-wrapper` package
   ```sh
   pip install olx-api-wrapper
   ```
2. In order to get access token you need to authenticate with authorization code. [How to get authorization code?](https://developer.olx.pl/api/doc#section/Authentication/Grant-type:-authorization_code)
   ```python
   from olx.partner import Auth
   auth = Auth(
     client_id="your_client_id",
     client_secret="your_client_secret",
   )
   auth.authenticate(code='authorization_code')
   access_token = auth.access_token
   ```
3. Now you have access token which you will need to have an access to OLX API resources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Using `olx-api-wrapper` in Your Project

Below are examples demonstrating the usage of `olx-api-wrapper` in your project. Please note that you require an access token to execute the actions described below.

Each section from the OLX API documentation corresponds to a separate object within `olx-api-wrapper`. For instance, the section Users in the documentation is represented as olx.Users. Additionally, each endpoint mentioned in the documentation corresponds to a single method. For example, the 'Get user' endpoint becomes the method `olx.partner.Users().get_user(user_id)`.

If a method returns a value, it will be in the form of a dataclass object. This facilitates ease of use and clarity due to type hints. You can access values as properties, for example, `user_values.email`.

This structure provides a convenient and straightforward approach to integrating `olx-api-wrapper` into your project.

=====================================

First of all you need to assign an object you want to use to variable and then use available method of this object. You must to pass `access_token` to every single object.

Prerequisites: Import olx module.
```python
import olx
```

- Show authenticated user info
  ```python
  users = olx.partner.Users(access_token='your_access_token')
  user_info = users.get_authenticated_user()
  # AuthenticatedUser(id=123, email='john@mail.com', status='confirmed', name='Paweł', phone='123123123', phone_login=None, created_at='2018-01-29 19:48:49', last_login_at='2024-04-26 17:20:48', avatar=None, is_business=True)
  
  user_email = user_info.email
  # john@mail.com
  ```
- Get category suggestions for provided ad title
  ```python
  categories_and_attributes = olx.partner.CategoriesAttributes(access_token='your_access_token')
  suggestions = categories_and_attributes.get_category_suggestions(ad_title='Honda Hornet')
  # [CategorySuggestion(id='1379', name='Szosowo - Turystyczny', path=[CategoryPath(id='5', name='Motoryzacja'), CategoryPath(id='81', name='Motocykle i Skutery')])]
  ```

<!-- TODO: _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Paweł Stawikowski - pawikoski@gmail.com

Project Link: [https://github.com/Pawikoski/olx-api-wrapper](https://github.com/Pawikoski/olx-api-wrapper)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Pawikoski/olx-api-wrapper.svg?style=for-the-badge
[contributors-url]: https://github.com/Pawikoski/olx-api-wrapper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Pawikoski/olx-api-wrapper.svg?style=for-the-badge
[forks-url]: https://github.com/Pawikoski/olx-api-wrapper/network/members
[stars-shield]: https://img.shields.io/github/stars/Pawikoski/olx-api-wrapper.svg?style=for-the-badge
[stars-url]: https://github.com/Pawikoski/olx-api-wrapper/stargazers
[issues-shield]: https://img.shields.io/github/issues/Pawikoski/olx-api-wrapper.svg?style=for-the-badge
[issues-url]: https://github.com/Pawikoski/olx-api-wrapper/issues
[license-shield]: https://img.shields.io/github/license/Pawikoski/olx-api-wrapper.svg?style=for-the-badge
[license-url]: https://github.com/Pawikoski/olx-api-wrapper/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/paweł-stawikowski
[product-image]: images/image.png
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[dacite]: https://img.shields.io/badge/dacite-20232A?style=for-the-badge&logo=github&logoColor=61DAFB
[dacite-url]: https://github.com/konradhalas/dacite
[requests]: https://img.shields.io/badge/requests-35495E?style=for-the-badge&logo=github&logoColor=4FC08D
[requests-url]: https://github.com/psf/requests
