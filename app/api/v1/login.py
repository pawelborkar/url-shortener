"""
@params: email, password (request body, JSON)
@method: POST
@return:
    - access_token    (10 min)
    - refresh_token   (7days or 7 * 60 * 24)
    - token_type      ("bearer")
    - expires_in      (600 seconds or 10 mins)
"""
