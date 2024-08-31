class Status:

    @classmethod
    def http_200_ok(cls):
        return 200

    @classmethod
    def http_204_no_content(cls):
        return 204

    @classmethod
    def http_400_bad_request(cls):
        return 400

    @classmethod
    def http_201_created(cls):
        return 201

    @classmethod
    def http_404_not_found(cls):
        return 404

    @classmethod
    def http_500_internal_server_error(cls):
        return 500
