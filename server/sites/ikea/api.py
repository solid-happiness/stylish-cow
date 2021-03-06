from typing import List

from server.models import Product, Company, SearchParams


class IkeaApi(Company):
    title = 'Ikea'
    main_url = 'https://www.ikea.com/'
    logo = '/companies/ikea/img/logo.png'

    @classmethod
    async def search(cls, params: SearchParams) -> List[Product]:
        response = await cls.get(
            f'https://sik.search.blue.cdtapps.com/ru/ru/search-result-page?q={params.query}&size={params.size}&columns=4'
        )
        search_result = response.get('searchResultPage')

        if not search_result:
            return []

        items = list(filter(
            lambda item: item.get('product'),
            search_result['products']['main']['items']
        ))
        return [
            Product(
                search_query=params.query,
                title=item['product']['name'],
                price=item['product']['priceNumeral'],
                image_url=item['product']['mainImageUrl'],
                product_url=item['product']['pipUrl'],
                description=item['product']['typeName'],
                site_logo=cls.logo,
            ) for item in items
        ]
