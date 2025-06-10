# from urllib.parse import parse_qs, urlparse

import requests
from fake_useragent import UserAgent

from .utils import reverse_url_to_params


def graphql_request(search_url: str, use_fake_ua: bool = False):
    graphql_query = """
query ListingSearchQuery(
  $searchParameters: [SearchParameter!] = {key: "", value: ""}
) {
  clientCompatibleListings(searchParameters: $searchParameters) {
    __typename
    ... on ListingSuccess {
      __typename
      data {
        id
        location {
          city {
            id
            name
            normalized_name
            _nodeId
          }
          district {
            id
            name
            normalized_name
            _nodeId
          }
          region {
            id
            name
            normalized_name
            _nodeId
          }
        }
        last_refresh_time
        delivery {
          rock {
            active
            mode
            offer_id
          }
        }
        created_time
        category {
          id
          type
          _nodeId
        }
        contact {
          courier
          chat
          name
          negotiation
          phone
        }
        business
        omnibus_pushup_time
        photos {
          link
          height
          rotation
          width
        }
        promotion {
          highlighted
          top_ad
          options
          premium_ad_page
          urgent
          b2c_ad_page
        }
        protect_phone
        shop {
          subdomain
        }
        title
        status
        url
        user {
          id
          uuid
          _nodeId
          about
          b2c_business_page
          banner_desktop
          banner_mobile
          company_name
          created
          is_online
          last_seen
          logo
          logo_ad_page
          name
          other_ads_enabled
          photo
          seller_type
          social_network_account_type
        }
        offer_type
        params {
          key
          name
          type
          value {
            __typename
            ... on GenericParam {
              key
              label
            }
            ... on CheckboxesParam {
              label
              checkboxParamKey: key
            }
            ... on PriceParam {
              value
              type
              previous_value
              previous_label
              negotiable
              label
              currency
              converted_value
              converted_previous_value
              converted_currency
              arranged
              budget
            }
            ... on SalaryParam {
              from
              to
              arranged
              converted_currency
              converted_from
              converted_to
              currency
              gross
              type
            }
            ... on ErrorParam {
              message
            }
          }
        }
        _nodeId
        description
        external_url
        key_params
        partner {
          code
        }
        map {
          lat
          lon
          radius
          show_detailed
          zoom
        }
        safedeal {
          allowed_quantity
          weight_grams
        }
        valid_to_time
      }
      metadata {
        filter_suggestions {
          category
          label
          name
          type
          unit
          values {
            label
            value
          }
          constraints {
            type
          }
          search_label
        }
        search_id
        total_elements
        visible_total_count
        source
        search_suggestion {
          url
          type
          changes {
            category_id
            city_id
            distance
            district_id
            query
            region_id
            strategy
            excluded_category_id
          }
        }
        facets {
          category {
            id
            count
            label
            url
          }
          category_id_1 {
            count
            id
            label
            url
          }
          category_id_2 {
            count
            id
            label
            url
          }
          category_without_exclusions {
            count
            id
            label
            url
          }
          category_id_3_without_exclusions {
            id
            count
            label
            url
          }
          city {
            count
            id
            label
            url
          }
          district {
            count
            id
            label
            url
          }
          owner_type {
            count
            id
            label
            url
          }
          region {
            id
            count
            label
            url
          }
          scope {
            id
            count
            label
            url
          }
        }
        new
        promoted
      }
      links {
        first {
          href
        }
        next {
          href
        }
        previous {
          href
        }
        self {
          href
        }
      }
    }
    ... on ListingError {
      __typename
      error {
        code
        detail
        status
        title
        validation {
          detail
          field
          title
        }
      }
    }
  }
}
"""

    # query_params = urlparse(search_url).query
    # variables = parse_qs(query_params)
    # variables.pop("min_id", None)

    olx_params = reverse_url_to_params(search_url)

    # try:
    #     olx_params = reverse_url_to_params(search_url)

    #     if "query" in olx_params:
    #         variables["query"] = olx_params["query"]

    #     if "category_id" in olx_params:
    #         variables["category_id"] = olx_params["category_id"]
    # except Exception as e:
    #     print(f"Error parsing URL: {e}")
    #     return None, 400

    graphql_variables = []

    for key, value in olx_params.items():
        if isinstance(value, list) and "enum_" in key:
            for item in value:
                graphql_variables.append({"key": key, "value": str(item)})
            continue
        graphql_variables.append({"key": key, "value": str(value)})

    sort_variable_index = next(
        (
            index
            for index, variable in enumerate(graphql_variables)
            if variable["key"] == "sort_by"
        ),
        None,
    )
    if sort_variable_index is not None:
        graphql_variables[sort_variable_index]["value"] = "created_at:desc"
    else:
        graphql_variables.append({"key": "order_by", "value": "created_at:desc"})

    headers = {}
    if use_fake_ua:
        ua = UserAgent(browsers=["Chrome", "Edge", "Firefox"], platforms=["Windows", "Linux"])
        headers["User-Agent"] = ua.random

    try:
        response = requests.post(
            "https://www.olx.pl/apigateway/graphql",
            json={
                "query": graphql_query,
                "variables": {"searchParameters": graphql_variables},
            },
            headers=headers,
        )
        data = response.json()
        return data, response.status_code
    except Exception as e:
        return None, response.status_code


# TODO: Pydantic model for the response
# TODO: manual pass variables in function parameters
