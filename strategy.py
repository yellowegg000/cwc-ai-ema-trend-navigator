# CWC AI EMA Trend Navigator
# Example strategy logic (educational only)

def long_signal(price_above_ema50, ema50_above_ema200, rsi, volume_above_average):
    return (
        price_above_ema50
        and ema50_above_ema200
        and rsi > 55
        and volume_above_average
    )

def short_signal(price_below_ema50, ema50_below_ema200, rsi, volume_above_average):
    return (
        price_below_ema50
        and ema50_below_ema200
        and rsi < 45
        and volume_above_average
    )

# Risk Management
RISK_PER_TRADE = 0.01
MAX_PORTFOLIO_EXPOSURE = 0.05

print("CWC AI EMA Trend Navigator Example")
