binder_UI_out = widgets.Output()
binder_out = widgets.Output()
binder_button = create_submit_button()
binder_download_button = create_download_button()
binder_refresh_button = create_refresh_button()

@binder_button.on_click
def on_click(b):
    pass

binder_lender = widgets.RadioButtons(
    options=['Wells Fargo', 'Bank of America (Private Wealth)', 'Bank of America', 'JPMorgan Chase', 'Ocean Bank', 'Other'],
    value='Ocean Bank',
    description='Lender:',
    disabled=False
)

binder_type = widgets.RadioButtons(
    options=['Middle Market', 'Construction Loan', 'Bank Loan', 'Loan Modification', 'ABL Loan', 'Art Loan'],
    value='Bank Loan',
    description='Loan Type:',
    disabled=False
)


tab1 = VBox(children=[HBox(children=[binder_lender, binder_type])])
tab2 = VBox(children=[HBox(children=[])])
tab = widgets.Tab(children=[tab1, tab2])
tab.set_title(0, 'Loan Details')
tab.set_title(1, 'Custom Templates')
HBox_binder = HBox(children=[binder_button, binder_refresh_button, binder_download_button])
VBox_binder = VBox(children=[tab, HBox_binder ])
with binder_UI_out:
    display(VBox_binder)
    
binder_UI_out