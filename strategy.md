# Trading Strategy Details

## Objective

Capture medium- to long-term trends in cryptocurrency perpetual futures using objective technical indicators and disciplined risk management.

## Supported Markets

- BTC/USDT
- ETH/USDT
- SOL/USDT
- Other high-liquidity perpetual futures

## Indicators

- EMA 50
- EMA 200
- RSI (14)
- ATR (14)
- Volume Moving Average (20)

## Entry Conditions

### Long

- EMA 50 > EMA 200
- RSI > 55
- Price closes above EMA 50
- Volume above 20-period average

### Short

- EMA 50 < EMA 200
- RSI < 45
- Price closes below EMA 50
- Volume above 20-period average

## Exit Conditions

- Stop Loss: 1.5 × ATR
- Take Profit: 3 × ATR
- Optional trailing stop after reaching 2 × ATR profit

## Position Sizing

Risk no more than 1% of account equity per trade.

## Suitable Market Conditions

- Strong uptrends
- Strong downtrends
- Moderate volatility
- High liquidity
