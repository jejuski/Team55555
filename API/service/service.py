from models.customer_v1 import CustomerV1
from util.altibase import InitAltibase
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt, os, json


class CustomerService:
    def __init__(self):
        # 알티베이스 연결 객체 생성
        self.db_conn = InitAltibase()
        # 서비스 객체에 연결 객체 전달
        self.db = CustomerV1(self.db_conn.get_conn())

    def create_jwt_token(self, username, password):
        load_dotenv()
        # DB 데이터 요청
        user_info = self.db.get_login_info(username, password)
        res_obj = dict()
        ...

    def get_stats_data(self, query_dict):
        count = self.db.get_stats_count(query_dict, False)
        if (count is not None):
            ...

    # 메시지 이력 데이터 조회
    def get_msghist_data(self, query_dict):
        count = self.db.get_msghist_count(query_dict, False)
        if (count is not None):
            ...