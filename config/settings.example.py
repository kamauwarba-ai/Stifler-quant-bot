"""
Example configuration template for MT5 Trading Bot
Copy and customize this file for your setup
"""

EXAMPLE_CONFIG = {
    # ============ MT5 CONNECTION ============
    'MT5': {
        # Your MT5 login number
        'login': 1234567,
        
        # Your MT5 password
        'password': 'your_password',
        
        # Broker server name (e.g., "FxPro-MT5", "Pepperstone-MT5")
        'server': 'your_broker_server',
        
        # Optional: path to MT5 terminal
        'path': None,
    },
    
    # ============ TRADING PAIRS ============
    'PAIRS': [
        'EURUSD',  # EUR/USD
        'GBPUSD',  # GBP/USD
        'USDJPY',  # USD/JPY
        'AUDUSD',  # AUD/USD
    ],
    
    # ============ TIMEFRAMES ============
    'TIMEFRAMES': {
        'M5': 5,      # 5 minutes
        'M15': 15,    # 15 minutes
        'M30': 30,    # 30 minutes
        'H1': 60,     # 1 hour
        'H4': 240,    # 4 hours
    },
    
    # ============ RISK MANAGEMENT ============
    'RISK': {
        # Risk X% of account per trade
        'risk_per_trade_percent': 2.0,
        
        # Use fixed lot size instead of risk-based sizing?
        'use_fixed_lot': False,
        'fixed_lot_size': 0.1,
        
        # Stop trading if account loses X%
        'max_drawdown_percent': 25.0,
        
        # Max number of open positions at same time
        'max_concurrent_positions': 5,
    },
    
    # ============ POSITION MANAGEMENT ============
    'POSITION': {
        # Stop loss distance in pips
        'stop_loss_pips': 50,
        
        # Take profit distance in pips
        'take_profit_pips': 100,
        
        # Enable trailing stop loss?
        'use_trailing_stop': False,
        'trailing_stop_pips': 20,
        
        # Close position when opposite signal appears?
        'close_on_opposite_signal': True,
        
        # Auto-close positions after X hours
        'auto_close_hours': 24,
    },
    
    # ============ EXECUTION RULES ============
    'EXECUTION': {
        # Enable/disable trading
        'enabled': True,
        
        # DEMO MODE: Set to True for testing, False for LIVE TRADING
        'demo_mode': True,
        
        # Only trade signals with strength >= X (0.0 to 1.0)
        'min_signal_strength': 0.6,
        
        # Max acceptable slippage in pips
        'max_slippage_pips': 5,
    },
    
    # ============ NOTIFICATIONS ============
    'ALERTS': {
        # Discord webhook URL (get from Discord server settings)
        'discord_webhook': None,  # 'https://discordapp.com/api/webhooks/...'
        
        # Email address for alerts
        'email': None,  # 'your_email@gmail.com'
        
        # Telegram bot token (get from BotFather)
        'telegram_token': None,  # 'YOUR_BOT_TOKEN'
        
        # Telegram chat ID
        'telegram_chat_id': None,  # 'YOUR_CHAT_ID'
        
        # Alert preferences
        'notify_on_trade': True,      # Notify when trades open/close
        'notify_on_signal': True,     # Notify on new signals
        'notify_on_error': True,      # Notify on errors
    },
    
    # ============ DATA & LOGGING ============
    'DATA': {
        # Save analysis results to CSV?
        'save_results': True,
        
        # Directory to save results
        'results_dir': 'data/results',
        
        # File to log all trades
        'trades_log': 'data/logs/trades.csv',
        
        # File to log errors
        'errors_log': 'data/logs/errors.log',
        
        # Number of historical bars to load for analysis
        'max_bars_to_load': 500,
    },
    
    # ============ SCHEDULER ============
    'SCHEDULER': {
        # Enable/disable scheduler?
        'enabled': True,
        
        # Run trading cycle every X minutes
        'interval_minutes': 5,
        
        # Start trading at this hour (24-hour format)
        'start_hour': 0,
        
        # Stop trading at this hour (24-hour format)
        'end_hour': 23,
        
        # Trade on these days (0=Monday, 4=Friday, skip 5-6 for weekends)
        'trading_days': [0, 1, 2, 3, 4],
    },
}


# ============ SETUP INSTRUCTIONS ============
"""
QUICK START:

1. Copy config/settings.py.example → config/settings.py
2. Update with your credentials:
   - MT5 login, password, server
   - Trading pairs
   - Risk settings
   
3. (Optional) Setup notifications:
   - Discord: https://discord.com/developers/applications
   - Telegram: Message @BotFather on Telegram
   - Email: Gmail app password (not regular password)

4. Run in DEMO MODE first:
   - Set 'demo_mode': True in EXECUTION
   - python main.py
   
5. After testing, set to LIVE MODE:
   - Set 'demo_mode': False in EXECUTION
   - ⚠️ CAUTION: This trades with real money

RISK MANAGEMENT TIPS:

- Start with 1-2% risk per trade
- Use smaller lot sizes on first trades
- Test strategy in demo for at least 1 week
- Monitor bot regularly (don't set and forget)
- Set max drawdown to 20-25% for safety
- Keep max concurrent positions to 3-5

SIGNAL STRENGTH GUIDE:

- 0.0-0.3: Very weak signals (skip)
- 0.3-0.6: Weak signals (risky)
- 0.6-0.8: Good signals (recommended)
- 0.8-1.0: Strong signals (best quality)

POSITION SIZING:

Risk-Based (Recommended):
- If SL is 50 pips away
- Account is $10,000
- Risk is 2% = $200
- Position size = $200 / (50 pips * 10) = 0.4 lot

Fixed Sizing:
- Always trade same lot size (0.1, 0.5, 1.0)
- Simpler but less risk control

TRADING HOURS:

Forex is open 24/5:
- Sunday 5 PM - Friday 5 PM EST
- Adjust start_hour and end_hour accordingly
- Consider low-liquidity hours (weekends, holidays)

TROUBLESHOOTING:

Bot not trading?
- Check 'demo_mode' setting
- Verify trading pairs are valid
- Check trading hours/days
- Verify signal strength threshold

High fees/slippage?
- Trade during peak hours (8-16 UTC)
- Use higher timeframes (avoid M5)
- Check max_slippage_pips setting

Need help?
- Check logs in data/logs/
- Read README.md
- Test in demo mode
"""
