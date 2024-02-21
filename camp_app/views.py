from multiprocessing import context
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404

# Create your views here.
from django.db.models import Max
from .models import *

def index(request):
    return render(request,'./camp_app/index.html')

def employeeProfileView(request):
    profile_view = EmployeeModel.objects.all()
    context = {'profile' : profile_view}
    
    return render(request,'./camp_app/employeeProfileView.html', context)

def campBossEmployeeview(request):
    profile_view = EmployeeModel.objects.all()
    context = {'profile' : profile_view}
    
    return render(request,'./camp_app/campBossEmployeeview.html', context)


def employeeViewBusSchedule(request):
    bus_schedule = TransportationModel.objects.all()
    context = {'bus' : bus_schedule}
    
    return render(request, './camp_app/employeeBusScheduleView.html', context)


def messCaptainViewMessSchedule(request):
    mess_schedule = MessModel.objects.all()
    context = {'mess' : mess_schedule}
    
    return render(request, './camp_app/messCaptainViewMessSchedule.html', context)


def messCaptainViewLeaveSchedule(request):
    leave_schedule = LeaveRequestModel.objects.all()
    context = {'leave' : leave_schedule}
    
    return render(request, './camp_app/messCaptainViewLeaveStatus.html', context)



def hrAddFloor(request):
    context = {}
    
    if request.method == 'POST':
        floor = request.POST.get('floorNumber')
        
        if Floor.objects.filter(floorno=floor).exists():
            context['error'] = "Floor already exists"
        else:
            temp = Floor(floorno=floor)
            temp.save()
            context['success'] = True
        
    return render(request, './camp_app/hrAddFloor.html', context)



def hrAddFlat(request):
    if request.method=="POST":
        floorid=request.POST.get("floorNumber")
        floor=Floor.objects.get(floorid=floorid)
        flatno=request.POST.get("flatNumber")
        new=Flat.objects.create(flatnumber=flatno,floorno=floor)
        new.save()
        return redirect('./camp_app/hrAddFlats.html')
    else:
        displayFloor = Floor.objects.all()
        return render(request, './camp_app/hrAddFlats.html', {"Floor":displayFloor})







def hrCreateRoomType(request):
    
    if request.method == 'POST':
        type = request.POST.get('roomtype')
        number = request.POST.get('occupancy')
        
        RoomTypeModel(roomtypename=type, occupancy=number).save()
        return render(request, './camp_app/hrAddFloor.html')
    else:
        return render(request, './camp_app/hrAddRoomType.html')
    
    

def hrAddRoom(request):
    
    if request.method == "POST":
        flatid = request.POST["flatNumber"]
        flat = Flat.objects.get(flatid=flatid)
        roomno = request.POST['roomNumber']
        roomtypeid = request.POST["roomtype"]
        roomtype = RoomTypeModel.objects.get(roomtypeid=roomtypeid)
        new = RoomModel.objects.create(roomnumber=roomno,flatid=flat,roomtypeid=roomtype)
        new.save()
        return redirect('./camp_app/hrAddRoom.html')
    else:
        displayFlat = Flat.objects.all()
        displayRoomType = RoomTypeModel.objects.all()
        return render(request, './camp_app/hrAddRoom.html',{"Flat":displayFlat, "RoomType": displayRoomType})


def hrAddBed(request):
    if request.method == "POST":
        roomid = request.POST["roomNumber"]
        room = RoomModel.objects.get(roomid=roomid)
        bedNumber = request.POST['bedNumber']
        new = BedModel.objects.create(roomid=room, number=bedNumber)
        new.save()
        return redirect("./camp_app/hrAddBed.html")
    else:
        displayRoom = RoomModel.objects.all()
        return render(request, "./camp_app/hrAddBed.html", {"Room":displayRoom})
    

def hrAddCamp(request):
    context = {}
    
    if request.method == 'POST':
        camp = request.POST.get('camp')
        locationname = request.POST.get('currentLocation')
        addressname = request.POST.get('currentAddress')
        phoneno = request.POST.get('contact')
        noofrooms = request.POST.get('roomnumber')
        nooffloors = request.POST.get('floornumber')
        noofBeds = request.POST.get('bednumber')
        
        if CampModel.objects.filter(campname = camp, location = locationname, address = addressname, phone = phoneno, numberofrooms = noofrooms, numberoffloors = nooffloors, numberofBeds = noofBeds).exists():
            context['error'] = "Camp already exists"
        else:
            temp = CampModel(campname = camp, location = locationname, address = addressname, phone = phoneno, numberofrooms = noofrooms, numberoffloors = nooffloors, numberofBeds = noofBeds)
            temp.save()
            context['success'] = True
    
    return render(request, './camp_app/hrAddCamp.html', context)





