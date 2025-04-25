<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

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

  <h3 align="center">OLX API Wrapper</h3>

  <p align="center">
    A Python client for the OLX Developer API, enabling seamless integration with OLX services.
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
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

OLX API Wrapper is a Python library designed to simplify integration with the OLX Developer API. It allows developers to:

- Fetch user data
- Manage adverts with CRUD operations
- Access OLX API resources effortlessly

This library is ideal for developers looking to streamline their interaction with OLX services.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][python]][python-url]
- [![requests][requests]][requests-url]
- [![dacite][dacite]][dacite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To use the OLX API Wrapper, you need to sign in to the OLX Developer Portal and create an app. For more details, visit [Getting Access to the API](https://developer.olx.pl/articles/getting-access-to-api).

### Prerequisites

1. [Not required for public API] Obtain your **Client ID** and **Client Secret** from the OLX Developer Portal.
2. Store them securely (e.g., as environment variables). Avoid hardcoding them in your code.

Supported countries:

- OLX PL
- OLX BG
- OLX RO
- OLX PT
- OLX UA
- OLX KZ

By default, requests are sent to OLX **PL**. To change the country, pass the `country_code` argument to the relevant class:

```python
from olx.partner import Auth, Adverts

auth = Auth(country_code="bg")
adverts = Adverts(country_code="ro")
```

### Installation

1. Install the package:

   ```sh
   pip install olx-api-wrapper
   ```

2. Authenticate using the authorization code:

   ```python
   from olx.partner import Auth

   auth = Auth(client_id="your_client_id", client_secret="your_client_secret")
   auth.authenticate(code="authorization_code")
   access_token = auth.access_token
   ```

3. Use the `AuthResponse` object to retrieve additional information:

   ```python
   auth_response = auth.authenticate(code="authorization_code")
   print(auth_response.refresh_token)  # Retrieve the refresh token
   ```

4. Refresh an expired access token:
   ```python
   auth.refresh(refresh_token=auth_response.refresh_token)
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Below are examples of how to use the `olx-api-wrapper` in your project. Ensure you have an access token before proceeding.

### Example 1: Fetch Authenticated User Info

```python
from olx.partner import Users

users = Users(access_token="your_access_token")
user_info = users.get_authenticated_user()
print(user_info.email)  # Output: john@mail.com
```

### Example 2: Get Category Suggestions

```python
from olx.partner import CategoriesAttributes

categories = CategoriesAttributes(access_token="your_access_token")
suggestions = categories.get_category_suggestions(ad_title="Honda Hornet")
print(suggestions)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Public API Methods

The `olx.public` module provides methods to interact with OLX's public API. Below are the available methods and their usage examples:

### Example 1: Fetch Offers

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
offers = olx_public.get_offers(category_id=123, offset=0, limit=10)
print(offers)
```

### Example 2: Get Offer Details

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
offer = olx_public.get_offer(offer_id=456)
print(offer)
```

### Example 3: Get Suggested Offers

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
suggested_offers = olx_public.get_suggested_offers(offer_id=456)
print(suggested_offers)
```

### Example 4: Get Offer Filters

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
filters = olx_public.get_offer_filters()
print(filters)
```

### Example 5: Get Breadcrumbs

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
breadcrumbs = olx_public.get_breadcrumbs(category_id=123)
print(breadcrumbs)
```

### Example 6: SEO Popular Searches

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
popular_searches = olx_public.seo.popular_searches(category_id=123, count=5)
print(popular_searches)
```

### Example 7: SEO Offer Details

```python
from olx.public import OlxPublic

olx_public = OlxPublic()
offer_seo = olx_public.seo.offer_seo(offer_id=456)
print(offer_seo)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

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
[python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[dacite]: https://img.shields.io/badge/dacite-20232A?style=for-the-badge&logo=github&logoColor=61DAFB
[dacite-url]: https://github.com/konradhalas/dacite
[requests]: https://img.shields.io/badge/requests-35495E?style=for-the-badge&logo=github&logoColor=4FC08D
[requests-url]: https://github.com/psf/requests
