import unittest

import psycopg2
from psycopg2.extras import RealDictCursor
from models import AuthorizeModel
from goods import GoodsModel


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        """Установка соединения с БД"""
        self.connection = psycopg2.connect(
            dbname='coursework_prdb',
            user='admin',
            password='qwerty',
            host='localhost'
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def tearDown(self) -> None:
        """Отключение соединения с БД"""
        self.connection.close()

    def test_authorize_employer(self):
        """Проверка на возможность авторизации сотруднику"""
        self.cursor.execute("SELECT * FROM employers LIMIT 1")
        employer = self.cursor.fetchone()
        if not employer:
            self.fail('no employee found')

        login = employer['login']
        password = employer['password']

        authorize_model = AuthorizeModel()
        result = authorize_model.verify_credentials(login, password)
        self.assertTrue(result)

    def test_non_authorize_employer(self):
        """Проверка авторизации сотрудника при неверных данных"""
        authorize_model = AuthorizeModel()
        result = authorize_model.verify_credentials(
            'nonexistent_email@ne.ne1',
            'nonexistent_password'
        )
        self.assertFalse(result)

    def test_filter_goods_category(self):
        """Проверка фильтрации товаров по категории"""
        category = "Стратегические"
        model = GoodsModel()
        model.goods_category = category
        goods = model.get_goods()
        if not len(goods):
            self.fail('no goods found')
        is_all_fits = all([product['category'] == category for product in goods])
        self.assertTrue(is_all_fits)

    def test_sort_goods_title_desc(self):
        """Проверка сортировки товаров по имени (по убыванию)"""
        model = GoodsModel()
        model.sort_field = "title"
        model.sort_type = "DESC"
        limit = model.limit

        self.cursor.execute(f"SELECT * from goods ORDER BY title DESC "
                            f"LIMIT {limit}")
        goods_expected = self.cursor.fetchall()
        if not len(goods_expected):
            self.fail('no goods found')

        goods_actual = model.get_goods()

        self.assertEqual(
            [product['id'] for product in goods_expected],
            [product['id'] for product in goods_actual]
        )


if __name__ == '__main__':
    unittest.main()
