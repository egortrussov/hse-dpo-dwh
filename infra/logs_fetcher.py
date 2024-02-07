import requests
import json
import time

from config import (
    API_URL,
    CHECK_STATUS_API_URL,
    DOWNLOAD_LOG_API_URL,
    TOKEN,
)

class LogsFetcherBase:

    def __init__(self, api_key):
        self._api_key = api_key
        self._fields = []
        self._rows = []
    
    def fetch_logs(
            self,
            fields_list,
            date_start,
            date_end,
            logs_type="hits",
    ):
        params = {
            'date1': date_start,
            'date2': date_end,
            "source": logs_type,
            "fields": ",".join(fields_list),
            "oauth_token": self._api_key,
        }

        r = requests.post(
            API_URL,
            params = params,
            headers={
                'Authorization': self._api_key,
            }
        )

        parsed = json.loads(r.text)
        print(parsed)
        print("Created request with id " + str(parsed["log_request"]["request_id"]))

        self._request_id = parsed["log_request"]["request_id"]

        self.__wait_for_request()

    
    def __wait_for_request(self):
        while True:
            r = requests.get(
                CHECK_STATUS_API_URL + "/" + str(self._request_id),
                headers={
                    'Authorization': self._api_key,
                }
            )
            parsed = json.loads(r.text)

            if "log_request" not in parsed.keys():
                print("Error sending request, sleep")
                time.sleep(5)

            if (parsed["log_request"]["status"] != "processed"):
                print(parsed)
                print(f"Not ready, status={parsed['log_request']['status']} retry in 5 seconds")
                time.sleep(5)
            else:
                self._parts_num = len(parsed["log_request"]["parts"])
                print("Logs ready, parts number is" + str(self._parts_num))
                self.__download_logs()
                break
    

    def __download_logs(self):

        for part_num in range(self._parts_num):
            r = requests.get(
                CHECK_STATUS_API_URL + "/" + str(self._request_id) + "/part/" + str(part_num) + "/download",
                headers={
                    'Authorization': self._api_key,
                }
            )

            self._fields, new_rows = self.__parse_result_table(r.text)
            self._rows += new_rows

            print(f"Result with part {part_num} written to output file")
        print("Download successful")
    

    def get_rows(self):
        return self._rows
    

    def get_fields(self):
        return self._fields
    

    def __parse_result_table(self, table_str: str):
        fields = []
        rows = []

        table_str_rows = table_str.split("\n")
        fields = table_str_rows[0].split("\t")
        
        for i in range(1, len(table_str_rows)):
            rows.append(table_str_rows[i].split("\t"))

        return (fields, rows)


class LogsFetcher(LogsFetcherBase):
    def __init__(self):
        super().__init__(TOKEN)

