"""this is added just to check online commit"""

class MyAccounts (object):
    """MyAccounts class:
takes an optional meaning full name as the constuctor argument"""

    FIX_WIDTH = 40
    def __init__ (self, name=''):
        """name: optional meaning ful string can be given as argument"""
        super ()
        self._name = name
        self._inc_dict = {}
        self._exp_dict = {}

    def __addToDict__ (dict_name, name, amount):
        assert type (dict_name) == dict, "First argument should be a dictionary type"
        amount = float (amount)
        assert type (name) == str
        assert amount >= 0, "Amount should be a NON-NEGATIVE number"
        dict_name [name] = amount

    def __addAmounts__ (dict_name):
        assert type (dict_name) == dict, "First argument should be a dictionary type"
        total = 0
        for value in dict_name.values():
            if type (value) == float:
                total += value
        return total

    def __removeFromDict__ (dict_name, name):
        assert type (dict_name) == dict, "First argument should be a dictionary type"
        assert type (name) == str
        amt = -1
        try:
            amt = dict_name.pop (name)
        except KeyError as k:
            raise NameError ('"' + name + '" not found in the particular\'s list')
        return amt

    def __displayDictDetails__ (dict_name):
        assert type (dict_name) == dict, "Argument should be a dictionary type"
        for key, val in dict_name.items():
            print ("%20s = %8.2f" % (key, val))
        print ("="*MyAccounts.FIX_WIDTH)
        print ("%20s = %8.2f\n" % ("TOTAL", MyAccounts.__addAmounts__(dict_name)))

    def getName (self):
        """returns the given name"""
        return _name

    def setName (self, name):
        """resets the name"""
        self._name = name

    def addIncome (self, inc_name, inc_amount):
        """inc_name: name of the income component (eg: salary, tax_refund etc...)"""
        MyAccounts.__addToDict__ (self._inc_dict, inc_name, inc_amount)

    def removeIncome (self, inc_name):
        """removes the passed income from the list and returns its current value"""
        amt = -1
        try:
            amt = MyAccounts.__removeFromDict__ (self._inc_dict, inc_name)
            print ("Income:", inc_name, " ==> Value:", amt, "(REMOVED)")
        except NameError:
            print ("No such INCOME :", inc_name)
        return amt

    def addExpense (self, exp_name, exp_amount):
        """exp_name: name of the expense (eg: bus_fare, tax_deducted etc...)
exp_amount: expense amount"""
        MyAccounts.__addToDict__ (self._exp_dict, exp_name, exp_amount)

    def removeExpense (self, exp_name):
        """remove the given expense from the list"""
        amt = -1
        try:
            amt = MyAccounts.__removeFromDict__ (self._exp_dict, exp_name)
            print ("Expense:", exp_name, " ==> Value:", amt, "(REMOVED)")
        except NameError:
            print ("No such EXPENSE :", exp_name)
        return amt

    def clearIncome (self):
        """clear all the income details from the list"""
        self._inc_dict.clear()

    def clearExpense (self):
        """clear all the expense details"""
        self._exp_dict.clear()

    def clearAll (self):
        """clear all income and expenses"""
        self.clearIncome()
        self.clearExpense()

    def totalIncome (self):
        """returns the sum of all income items"""
        return MyAccounts.__addAmounts__ (self._inc_dict)

    def totalExpense (self):
        """returns the sum of all expenses"""
        return MyAccounts.__addAmounts__ (self._exp_dict)

    def balance (self):
        """returns the cash balance (income - expense)"""
        return (self.totalIncome() - self.totalExpense())

    def save (self, file_name):
        """file_name: name of the file to which these details has to be saved"""
        assert type(file_name) == str, "'file_name' should be provided as a string argument"
        fSave = open (file_name, 'bw')
        import pickle,zlib
        pickStr = pickle.dumps (self)
        zippedStr = zlib.compress (pickStr)
        fSave.write (zippedStr)
        fSave.close()
        del pickle, zlib
        print ("Saved the current state of the object to '" + file_name + "'")

    def load (self, file_name, old_load=False):
        """file_name: pass the file from which the details has to be loaded
old_load: boolean value, if true, load will try to read the file as an old_version_file"""
        assert type(file_name) == str, "'file_name' should be provided as a string argument"
        assert type(old_load) == bool, "'old_load' should be a boolean value"
        fLoad = open (file_name, 'br')
        import pickle, zlib
        dataLoaded = ""
        zippedStr = ""
        if not old_load:
            zippedStr = fLoad.read()
            dataLoaded = zlib.decompress (zippedStr)
        else:
            dataLoaded = fLoad.read()
        tmpObj = pickle.loads (dataLoaded)
        try:
            self._name = tmpObj._name
        except AttributeError:
            self._name = ''
            print ("loading an old version of 'myAccMgr' module")
        self._inc_dict = dict (tmpObj._inc_dict)
        self._exp_dict = dict (tmpObj._exp_dict)
        fLoad.close()
        del pickle, zlib, tmpObj, zippedStr, dataLoaded
        print ("Successfully reloaded from '" + file_name + "'")

    def displayDetails (self):
        """display all the details"""
        print ()
        print (self._name.center (MyAccounts.FIX_WIDTH))
        print ("".center (MyAccounts.FIX_WIDTH, "="))
        self.displayIncomeDetails ()
        self.displayExpenseDetails ()
        print ("%20s : %8.2f\n" % ("BALANCE", self.balance()))

    def displayIncomeDetails (self):
        """display only the income details"""
        print ()
        print ("INCOME".center(MyAccounts.FIX_WIDTH, "="))
        MyAccounts.__displayDictDetails__ (self._inc_dict)

    def displayExpenseDetails (self):
        """display only expense details"""
        print ()
        print ("EXPENSE".center(MyAccounts.FIX_WIDTH, "="))
        MyAccounts.__displayDictDetails__ (self._exp_dict)

