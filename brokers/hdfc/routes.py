"""
HDFC Sky API Routes
"""

# =============================================================================
# AUTHENTICATION
# =============================================================================

LOGIN = "/login"

VALIDATE = "/validate"

LOGOUT = "/logout"

# =============================================================================
# ORDERS
# =============================================================================

PLACE_ORDER = "/orders"

MODIFY_ORDER = "/orders/modify"

CANCEL_ORDER = "/orders/cancel"

ORDER_BOOK = "/orders"

TRADE_BOOK = "/trades"

# =============================================================================
# PORTFOLIO
# =============================================================================

POSITIONS = "/portfolio/positions"

HOLDINGS = "/portfolio/holdings"

FUNDS = "/portfolio/funds"

# =============================================================================
# MARKET DATA
# =============================================================================

MARKET_QUOTE = "/market/quote"

OPTION_CHAIN = "/market/option-chain"

HISTORICAL_DATA = "/market/history"