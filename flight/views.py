from django.shortcuts import render,redirect
from .models import train_register,flight_register
from datetime import datetime
from django.utils import timezone
from .amadeus_api import search_flights
# Create your views here.
def home(request):
    return render(request, 'index.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def find_source(mp,source):
    for ele in mp:
        if mp[ele]['city']==source:
            return mp[ele]['IATA']
    return None
def find_dest(mp,dest):
    for ele in mp:
        if mp[ele]['city']==dest:
            return mp[ele]['IATA']
    return None 
def str_to_date(s):
    dt = datetime.strptime("2025-04-12 15:30:45", "%Y-%m-%d %H:%M:%S")    
    return dt.time() 
def selection_view(request):
    indian_airports = {
    "Indira Gandhi International Airport": {"city": "Delhi", "IATA": "DEL"},
    "Chhatrapati Shivaji Maharaj International Airport": {"city": "Mumbai", "IATA": "BOM"},
    "Kempegowda International Airport": {"city": "Bengaluru", "IATA": "BLR"},
    "Rajiv Gandhi International Airport": {"city": "Hyderabad", "IATA": "HYD"},
    "Netaji Subhas Chandra Bose International Airport": {"city": "Kolkata", "IATA": "CCU"},
    "Chennai International Airport": {"city": "Chennai", "IATA": "MAA"},
    "Sardar Vallabhbhai Patel International Airport": {"city": "Ahmedabad", "IATA": "AMD"},
    "Cochin International Airport": {"city": "Kochi", "IATA": "COK"},
    "Goa International Airport": {"city": "Goa", "IATA": "GOI"},
    "Pune Airport": {"city": "Pune", "IATA": "PNQ"},
    "Lokpriya Gopinath Bordoloi International Airport": {"city": "Guwahati", "IATA": "GAU"},
    "Sri Guru Ram Dass Jee International Airport": {"city": "Amritsar", "IATA": "ATQ"},
    "Thiruvananthapuram International Airport": {"city": "Thiruvananthapuram", "IATA": "TRV"},
    "Jay Prakash Narayan International Airport": {"city": "Patna", "IATA": "PAT"},
    "Veer Savarkar International Airport": {"city": "Port Blair", "IATA": "IXZ"},
    "Bagdogra Airport": {"city": "Bagdogra", "IATA": "IXB"},
    "Biju Patnaik International Airport": {"city": "Bhubaneswar", "IATA": "BBI"},
    "Jolly Grant Airport": {"city": "Dehradun", "IATA": "DED"},
    "Dr. Babasaheb Ambedkar International Airport": {"city": "Nagpur", "IATA": "NAG"},
    "Lal Bahadur Shastri International Airport": {"city": "Varanasi", "IATA": "VNS"},
    "Mangaluru International Airport": {"city": "Mangaluru", "IATA": "IXE"},
    "Madurai Airport": {"city": "Madurai", "IATA": "IXM"},
    "Tirupati Airport": {"city": "Tirupati", "IATA": "TIR"},
    "Coimbatore International Airport": {"city": "Coimbatore", "IATA": "CJB"},
    "Visakhapatnam Airport": {"city": "Visakhapatnam", "IATA": "VTZ"},
    "Jaipur International Airport": {"city": "Jaipur", "IATA": "JAI"},
    "Srinagar Airport": {"city": "Srinagar", "IATA": "SXR"},
    "Leh Airport": {"city": "Leh", "IATA": "IXL"},
    "Agartala Airport": {"city": "Agartala", "IATA": "IXA"},
    "Imphal Airport": {"city": "Imphal", "IATA": "IMF"},
    "Dimapur Airport": {"city": "Dimapur", "IATA": "DMU"},
    "Shillong Airport": {"city": "Shillong", "IATA": "SHL"},
    "Silchar Airport": {"city": "Silchar", "IATA": "IXS"},
    "Dibrugarh Airport": {"city": "Dibrugarh", "IATA": "DIB"},
    "Jorhat Airport": {"city": "Jorhat", "IATA": "JRH"},
    "Tezpur Airport": {"city": "Tezpur", "IATA": "TEZ"},
    "Lilabari Airport": {"city": "Lilabari", "IATA": "IXI"},
    "Aizawl Airport": {"city": "Aizawl", "IATA": "AJL"},
    "Lengpui Airport": {"city": "Lengpui", "IATA": "AJL"},
    "Itanagar Airport": {"city": "Itanagar", "IATA": "HGI"},
    "Pasighat Airport": {"city": "Pasighat", "IATA": "IXT"},
    "Ziro Airport": {"city": "Ziro", "IATA": "ZER"},
    "Daporijo Airport": {"city": "Daporijo", "IATA": "DAE"},
    "Along Airport": {"city": "Along", "IATA": "IXV"},
    "Tawang Airport": {"city": "Tawang", "IATA": "TWI"},
    "Khowai Airport": {"city": "Khowai", "IATA": "IXN"},
    "Kailashahar Airport": {"city": "Kailashahar", "IATA": "IXH"},
    "Kamalanagar Airport": {"city": "Kamalanagar", "IATA": "IXQ"},
    "Kamalpur Airport": {"city": "Kamalpur", "IATA": "IXQ"},
    "Agatti Airport": {"city": "Agatti Island", "IATA": "AGX"},
    "Kadapa Airport": {"city": "Kadapa", "IATA": "CDP"},
    "Rajahmundry Airport": {"city": "Rajahmundry", "IATA": "RJA"},
    "Vijayawada Airport": {"city": "Vijayawada", "IATA": "VGA"},
    "Gaya Airport": {"city": "Gaya", "IATA": "GAY"},
    "Durgapur Airport": {"city": "Durgapur", "IATA": "RDP"},
    "Jharsuguda Airport": {"city": "Jharsuguda", "IATA": "JRG"},
    "Jammu Airport": {"city": "Jammu", "IATA": "IXJ"},
    "Kangra Airport": {"city": "Kangra", "IATA": "DHM"},
    "Shimla Airport": {"city": "Shimla", "IATA": "SLV"},
    "Kullu–Manali Airport": {"city": "Kullu", "IATA": "KUU"},
    "Pantnagar Airport": {"city": "Pantnagar", "IATA": "PGH"},
    "Bareilly Airport": {"city": "Bareilly", "IATA": "BEK"},
    "Kanpur Airport": {"city": "Kanpur", "IATA": "KNU"}}
    transport_type = request.GET.get('type', 'flight') 
    cities=['Delhi', 'Mumbai', 'Bengaluru', 'Hyderabad', 'Kolkata', 'Chennai', 'Ahmedabad', 'Kochi', 'Goa', 'Pune', 'Guwahati', 'Amritsar', 'Thiruvananthapuram', 'Patna', 'Port Blair', 'Bagdogra', 'Bhubaneswar', 'Dehradun', 'Nagpur', 'Varanasi', 'Mangaluru', 'Madurai', 'Tirupati', 'Coimbatore', 'Visakhapatnam', 'Jaipur', 'Srinagar', 'Leh', 'Agartala', 'Imphal', 'Dimapur', 'Shillong', 'Silchar', 'Dibrugarh', 'Jorhat', 'Tezpur', 'Lilabari', 'Aizawl', 'Lengpui', 'Itanagar', 'Pasighat', 'Ziro', 'Daporijo', 'Along', 'Tawang', 'Khowai', 'Kailashahar', 'Kamalanagar', 'Kamalpur', 'Agatti Island', 'Kadapa', 'Rajahmundry', 'Vijayawada', 'Gaya', 'Durgapur', 'Jharsuguda', 'Jammu', 'Kangra', 'Shimla', 'Kullu', 'Pantnagar', 'Bareilly', 'Kanpur']
    error = None
    previous_data = {
        'email': '',
        'source': '',
        'dest': '',
        'date': ''
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        source = request.POST.get('source')
        dest= request.POST.get('dest')
        date = request.POST.get('date')
        previous_data = {
            'email': email,
            'source': source,
            'dest': dest,
            'date': date
        }
        try:
            selected_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            selected_date = None

        today = timezone.now().date()

        if not selected_date or selected_date <= today:
            error = "⚠️ Please select a date that is in the future."
            return render(request, 'selection.html', {'type': transport_type,'cities':cities,'error':error,'previous_data': previous_data})


        s=find_source(indian_airports,source)
        d=find_dest(indian_airports,dest)
        flights = search_flights(s, d, selected_date)
        if transport_type == "flight" and (not flights or "data" not in flights or len(flights["data"]) == 0):
            error=f"No flights found from {source} to {dest} on {date}."
            return render(request, 'selection.html', {'type': transport_type,'cities':cities,'error':error,'previous_data': previous_data})

            
        else:
            if transport_type == 'flight':
                flight_register.objects.create(
                    email=email,
                    source=source,
                    dest=dest,
                    date=date
                )
            elif transport_type == 'train':
                train_register.objects.create(
                    email=email,
                    source=source,
                    dest=dest,
                    date=date
                )
            carrier_dict = flights.get("dictionaries", {}).get("carriers", {})

            flight_info_list = []

            for i, offer in enumerate(flights["data"][:2]):
                itinerary = offer["itineraries"][0]["segments"][0]
                seats = offer.get("numberOfBookableSeats", "N/A")

                carrier_code = itinerary["carrierCode"]
                flight_number = itinerary["number"]
                airline_name = carrier_dict.get(carrier_code, carrier_code)  # fallback to code if not found

                flight_info_list.append({
                    "source": source,
                    "dest": dest,
                    "date": date,
                    "flight_name": airline_name,
                    "source_iata": itinerary["departure"]["iataCode"],
                    "dest_iata": itinerary["arrival"]["iataCode"],
                    "Airline": airline_name,
                    "Flight": flight_number,
                    "Departure": str_to_date(itinerary["departure"]["at"]),
                    "Arrival": str_to_date(itinerary["arrival"]["at"]),
                    "Remaining_seats": seats
                })

            return render(request, 'success.html', {
                'flight_details': flight_info_list
            })
        
 # or a confirmation page
    return render(request, 'selection.html', {'type': transport_type,'cities':cities,'error':error,'previous_data': previous_data})
