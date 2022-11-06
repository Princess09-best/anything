charge_inc = 0
rate =0
payableTax = 0
Cumm_inc=0
cumm_tax= 0
def Taxcalc(gross_inc):
    Tax1=0
    Tax2=0.05
    Tax3=0.1
    Tax4=0.175
    Tax5=0.25
    Tax6=0.3

    total_tax = 0
    net_income = 0

    ch_income1 = 365
    ch_income2 = 110
    ch_income3 = 130
    ch_income4 = 3000
    ch_income5 = 16395
    ch_income6 = 20000

    if gross_inc <=ch_income1:
        net_income=gross_inc
        
    if gross_inc > ch_income1:
        taxable_income=gross_inc - ch_income1
        
    if taxable_income<= 110:
        taxA = taxable_income *Tax2
        net_income = gross_inc - taxA

    elif taxable_income > 110:
        net_income = gross_inc-((Tax2 *110))
        difference = taxable_income -110

        if difference<130:
            TaxB = difference*Tax3
            net_income=net_income-TaxB

        if difference > 130:
            net_income = gross_inc-((Tax3 *130))
            difference = taxable_income -130
            