def hrEmployeeLeaveStatus(request):
    # Fetch all leave status records
    leave_statuses = LeaveStatusModel.objects.all()
    context={'leave_status':leave_statuses}

    # Render the template with leave status data
    return render(request, './camp_app/hrEmployeeLeaveStatus.html',context)


def employeeLeaveRequestView(request):
    render(request, './camp_app/employeeLeaveRequestView.html')
    

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LeaveRequestModel, LeaveTypeModel, EmployeeModel
from django.contrib.auth.decorators import login_required  # If using Django's authentication system

@login_required
def employeeLeaveRequest(request):
    
    
    if request.method == 'POST':
        
        id = request.session['id']
        print(id)
        employee = EmployeeModel.objects.get(employeeid=id)
        reason = request.POST.get('reason')
        print("Reason received:", reason)

        numberofdays = int(request.POST.get('numberofdays', 0))  # Default to 0 if not provided

        fromdate = request.POST.get('fromDate')
        todate = request.POST.get('toDate')
        leavetypeid = request.POST.get('leaveType')

     
        leavetype = LeaveTypeModel.objects.get(leavetypeid=leavetypeid)

        # Create and save the leave request
        leave_request = LeaveRequestModel(
            reason=reason,
            numberofdays=numberofdays,
            fromdate=fromdate,
            todate=todate,
            employeeid=employee,
            leavetypeid=leavetype,
           
        )
        leave_request.save()
        
        return redirect('employeeLeaveRequest')  # Assuming you have a URL named 'leave_request_success'
    
    # If not POST, or the form is invalid, show the form again
    leave_types = LeaveTypeModel.objects.all()  # Assuming you want to show leave types in your form
    context = {
        'leave_types': leave_types,
    }
    return render(request, 'camp_app/employeeLeaveRequest.html', context)

def employeeComplaintPortal(request):
    if request.method == "POST":
        id = request.session["id"]
        employee = EmployeeModel.objects.get(employeeid = id)
        reason = request.POST.get("reason")
    
        complaint_against = request.POST.get('complaint_person')

        date = request.POST.get("date")
        
       
        new_complaint = ComplaintModel.objects.create(
    employeeid=employee,
    reason=reason,
    date=date,
    complaint_against=complaint_against
)


        new_complaint.save()
        return redirect("employeeComplaintPortal")
    else:
        displayEmployee = EmployeeModel.objects.all()
        return render(request, './camp_app/employeeComplaintPortal.html', {"Person":displayEmployee})



def campBossBase(request):
    return render(request,'./camp_app/campBossBase.html')


