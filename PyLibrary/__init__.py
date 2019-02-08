# margin calculator

# wholesale
def marg_calc(wls_or_rtl, start_price, end_price):
    """
    User selects wholesale ('w') or retail ('r'), enters a start price and an
    end price and the margin is returned.
    
    Example:
        
    margin_pct = marg_calc('w', 10, 15.51)
    margin_pct
    """
    if wls_or_rtl == 'w':
        margin = '{0:0.2f}'.format((1 - start_price/end_price)*100)
    else:
        margin = '{0:0.2f}%'.format((1 - start_price/end_price)*100)
    return margin
    


	
    






