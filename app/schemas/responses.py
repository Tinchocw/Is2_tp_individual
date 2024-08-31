from app.schemas.status import Status

RFC_7087 = {
    "type": {
        "type": "string"
    },
    "title": {
        "type": "string"
    },
    "status": {
        "type": "integer"
    },
    "detail": {
        "type": "string"
    },
    "instance": {
        "type": "string"
    },
}


class ResponseModel:

    @classmethod
    def post_response_model(cls):
        return {
            Status.http_201_created(): {
                "description": "Snap created successfully",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string",
                                               "format": "uuid"},
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Status.http_400_bad_request(): {
                "description": "Bad request error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            },
            Status.http_500_internal_server_error(): {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            }
        }

    @classmethod
    def get_response_model(cls):
        return {
            Status.http_200_ok(): {
                "description": "A list of snaps",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {"type": "string",
                                                   "format": "uuid"},
                                            "message": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Status.http_500_internal_server_error(): {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            }
        }

    @classmethod
    def delete_response_model(cls):
        return {
            Status.http_204_no_content(): {
                "description": "Snap deleted successfully"
            },
            Status.http_404_not_found(): {
                "description": "Snap not found",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            },
            Status.http_500_internal_server_error(): {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            }
        }

    @classmethod
    def get_by_id_response_model(cls):
        return {
            Status.http_200_ok(): {
                "description": "Snap retrieved successfully",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string",
                                               "format": "uuid"},
                                        "message": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Status.http_404_not_found(): {
                "description": "Snap not found",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            },
            Status.http_500_internal_server_error(): {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": RFC_7087
                        }
                    }
                }
            }
        }