def AddEmployee(request):
    
    camps = CampModel.objects.all() 
    buses = TransportationModel.objects.all()
    floors = Floor.objects.all()
    flats = Flat.objects.all()
    rooms = RoomModel.objects.all()
    beds = BedModel.objects.all()
    items = ItemModel.objects.all()
    roomtype = RoomTypeModel.objects.all()
    usertype = UserTypeModel.objects.all()
    # This will be a list of item IDs
   
  
    context = {'camps': camps, "buses": buses,'floors':floors,'flats':flats,'beds':beds,'rooms':rooms,'categories':items,'roomtype':roomtype,'usertype':usertype}

    if request.method == 'POST':
        # Basic field extraction
        name = request.POST.get('name')
        phone = request.POST.get('phone', 0)  # Providing a default value if not found
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        nationality = request.POST.get('nationality')
        jobcategory = request.POST.get('jobcategory')
        passport = request.POST.get('passport')
        passportexpiry = request.POST.get('passportexpiry')
        department = request.POST.get('department')
        bloodgroup = request.POST.get('bloodgroup')
        diagnosisdiseases = request.POST.get('diagnosisdiseases')
        emergencymedicine = request.POST.get('emergencymedicine')
        emergencyphone = request.POST.get('emergencyphone', 0)
        domesticaddress = request.POST.get('domesticaddress')
        education = request.POST.get('education')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        camp = request.POST.get('camp')
        
        camp_id = request.POST.get('camp')
        if camp_id:
            camp = get_object_or_404(CampModel, pk=camp_id)
        else:
            camp = None

        # Fetch the Floor instance for the given floor ID
        floor_id = request.POST.get('floorNo')
        if floor_id:
            floorNo = get_object_or_404(Floor, floorid=floor_id)
        else:
            floorNo = None

        usertypeid  = request.POST.get('usertype')
        if usertypeid:
            usertype = get_object_or_404(UserTypeModel, usertypeid =usertypeid )
        else:
            usertype = None
        # Fetch the Flat instance for the given flat ID
        flat_id = request.POST.get('flatNo')
        if flat_id:
            flatNo = get_object_or_404(Flat, flatid=flat_id)
        else:
            flatNo = None

        # Fetch the RoomModel instance for the given room ID
        room_id = request.POST.get('RoomNo')
        if room_id:
            roomNo = get_object_or_404(RoomModel, roomid=room_id)
        else:
            roomNo = None

        # Fetch the TransportationModel instance for the given bus ID
        bus_id = request.POST.get('busNo')
        if bus_id:
            busNo = get_object_or_404(TransportationModel, pk=bus_id)
        else:
            busNo = None
       
        item_id = request.POST.get('itemNo')
        itemNo = get_object_or_404(ItemModel, pk=item_id) if item_id else None
       
        room_type_id = request.POST.get('roomTypeNo')
        roomTypeNo = get_object_or_404(RoomTypeModel, pk=room_type_id) if room_type_id else None
       
        bed_id = request.POST.get('bedNo')
        bedNo = None  # Default to None
        if bed_id:  # Check if bed_id is not empty
            try:
                bedNo = BedModel.objects.get(pk=bed_id)  # Try to fetch the BedModel instance
            except BedModel.DoesNotExist:
                # If no BedModel with the given ID exists, you can either set bedNo to None or handle the error as you see fit
                pass
       
        
        
        un = email
        pwd = password
        
        ul = Login(username = email,password = password)
        ul.save()
        employeeid= Login.objects.all().aggregate(Max('id'))['id__max']
        
        new_employee = EmployeeModel(
            employeeid = employeeid,
                name=name,
                phone=phone,
                dob=dob,
                address=address,
                nationality=nationality,
                jobcategory=jobcategory,
                passport=passport,
                passportexpiry=passportexpiry,
                department=department,
                bloodgroup=bloodgroup,
                diagnosisdiseases=diagnosisdiseases,
                emergencymedicine=emergencymedicine,
                emergencyphone=emergencyphone,
                domesticaddress=domesticaddress,
                education=education,
                email=email,
                password=password,
                camp=camp,
                bedid=bedNo,
                floorid=floorNo,
                flatid=flatNo,
                roomid=roomNo,
                itemid=itemNo,
                Roomtype = roomTypeNo,
                busid=busNo,
                usertypeid = usertype,
            )
        new_employee.save()
        
       

        
    return render(request, './camp_app/campBossAddEmployee.html',context)


