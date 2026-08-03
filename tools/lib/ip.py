from fastapi import Request


def get_client_ip(request: Request) -> str | None:
    """
    リクエストからクライアントのIPアドレスを取得する関数。
    Args:
        request (Request): FastAPIのリクエストオブジェクト。
    Returns:
        str | None: クライアントのIPアドレス。取得できない場合は"Unknown"を返す。
    """
    if request.client:
        client_ip = request.client.host
    else:
        client_ip = None
    return client_ip
