from django.db import models

class UserTypeModel(models.Model):
    usertypeid = models.AutoField(primary_key=True)
    usertypename = models.CharField(default="", max_length=100)
    



class CampModel(models.Model):
    campid = models.AutoField(primary_key=True)
    campname = models.CharField(default="", max_length=400)
    location = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=400)
    phone = models.BigIntegerField(null=True)
    numberofrooms = models.IntegerField(default="", max_length=100)
    numberoffloors = models.IntegerField(default="", max_length=100)
    numberofBeds = models.IntegerField(default="", max_length=100)
    

class Floor(models.Model):
    floorid = models.AutoField(primary_key=True)
    floorno = models.CharField(default = "", max_length = 100)

class Flat(models.Model):
    flatid = models.AutoField(primary_key=True)
    flatnumber = models.CharField(default="", max_length=100)
    floorno = models.ForeignKey(Floor, null = True, on_delete = models.CASCADE)

class RoomTypeModel(models.Model):
    roomtypeid = models.AutoField(primary_key=True)
    roomtypename = models.CharField(default="", max_length=100)
    occupancy = models.IntegerField(default="", max_length=100)

class RoomModel(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomnumber = models.IntegerField(default="", max_length=100)
    roomtypeid = models.ForeignKey(RoomTypeModel, null=True, on_delete=models.CASCADE)
    flatid = models.ForeignKey(Flat, null=True, on_delete=models.CASCADE)
    
class BedModel(models.Model):
    bedid = models.AutoField(primary_key=True)
    roomid = models.ForeignKey(RoomModel, null=True, on_delete=models.CASCADE)
    number = models.IntegerField(default = "", max_length = 100)

class ItemCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=100)
    number = models.IntegerField(null=True, blank=True)  # Allow null values for the number field

    def __str__(self):
        return self.ItemName   

class ItemModel(models.Model):
    itemid = models.AutoField(primary_key=True)
    itemname = models.CharField(default="", max_length=100)

class TransportationModel(models.Model):
    busid = models.AutoField(primary_key=True)
    busno = models.IntegerField(default="1")
    destination = models.CharField(default="", max_length=200)
    time = models.TimeField()
    campname = models.ForeignKey(CampModel, null=True, on_delete=models.CASCADE)
    
    def _str_(self):
        return f"Bus No: {self.busno}"

class LeaveTypeModel(models.Model):
    leavetypeid = models.AutoField(primary_key=True)
    leavetypename = models.CharField(default="", max_length=100)
    totalnoofdays = models.IntegerField(default="", max_length=100)


class HRManagerModel(models.Model):
    hrmanagerid = models.AutoField(primary_key=True)
    hrmanagername = models.CharField(default="", max_length=100)
    email = models.EmailField(default="", max_length=100)
    password = models.CharField(default="", max_length=100)

class MessModel(models.Model):
    messid = models.AutoField(primary_key=True)
    messcaptainname = models.CharField(default="", max_length=100)
    campid = models.ForeignKey(CampModel, null=True, on_delete=models.CASCADE)
    cuisine = models.CharField(default="", max_length=100)
    timingfrom = models.TimeField()
    timingto = models.TimeField()

class EmployeeModel(models.Model):
    employeeid = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=100)
    phone = models.BigIntegerField(null=True)
    dob = models.DateField()
    address = models.CharField(default=" ", max_length=400)
    nationality = models.CharField(default="", max_length=100)
    jobcategory = models.CharField(default="", max_length=100)
    passport = models.CharField(default="", max_length=100)
    passportexpiry = models.DateField()
    department = models.CharField(default="", max_length=100)
    bloodgroup = models.CharField(default="", max_length=100)
    diagnosisdiseases = models.CharField(default="", max_length=100)
    emergencymedicine = models.CharField(default="", max_length=100)
    emergencyphone = models.BigIntegerField(null=True)
    domesticaddress = models.CharField(default="", max_length=400)
    education = models.CharField(default="", max_length=100)
    email = models.EmailField(default="", max_length=100)
    password = models.CharField(default="", max_length=100)
    bedid = models.ForeignKey(BedModel, null=True, on_delete=models.CASCADE)
    itemid = models.ForeignKey(ItemModel, null=True, on_delete=models.CASCADE)
    busid = models.ForeignKey(TransportationModel, null=True, on_delete=models.CASCADE)
    floorid = models.ForeignKey(Floor, null=True, on_delete=models.CASCADE)
    roomid = models.ForeignKey(RoomModel, null=True, on_delete=models.CASCADE)
    Roomtype= models.ForeignKey(RoomTypeModel, null=True, on_delete=models.CASCADE)
    flatid= models.ForeignKey(Flat, null=True, on_delete=models.CASCADE)
    usertypeid = models.ForeignKey(UserTypeModel, null=True, on_delete=models.CASCADE)
    camp =  models.ForeignKey(CampModel, null=True, on_delete=models.CASCADE)
    totalNoOfLeave = models.IntegerField(default='30')
    
class Login(models.Model):

    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    emp_id = models.ForeignKey(EmployeeModel, null = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.username

class LeaveRequestModel(models.Model):
    requestid = models.AutoField(primary_key=True)
    reason = models.CharField(default="", max_length=400)
    numberofdays = models.IntegerField()
    fromdate = models.DateField()
    todate = models.DateField()
    approvalstatus = models.CharField(default="pending", max_length=100)
    employeeid = models.ForeignKey(EmployeeModel, null=True, on_delete=models.CASCADE)
    leavetypeid = models.ForeignKey(LeaveTypeModel, null=True, on_delete=models.CASCADE)

class StorageModel(models.Model):
    storageid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey(EmployeeModel, null=True, on_delete=models.CASCADE)
    fromdate = models.DateTimeField()
    todate = models.DateTimeField()
    items = models.CharField(default="", max_length=100)

class LeaveStatusModel(models.Model):
    leavestatusid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey(EmployeeModel, null=True, on_delete=models.CASCADE)
    leavetypeid = models.ForeignKey(LeaveTypeModel, null=True, on_delete=models.CASCADE)
    remainingdays = models.IntegerField(default="", max_length=100)
    numberofdays = models.ForeignKey(LeaveRequestModel, null=True, on_delete=models.CASCADE)

class ComplaintModel(models.Model):
    complaintid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey(EmployeeModel, null=True, on_delete=models.CASCADE)
    complaint_against = models.CharField(default="", max_length=100)
    reason = models.CharField(default="", max_length=400)
    date = models.DateField()
    
    

