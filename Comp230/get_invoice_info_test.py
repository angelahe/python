import unittest
from get_invoice_info import GetInvoiceInfo

class TestGetInvoiceInfo(unittest.TestCase):

    def test_new(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.invoiceID, 1000)
        self.assertEqual(newInvoiceInfo.fileName, "CM2_1.xlsx")

    def test_file_exists_true(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.check_file_exists(), True)

    def test_file_exists_false(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CMX.xlsx")
        self.assertNotEqual(newInvoiceInfo.check_file_exists, True, FileNotFoundError)

    def test_check_for_sheets(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.check_for_sheets(), True)

    def test_check_for_sheets_fail(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM.xlsx")
        self.assertEqual(newInvoiceInfo.check_for_sheets(), False)

    def test_get_invoice_info(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_invoice_info(), True)
        self.assertEqual(newInvoiceInfo.customerID, 1100)
        self.assertEqual(str(newInvoiceInfo.invoiceDate), '2019-01-01 00:00:00')
        #print(f'date is {newInvoiceInfo.invoiceDate}')

    def test_get_invoice_info_fails(self):
        newInvoiceInfo = GetInvoiceInfo(9999, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_invoice_info(), False)
    
    def test_get_customer_info(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_invoice_info(), True)
        self.assertEqual(newInvoiceInfo.get_customer_info(), True)
        self.assertEqual(newInvoiceInfo.customerName, 'Linda Mendoza')
        self.assertEqual(newInvoiceInfo.customerAddress, '123 Apple St SW Calgary AB')
        self.assertEqual(newInvoiceInfo.customerPhone, '555-123-4567')
        self.assertEqual(newInvoiceInfo.customerContact, 'Linda')

    def test_get_customer_info_fails(self):
        newInvoiceInfo = GetInvoiceInfo(2800, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_customer_info(), False)

    def test_get_line_items(self):
        newInvoiceInfo = GetInvoiceInfo(1001, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_line_items(), True)
        self.assertNotEqual(newInvoiceInfo.invoiceItems, [])
        self.assertEqual(newInvoiceInfo.invoiceItems[0]['productNum'], 17)
        self.assertEqual(newInvoiceInfo.invoiceItems[0]['units'], 3)
        self.assertEqual(newInvoiceInfo.invoiceItems[1]['productNum'], 18)
        self.assertEqual(newInvoiceInfo.invoiceItems[1]['units'], 2)
        self.assertEqual(newInvoiceInfo.invoiceItems[1]['description'], 'UX Design')
        self.assertEqual(newInvoiceInfo.invoiceItems[1]['unitCost'], 45)
        self.assertEqual(newInvoiceInfo.invoiceItems[1]['totalCost'], 90) 

    def test_get_line_items_fails(self):
        newInvoiceInfo = GetInvoiceInfo(2801, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.get_line_items(), False)

    def test_load_product_info(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.load_product_info(), True)
        self.assertNotEqual(newInvoiceInfo.products, [])

    #def test_load_product_info_fails(self):

    def test_lookup_product_info(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.load_product_info(), True)
        result = newInvoiceInfo.lookup_product_info(18)
        self.assertEqual(result, {'productNum': 18, 'description': 'UX Design', 'unitCost': 45})
        

    def test_lookup_product_fails(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.load_product_info(), True)
        result = newInvoiceInfo.lookup_product_info(19)
        self.assertEqual(result, False)
    
    def test_lookup_product_with_empty_productlist(self):
        newInvoiceInfo = GetInvoiceInfo(1000, "CM2_1.xlsx")
        self.assertEqual(newInvoiceInfo.lookup_product_info(18), False)

if __name__ == '__main__':
    unittest.main()
    