def login_view(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user_type = request.POST.get('user_type')

        login_data = Login.objects.filter(username=username,password = password)

        # Redirect users based on user type
        if len(login_data) == 1:
            # creating session for username

            request.session['user'] = login_data[0].username
            request.session['id'] = login_data[0].id


            # context1 ={'uname':request.session['user']}

            return redirect(employeeLeaveRequest)
          # Assuming 'messcaptainHome' is the name of the mess captain home page URL pattern

    return render(request, './camp_app/login.html')



    def index(request):
      return render(request, './camp_app/index.html') 



def login_view(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user_type = request.POST.get('user_type')

        login_data = Login.objects.filter(username=username,password = password)

        # Redirect users based on user type
        if len(login_data) == 1:
            # creating session for username

            request.session['user'] = login_data[0].username
            request.session['id'] = login_data[0].id


            # context1 ={'uname':request.session['user']}

            return redirect('./camp_app/employeeLeaveRequest.html')
          # Assuming 'messcaptainHome' is the name of the mess captain home page URL pattern

    return render(request, './camp_app/login.html')

def hr_login_view(request):
    if request.method == 'POST':
        # Handle form submission for login
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if email and password match the specified values
        if email == 'hr@gmail.com' and password == '123':
            # If valid, redirect to HR home page
            return redirect('hrHome')  # Assuming 'hrHome' is the name of the URL pattern for HR home
        else:
            # If email or password is incorrect, display error message
            error_message = 'Invalid email or password'
            return render(request, './camp_app/hr_login.html', {'error_message': error_message})
    else:
        # If GET request, render the login page
        return render(request, './camp_app/hr_login.html')



def hr_home_view(request):
    # Add any necessary logic here
    return render(request, './camp_app/hrHome.html')



def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        pass  # Replace this with your actual login logic

    return render(request, './camp_app/login.html')

def mess_captain_home_view(request):
    # Add any additional logic here
    return render(request, './camp_app/messCaptainHome.html')


def hrAddCamp(request):
    if request.method == 'POST':
        camp_name = request.POST.get('camp')
        contact_no = request.POST.get('contact')
        location = request.POST.get('currentLocation')
        address = request.POST.get('currentAddress')
        num_rooms = request.POST.get('roomnumber')
        num_floors = request.POST.get('floornumber')
        num_beds = request.POST.get('bednumber')

        # Create a new CampModel object and save it to the database
        camp = CampModel.objects.create(
            campname=camp_name,
            location=location,
            address=address,
            phone=contact_no,
            numberofrooms=num_rooms,
            numberoffloors=num_floors,
            numberofBeds=num_beds
        )

        # Optionally, you can perform additional validation or checks here
        
        # Return a success message or redirect to another page
        return HttpResponse("Camp added successfully!")  # Placeholder response, adjust as needed
    else:
        # Render the form template if it's a GET request
        return render(request, './camp_app/hrAddCamp.html')
def add_camp_boss_view(request):
    if request.method == 'POST':
        # Handle form submission
        # Get form data from the request
        user_type = request.POST.get('userType')
        name = request.POST.get('name')
        camp_name = request.POST.get('campName')
        contact_no = request.POST.get('contactNo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Add more fields as needed

        # Create a new CampBoss object and save it to the database
        camp_boss = EmployeeModel.objects.create(
            user_type=user_type,
            name=name,
            camp_name=camp_name,
            contact_no=contact_no,
            email=email,
            password=password,
            # Add more fields as needed
        )
        # Redirect to a success page or another URL
        return HttpResponseRedirect('/success/')  # Redirect to a success page
    else:
        # Fetch camp names from the database
        camps = CampModel.objects.all()
        context = {'camps': camps}
        return render(request, './camp_app/hrAddCampBoss.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ItemCategory  # Assuming ItemCategory is the correct model
from django.http import HttpResponse

def AddItemCategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        # Make sure to use the correct field name when checking if the category already exists
        if ItemCategory.objects.filter(ItemName=category_name).exists():
            messages.error(request, "This category already exists!")
        else:
            # Use the correct field name when creating a new ItemCategory object
            ItemCategory.objects.create(ItemName=category_name)
            messages.success(request, "Item added successfully!")
        return redirect('campBossAddCategory')  # Ensure this named URL is correctly defined in your urls.py

    return render(request, './camp_app/campBossAddCategory.html')


def add_item(request):
    categories = ItemCategory.objects.all()  # Query all categories from the database

    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        category_id = request.POST.get('category')  # Get the selected category ID from the form

        # Check if the selected category exists
        if ItemCategory.objects.filter(pk=category_id).exists():
            category = ItemCategory.objects.get(pk=category_id)

            # Create a new ItemModel instance with the provided item name and selected category
            new_item = ItemModel.objects.create(itemname=item_name, category=category)

            # Display a success message
            messages.success(request, 'Item added successfully!')
            return redirect('campBossAdditem')  # Redirect back to the same page after adding an item

        else:
            messages.error(request, 'Invalid category selected!')

    return render(request, './camp_app/campBossAdditems.html', {'categories': categories})




def campBossHomeView(request):
    # Your view logic here
    return render(request, './camp_app/campBossHome.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import EmployeeModel, CampModel, Floor, Flat, RoomModel, BedModel, TransportationModel, ItemModel, RoomTypeModel, UserTypeModel

def AddCampBoss(request):
    # Retrieve all necessary data from the database
    camps = CampModel.objects.all() 
    buses = TransportationModel.objects.all()
    floors = Floor.objects.all()
    flats = Flat.objects.all()
    rooms = RoomModel.objects.all()
    beds = BedModel.objects.all()
    items = ItemModel.objects.all()
    roomtypes = RoomTypeModel.objects.all()
    usertypes = UserTypeModel.objects.all()

    # Context dictionary to pass data to the template
    context = {
        'camps': camps,
        'buses': buses,
        'floors': floors,
        'flats': flats,
        'rooms': rooms,
        'beds': beds,
        'items': items,
        'roomtypes': roomtypes,
        'usertypes': usertypes
    }

    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        nationality = request.POST.get('nationality')
        jobcategory = request.POST.get('jobcategory')
        passport = request.POST.get('passport')
        passportexpiry = request.POST.get('passportexpiry')
        department = request.POST.get('department')
        bloodgroup = request.POST.get('bloodgroup')
        diagnosisdiseases = request.POST.get('diagnosisdiseases')
        emergencymedicine = request.POST.get('emergencymedicine')
        emergencyphone = request.POST.get('emergencyphone')
        domesticaddress = request.POST.get('domesticaddress')
        education = request.POST.get('education')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Get selected items from dropdown menus
        camp_id = request.POST.get('camp')
        camp = get_object_or_404(CampModel, pk=camp_id) if camp_id else None

        floor_id = request.POST.get('floorNo')
        floor = get_object_or_404(Floor, floorid=floor_id) if floor_id else None

        flat_id = request.POST.get('flatNo')
        flat = get_object_or_404(Flat, flatid=flat_id) if flat_id else None

        # Add similar code to get selected items for RoomType, Room, Bed, Bus, Item, UserType

        # Create a new user instance
        user = User.objects.create_user(username=email, email=email, password=password)

        # Create a new EmployeeModel instance and set its attributes
        new_employee = EmployeeModel(
            name=name,
            phone=phone,
            dob=dob,
            address=address,
            nationality=nationality,
            jobcategory=jobcategory,
            passport=passport,
            passportexpiry=passportexpiry,
            department=department,
            bloodgroup=bloodgroup,
            diagnosisdiseases=diagnosisdiseases,
            emergencymedicine=emergencymedicine,
            emergencyphone=emergencyphone,
            domesticaddress=domesticaddress,
            education=education,
            email=email,
            user=user,  # Associate the user with the employee
            camp=camp,
            floorid=floor,
            flatid=flat,
            # Assign selected items to their respective fields
            # roomtypeid=roomtype,
            # roomid=room,
            # bedid=bed,
            # busid=bus,
            # itemid=item,
            # usertypeid=usertype
        )
        new_employee.save()  # Save the new employee instance to the database

        # Redirect to a success page or another view
        return redirect('success_url_name')

    return render(request, 'camp_app/hrAddCampBoss.html', context)


def AddEmployee(request):
    
    camps = CampModel.objects.all() 
    buses = TransportationModel.objects.all()
    floors = Floor.objects.all()
    flats = Flat.objects.all()
    rooms = RoomModel.objects.all()
    beds = BedModel.objects.all()
    items = ItemModel.objects.all()
    roomtype = RoomTypeModel.objects.all()
    usertype = UserTypeModel.objects.all()
    # This will be a list of item IDs
   
  
    context = {'camps': camps, "buses": buses,'floors':floors,'flats':flats,'beds':beds,'rooms':rooms,'categories':items,'roomtype':roomtype,'usertype':usertype}

    if request.method == 'POST':
        # Basic field extraction
        name = request.POST.get('name')
        phone = request.POST.get('phone', 0)  # Providing a default value if not found
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        nationality = request.POST.get('nationality')
        jobcategory = request.POST.get('jobcategory')
        passport = request.POST.get('passport')
        passportexpiry = request.POST.get('passportexpiry')
        department = request.POST.get('department')
        bloodgroup = request.POST.get('bloodgroup')
        diagnosisdiseases = request.POST.get('diagnosisdiseases')
        emergencymedicine = request.POST.get('emergencymedicine')
        emergencyphone = request.POST.get('emergencyphone', 0)
        domesticaddress = request.POST.get('domesticaddress')
        education = request.POST.get('education')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        camp = request.POST.get('camp')
        
        camp_id = request.POST.get('camp')
        if camp_id:
            camp = get_object_or_404(CampModel, pk=camp_id)
        else:
            camp = None

        # Fetch the Floor instance for the given floor ID
        floor_id = request.POST.get('floorNo')
        if floor_id:
            floorNo = get_object_or_404(Floor, floorid=floor_id)
        else:
            floorNo = None

        usertypeid  = request.POST.get('usertype')
        if usertypeid:
            usertype = get_object_or_404(UserTypeModel, usertypeid =usertypeid )
        else:
            usertype = None
        # Fetch the Flat instance for the given flat ID
        flat_id = request.POST.get('flatNo')
        if flat_id:
            flatNo = get_object_or_404(Flat, flatid=flat_id)
        else:
            flatNo = None

        # Fetch the RoomModel instance for the given room ID
        room_id = request.POST.get('RoomNo')
        if room_id:
            roomNo = get_object_or_404(RoomModel, roomid=room_id)
        else:
            roomNo = None

        # Fetch the TransportationModel instance for the given bus ID
        bus_id = request.POST.get('busNo')
        if bus_id:
            busNo = get_object_or_404(TransportationModel, pk=bus_id)
        else:
            busNo = None
       
        item_id = request.POST.get('itemNo')
        itemNo = get_object_or_404(ItemModel, pk=item_id) if item_id else None
       
        room_type_id = request.POST.get('roomTypeNo')
        roomTypeNo = get_object_or_404(RoomTypeModel, pk=room_type_id) if room_type_id else None
       
        bed_id = request.POST.get('bedNo')
        bedNo = None  # Default to None
        if bed_id:  # Check if bed_id is not empty
            try:
                bedNo = BedModel.objects.get(pk=bed_id)  # Try to fetch the BedModel instance
            except BedModel.DoesNotExist:
                # If no BedModel with the given ID exists, you can either set bedNo to None or handle the error as you see fit
                pass
       
        
        
        un = email
        pwd = password
        
       
       
        
        new_employee = EmployeeModel(
       
                name=name,
                phone=phone,
                dob=dob,
                address=address,
                nationality=nationality,
                jobcategory=jobcategory,
                passport=passport,
                passportexpiry=passportexpiry,
                department=department,
                bloodgroup=bloodgroup,
                diagnosisdiseases=diagnosisdiseases,
                emergencymedicine=emergencymedicine,
                emergencyphone=emergencyphone,
                domesticaddress=domesticaddress,
                education=education,
                email=email,
                password=password,
                camp=camp,
                bedid=bedNo,
                floorid=floorNo,
                flatid=flatNo,
                roomid=roomNo,
                itemid=itemNo,
                Roomtype = roomTypeNo,
                busid=busNo,
                usertypeid = usertype,
            )
        new_employee.save()
        ul = Login(username = email,password = password,emp_id=new_employee)
        ul.save()
        
       

        
    return render(request, './camp_app/campBossAddEmployee.html',context)

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if credentials are for the campBoss
        if username == 'campBoss' and password == 'camp':
            # Redirect to campBoss home page
            return redirect('campBossHome')  # Ensure 'campBossHome' is the correct URL pattern name

        # Check if credentials are for the messCaptain
        elif username == 'messcaptain' and password == 'camp1':
            # Redirect to messCaptain home page
            return render(request,'./camp_app/messcaptain.html')  # Ensure 'messCaptainHome' is the correct URL pattern name

        # For regular users
        else:
            login_data = Login.objects.filter(username=username, password=password)

            # Redirect users based on successful login
            if len(login_data) == 1:
                # creating session for username
                request.session['user'] = login_data[0].username
                request.session['id'] = login_data[0].emp_id.employeeid

                # Redirect to employee leave request page or any appropriate page for a normal employee
                return redirect(employeeLeaveRequest)

    # Render login page again if conditions are not met
    return render(request, './camp_app/login.html')




def employee_home_view(request):
    return render(request, './camp_app/EmployeeHome.html')

def mess_captain_home_view(request):
    # Your view logic here
    return render(request, './camp_app/messCaptainHome.html')


def hrAddFloor(request):
    context = {}
    
    if request.method == 'POST':
        floor = request.POST.get('floorNumber')
        
        if Floor.objects.filter(floorno=floor).exists():
            context['error'] = "Floor already exists"
        else:
            temp = Floor(floorno=floor)
            temp.save()
            context['success'] = True
        
    return render(request, './camp_app/hrAddFloor.html', context)



def hrAddFlat(request):
    if request.method=="POST":
        floorid=request.POST.get("floorNumber")
        floor=Floor.objects.get(floorid=floorid)
        flatno=request.POST.get("flatNumber")
        new=Flat.objects.create(flatnumber=flatno,floorno=floor)
        new.save()
        return redirect('./camp_app/hrAddFlats.html')
    else:
        displayFloor = Floor.objects.all()
        return render(request, './camp_app/hrAddFlats.html', {"Floor":displayFloor})



def hrCreateRoomType(request):
    
    if request.method == 'POST':
        type = request.POST.get('roomtype')
        number = request.POST.get('occupancy')
        
        RoomTypeModel(roomtypename=type, occupancy=number).save()
        return render(request, './camp_app/hrAddRoomType.html')
    else:
        return render(request, './camp_app/hrAddRoomType.html')
    
    

def hrAddRoom(request):
    
    if request.method == "POST":
        flatid = request.POST["flatNumber"]
        flat = Flat.objects.get(flatid=flatid)
        roomno = request.POST['roomNumber']
        roomtypeid = request.POST["roomtype"]
        roomtype = RoomTypeModel.objects.get(roomtypeid=roomtypeid)
        new = RoomModel.objects.create(roomnumber=roomno,flatid=flat,roomtypeid=roomtype)
        new.save()
        return redirect('./camp_app/hrAddRoom.html')
    else:
        displayFlat = Flat.objects.all()
        displayRoomType = RoomTypeModel.objects.all()
        return render(request, './camp_app/hrAddRoom.html',{"Flat":displayFlat, "RoomType": displayRoomType})


def hrAddBed(request):
    if request.method == "POST":
        roomid = request.POST["roomNumber"]
        room = RoomModel.objects.get(roomid=roomid)
        bedNumber = request.POST['bedNumber']
        new = BedModel.objects.create(roomid=room, number=bedNumber)
        new.save()
        return redirect('./camp_app/hrAddBed.html')
    else:
        displayRoom = RoomModel.objects.all()
        return render(request, "./camp_app/hrAddBed.html", {"Room":displayRoom})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployeeModel

@login_required
def employeeProfileView(request):
    try:
        id = request.session.get("id")
        employee = EmployeeModel.objects.get(employeeid=id)
        context = {'employee': employee}
        return render(request, 'camp_app/employeeProfileView.html', context)
    except EmployeeModel.DoesNotExist:
        return render(request, 'camp_app/no_employee_profile.html')
    

@login_required
def campBossProfileView(request):
    try:
        id = request.session.get("id")
        campBoss = EmployeeModel.objects.get(employeeid=id)
        context = {'employee': campBoss, 'user_type': 'CampBoss'}  # Include user_type in the context
        return render(request, 'camp_app/employeeProfileView.html', context)
    except EmployeeModel.DoesNotExist:
        return render(request, 'camp_app/no_campBoss_profile.html')








def hrEmployeeProfileView(request):
    profile_view = EmployeeModel.objects.all()
    context = {'profile' : profile_view}
    
    return render(request,'./camp_app/hrEmployeeProfileView.html', context)


def employeeViewBusSchedule(request):
    bus_schedule = TransportationModel.objects.all()
    context = {'bus' : bus_schedule}
    
    return render(request, './camp_app/employeeBusScheduleView.html', context)


def messCaptainViewMessSchedule(request):
    mess_schedule = MessModel.objects.all()
    context = {'mess' : mess_schedule}
    
    return render(request, './camp_app/messCaptainViewMessSchedule.html', context)


def messCaptainViewLeaveSchedule(request):
    leave_schedule = LeaveRequestModel.objects.all()
    context = {'leave' : leave_schedule}
    
    return render(request, './camp_app/messCaptainViewLeaveStatus.html', context)



def hrEmployeeLeaveStatus(request):
    # Fetch all leave status records
    leave_statuses = LeaveStatusModel.objects.all()
    context={'leave_status':leave_statuses}

    # Render the template with leave status data
    return render(request, './camp_app/hrEmployeeLeaveStatus.html',context)

def hr_leave_request_view(request):
    # Your view logic here
    return render(request, './camp_app/hrEmployeeLeaveRequestView.html')



from django.shortcuts import render
from .models import TransportationModel, CampModel

def campBossAddBus(request):
    camps = CampModel.objects.all()  # Query all camps to be passed into the context
    context = {'success': False, 'error': None, 'camps': camps}  # Include camps in context
    
    if request.method == 'POST':
        busname = request.POST.get('busname')
        destination = request.POST.get('destination')
        time = request.POST.get('time')
        campid = request.POST.get('campid')
        
        # Find the camp instance based on campid
        try:
            camp = CampModel.objects.get(pk=campid)
        except CampModel.DoesNotExist:
            context['error'] = "Selected camp does not exist."
            return render(request, './camp_app/campBossAddBus.html', context)

        # Check if the bus with this name already exists for the selected camp
        if TransportationModel.objects.filter(busname=busname, campid=camp).exists():
            context['error'] = "Bus with this name already exists for the selected camp."
        else:
            # Create the TransportationModel instance
            bus = TransportationModel(busname=busname, destination=destination, time=time, campid=camp)
            bus.save()
            context['success'] = True  # Set success to True after saving
    
    return render(request, './camp_app/campBossAddBus.html',context)

def hrViewComplaint(request):
    complaints = ComplaintModel.objects.all()
    context = {'complaints':complaints}
    return render(request,'./camp_app/hrViewComplaint.html',context)

def hrLeaveRequestView(request):
    leaverequests = LeaveRequestModel.objects.filter(approvalstatus='pending')
    context = {'a':leaverequests}
    return render(request,'./camp_app/hrLeaveRequestView.html',context)



from django.shortcuts import get_object_or_404, redirect
from .models import LeaveRequestModel, EmployeeModel

def approve_leave_request(request, request_id):
    leave_request = get_object_or_404(LeaveRequestModel, requestid=request_id)
    
    # Check if the leave request is still pending and if so, approve it
    if leave_request.approvalstatus == 'pending':
        leave_request.approvalstatus = 'approved'
        leave_request.save()
        
        # Get the associated employee
        employee = leave_request.employeeid
        
        # Reduce the employee's total number of leaves by the number of days requested
        # Ensure that we don't reduce below 0
        days_requested = leave_request.numberofdays
        if employee.totalNoOfLeave >= days_requested:
            employee.totalNoOfLeave -= days_requested
            employee.save()
        else:
            # Handle cases where the employee does not have enough leave days
            # This might involve setting the request to a different status or notifying someone
            pass
        
        # Redirect to a success page
        return redirect('hrLeaveRequestView')
    else:
        # Redirect or handle cases where the leave request is not pending
        return redirect('hrLeaveRequestView')


def reject_leave_request(request, request_id):
    leave_request = get_object_or_404(LeaveRequestModel, requestid=request_id)
    leave_request.approvalstatus = 'rejected'
    leave_request.save()
    return redirect('hrLeaveRequestView')  # Redirect to the leave request list page or wherever appropriate


def employeeLeaveStatus(request):
    try:
        # Assuming the EmployeeModel is linked to the User model via a 'user' field
        id = request.session["id"]
        employee = EmployeeModel.objects.get(employeeid = id)
        leave_requests = LeaveRequestModel.objects.filter(employeeid=employee)
    except EmployeeModel.DoesNotExist:
        leave_requests = None
    return render(request,'./camp_app/employeeLeaveStatus.html',{'leave_requests': leave_requests})

def employeemessview_schedule(request):
    mess_schedule = MessModel.objects.all()
    context = {'mess' : mess_schedule}
    
    return render(request, './camp_app/employeemessview_schedule.html', context)


def campbossviewmessschedule(request):
    mess_schedule = MessModel.objects.all()
    context = {'mess' : mess_schedule}
    
    return render(request, './camp_app/campbossviewmessschedule.html', context)


def viewBusSchedule(request):
    bus = TransportationModel.objects.all()
    context = {"a":bus}
    return render(request,"./camp_app/AllBusScheduleView.html",context)
