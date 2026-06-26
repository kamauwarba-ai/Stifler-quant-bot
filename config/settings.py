"""
Configuration settings for MT5 Trading Bot
"""

CONFIG = {
    # MT5 Connection
    'MT5': {
        'login': None,  # Set your MT5 login
        'password': None,  # Set your MT5 password
        'server': None,  # Set your broker server
        'path': None,  # Optional: path to MT5 terminal
    },
    
    # Trading Pairs
    'PAIRS': ['EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD'],
    
    # Timeframes (in minutes)
    'TIMEFRAMES': {
        'M5': 5,
        'M15': 15,
        'M30': 30,
        'H1': 60,
        'H4': 240,
    },
    
    # Risk Management
    'RISK': {
        'risk_per_trade_percent': 2.0,  # Risk 2% of account per trade
        'use_fixed_lot': False,  # Set to True for fixed lot size
        'fixed_lot_size': 0.1,  # If use_fixed_lot is True
        'max_drawdown_percent': 25.0,  # Stop trading if drawdown exceeds this
        'max_concurrent_positions': 5,  # Maximum open positions at once
    },
    
    # Position Management
    'POSITION': {
        'stop_loss_pips': 50,  # Stop loss distance in pips
        'take_profit_pips': 100,  # Take profit distance in pips
        'use_trailing_stop': False,  # Enable trailing stop loss
        'trailing_stop_pips': 20,  # Trailing stop distance
        'close_on_opposite_signal': True,  # Close position on opposite signal
        'auto_close_hours': 24,  # Auto-close positions after N hours
    },
    
    # Execution Rules
    'EXECUTION': {
        'enabled': True,  # Enable/disable live trading
        'demo_mode': True,  # Set to False for live trading (CAUTION!)
        'min_signal_strength': 0.6,  # Only trade signals with strength >= this
        'max_slippage_pips': 5,  # Max acceptable slippage
    },
    
    # Notifications
    'ALERTS': {
        'discord_webhook': None,  # Set your Discord webhook URL
        'email': None,  # Set your email for alerts
        'telegram_token': None,  # Set Telegram bot token
        'telegram_chat_id': None,  # Set Telegram chat ID
        'notify_on_trade': True,
        'notify_on_signal': True,
        'notify_on_error': True,
    },
    
    # Data & Logging
    'DATA': {
        'save_results': True,
        'results_dir': 'data/results',
        'trades_log': 'data/logs/trades.csv',
        'errors_log': 'data/logs/errors.log',
        'max_bars_to_load': 500,  # Historical bars to load for analysis
    },
    
    # Scheduler (run bot on intervals)
    'SCHEDULER': {
        'enabled': True,
        'interval_minutes': 5,  # Run analysis every 5 minutes
        'start_hour': 0,  # 24-hour format (0-23)
        'end_hour': 23,
        'trading_days': [0, 1, 2, 3, 4],  # Monday=0, Friday=4 (skip weekends)
    },
}
